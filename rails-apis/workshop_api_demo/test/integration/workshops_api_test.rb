require "test_helper"

class WorkshopsApiTest < ActionDispatch::IntegrationTest
  test "create list show update and delete a session" do
    post "/api/v1/workshops", params: { workshop: { title: "Ruby", capacity: 25, starts_on: "2026-09-27" } }, as: :json
    assert_response :created
    id = response.parsed_body.fetch("id")
    assert_equal "Ruby", response.parsed_body.fetch("title")

    get "/api/v1/workshops"
    assert_response :success
    assert_equal 1, response.parsed_body.length

    get "/api/v1/workshops/#{id}"
    assert_equal 25, response.parsed_body.fetch("capacity")

    patch "/api/v1/workshops/#{id}", params: { workshop: { capacity: 30 } }, as: :json
    assert_response :success
    assert_equal 30, response.parsed_body.fetch("capacity")

    delete "/api/v1/workshops/#{id}"
    assert_response :no_content
    get "/api/v1/workshops/#{id}"
    assert_response :not_found
  end

  test "validation errors do not create bad data" do
    post "/api/v1/workshops", params: { workshop: { title: "Ruby", capacity: -5, starts_on: "2026-09-27" } }, as: :json
    assert_response :unprocessable_content
    assert response.parsed_body.fetch("errors").any?
    assert_equal 0, Workshop.count
  end

  test "unexpected attributes are not written" do
    post "/api/v1/workshops", params: { workshop: { title: "SQL", capacity: 15, starts_on: "2026-09-27", admin: true } }, as: :json
    assert_response :created
    refute response.parsed_body.key?("admin")
  end

  test "blank title alone is rejected" do
    post "/api/v1/workshops", params: { workshop: { title: " ", capacity: 0, starts_on: "2026-09-27" } }, as: :json
    assert_response :unprocessable_content
    assert response.parsed_body.fetch("errors").any?
    assert_equal 0, Workshop.count
  end

  test "missing date alone is rejected" do
    post "/api/v1/workshops", params: { workshop: { title: "Ruby", capacity: 0 } }, as: :json
    assert_response :unprocessable_content
    assert response.parsed_body.fetch("errors").any?
    assert_equal 0, Workshop.count
  end

  test "fractional capacity alone are rejected" do
    post "/api/v1/workshops", params: { workshop: { title: "Ruby", capacity: 2.5, starts_on: "2026-09-27" } }, as: :json
    assert_response :unprocessable_content
    assert response.parsed_body.fetch("errors").any?
    assert_equal 0, Workshop.count
  end

  test "invalid patch preserves stored capacity" do
    record = Workshop.create!(title: "Ruby", capacity: 25, starts_on: "2026-09-27")
    patch "/api/v1/workshops/#{record.id}", params: { workshop: { capacity: -1 } }, as: :json
    assert_response :unprocessable_content
    assert response.parsed_body.fetch("errors").any?
    assert_equal 25, record.reload.capacity
    assert_equal 1, Workshop.count
  end

  test "zero capacity is a valid boundary" do
    post "/api/v1/workshops", params: { workshop: { title: "Ruby", capacity: 0, starts_on: "2026-09-27" } }, as: :json
    assert_response :created
    assert_equal 0, response.parsed_body.fetch("capacity")
    assert_equal 1, Workshop.count
  end

end
