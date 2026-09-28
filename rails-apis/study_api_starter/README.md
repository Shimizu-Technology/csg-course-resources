# Practice Sessions API — learner starter

Local Rails 8.1.3.1 / Ruby 3.3.4 project. It deliberately contains TODO controller actions and model validations. It is not a public production service. Begin with the [course overview](../README.md), then follow the full lessons in CSG Learn when the course opens.

Run `bundle install`, `bin/rails db:prepare`, and `bin/rails server`. In another terminal, `curl -i http://127.0.0.1:3000/api/v1/practice_sessions` returns 200 and `[]` initially. Fill the TODOs so POST, GET one, PATCH, DELETE, 404, and 422 behave as specified. Run the starter test with `bin/rails test`, then add request tests for the actions you implement.

Never commit generated `config/master.key`, real credentials, or SQLite databases.
