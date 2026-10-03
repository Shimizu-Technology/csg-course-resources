# Practice Sessions API — learner starter

Local Rails 8.1.3.1 / Ruby 3.3.4 project. It deliberately contains TODO controller actions and model validations. It is not a public production service. Follow `../LEARNER.md` and the nine recordings.

Run `bundle install`, `bin/rails db:prepare`, and `bin/rails server`. In another terminal, `curl -i http://127.0.0.1:3000/api/v1/practice_sessions` returns 200 and `[]` initially. Fill the TODOs so POST, GET one, PATCH, DELETE, 404, and 422 behave as specified. Add request tests. The assessed staff reference is withheld. Submit your own attempt in Learn and ask for feedback.

Never commit generated `config/master.key`, real credentials, or SQLite databases.
