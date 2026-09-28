require "test_helper"

class PracticeSessionsBaselineTest < ActionDispatch::IntegrationTest
  test "a fresh project lists no practice sessions" do
    get "/api/v1/practice_sessions"

    assert_response :success
    assert_equal [], response.parsed_body
  end
end
