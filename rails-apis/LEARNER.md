# APIs with Ruby on Rails

Learner preparation guide. Use the matching course in CSG Learn for recordings, submissions and questions. Recordings and admissions are pending; these files alone do not grant access. All practice data is fictional.

## Orientation and first run

Required

# APIs with Ruby on Rails

Complete Ruby Fundamentals or equivalent methods, arrays, hashes and conditionals first. Complete the free versioned Mac/Windows-WSL setup bridge before the route lesson. Rails runs locally; Hafa Ruby is for the single-file bridge only.

Work through three weeks: nine teaching lessons, twelve exercises, two checkpoints and one independent project. Plan roughly 4–6 hours of practice per week, with time to revise. All examples are fictional. Use your own harmless practice data; keep private records and credentials out of submissions. A paid coding agent is not required.

Predict before running, change one thing, compare expected with actual output, then explain the result. Worked examples use separate data; integrate the assessed starter yourself. Save exact source and output in the corresponding exercise. An accessible project/repository link may accompany the saved source. For help, include the smallest failing code, expected result and actual error.

First task: run a greeting (or preview the three frontend starter files), change one word and run again. Submit source and output or a preview screenshot. Done when you can reopen it and reproduce the result.

# Rails setup bridge — version 2026-10-04

Teaching runtime: **Ruby 3.3.4, Rails 8.1.3.1, Bundler 4.0.7**, the supplied Gemfile.lock, SQLite (no PostgreSQL server). Keep these versions for the recordings; review supported patch updates before selling a later edition. Existing supported Ruby can be accepted only after the instructor reruns the exact kit. Do not overwrite a learner's existing version-manager setup. No fresh OS install is claimed by this document.

Official sources checked 2026-10-04: [Rails installation](https://guides.rubyonrails.org/install_ruby_on_rails.html), [rbenv](https://github.com/rbenv/rbenv#installation), [ruby-build dependencies](https://github.com/rbenv/ruby-build/wiki), [Microsoft WSL](https://learn.microsoft.com/en-us/windows/wsl/install). Upstream examples may choose the newest versions; this kit deliberately pins its teaching runtime. No external page substitutes for the course-specific commands below.

## macOS Terminal

1. If absent, install Apple's Command Line Tools with `xcode-select --install`; finish the installer. Install Homebrew from its [official installer](https://brew.sh/) if absent, and apply the displayed Apple Silicon or Intel shell PATH instructions. Existing users skip those installations.
2. In Terminal run:
```sh
brew install rbenv ruby-build openssl@3 readline libyaml gmp autoconf sqlite
rbenv init
```
Read and apply rbenv's displayed shell initialization instructions, then open a new Terminal. Do not paste a second initialization into an already configured shell. Run:
```sh
rbenv install -s 3.3.4
```
Installation may take several minutes. If compilation fails, keep the final error and ask staff; do not switch randomly to the macOS system Ruby.

## Windows: administrator PowerShell, then Ubuntu

Windows 11 or supported Windows 10 build 19041+. In administrator PowerShell:
```powershell
wsl --install --distribution Ubuntu-24.04
```
Restart if asked. Open Ubuntu from Start; create its Linux username/password. The following commands are in Ubuntu, **not PowerShell**. Keep the project in `~/csg-courses`, not a Windows-mounted folder.
```sh
sudo apt update
sudo apt install -y build-essential autoconf patch libssl-dev libyaml-dev zlib1g-dev libgmp-dev libreadline-dev libffi-dev rustc git curl sqlite3 libsqlite3-dev
```
For a new rbenv installation only:
```sh
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
export PATH="$HOME/.rbenv/bin:$PATH"
rbenv init
```
Apply the printed Bash shell instructions, then reopen Ubuntu. Existing version-manager users keep their configuration. Run `rbenv install -s 3.3.4`. Fresh WSL install/version acceptance remains an instructor checklist item; the commands are prepared, not an observed Windows pass.

## Shared course setup, inside the supplied app

Copy the course's **starter** folder into your own projects; keep the reference separate. In its directory:
```sh
rbenv local 3.3.4
ruby -v
gem install bundler -v 4.0.7
bundle _4.0.7_ install
bundle exec rails -v
bin/rails db:prepare
bin/rails routes
bin/rails server -b 127.0.0.1 -p 3000
```
Expected versions: ruby 3.3.4; Rails 8.1.3.1. On the checked teaching machine an uninitialized shell selected `/usr/bin/ruby` 2.6.10: use `rbenv exec ruby` to diagnose, then repair shell initialization instead of installing gems into system Ruby.

In a second terminal, from the same project:
```sh
curl -i http://127.0.0.1:3000/api/v1/practice_sessions
```
Expected starter result: 200 with `[]`. Workshop recording app uses `/api/v1/workshops` instead. A connection failure means the server did not start or the port differs; inspect its terminal. A 404 means check path and routes. If port 3000 is occupied, do not stop that process: use `-p 3100` and change every request URL. Never delete an existing project DB to make an output match.

Before proceeding, learner demonstrates a greeting, the Ruby bridge, matching versions, routes, empty-list request and server shutdown with Ctrl+C. Save the commands/results in Learn. Rails course assumes this setup is complete before its short route lesson. Staff rehearses both a fresh Mac and a fresh Windows/WSL account before claiming those paths accepted. Do not commit config/master.key, credentials, storage SQLite files or logs. Never bind this unauthenticated exercise to a public interface. This setup is a free prerequisite, not part of the nine short paid teaching clips.


## Lesson 1: Ruby bridge

Required

# Lesson 1 — Ruby bridge

Rails still uses Ruby. This fictional workshop record has title and capacity keys. A method receives that record and returns an interpolated label. Our second method accepts an array; sum asks each record for capacity and adds those values. An empty array produces zero. Predict six plus four before Run. The quotes around the label make text; the returned total remains a number. Try a second title, then restore the checked file. Your A1 and A2 use the different practice-session fields topic and minutes. Explain the difference between returning and printing, and show your empty-array result. If this is difficult, stop for the Ruby Fundamentals bridge. A framework does not remove those prerequisites.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

Run `rbenv exec ruby practice/01-bridge.rb`: Git practice: 6 seats; 10; 0. No server.
### 01-bridge.rb

```ruby
def label(record)
  "#{record[:title]}: #{record[:capacity]} seats"
end
def total_seats(records)
  records.sum { |record| record[:capacity] }
end
puts label({ title: "Git practice", capacity: 6 })
puts total_seats([{ capacity: 6 }, { capacity: 4 }])
puts total_seats([])
```


## A1: Practice after Lesson 1

Required

## A1

Write `session_label({topic: "Ruby", minutes: 25})` → `Ruby: 25 minutes`.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## A2: Practice after Lesson 1

Required

## A2

Write `total_minutes` for `[{topic: "Ruby", minutes: 25}, {topic: "SQL", minutes: 20}]` and `[]`; return a number to the caller. If either is difficult, complete Ruby Fundamentals first or use a guided bridge.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 2: HTTP and JSON

Required

# Lesson 2 — HTTP and JSON

An HTTP request has a method, a path, headers and sometimes a body. The method expresses the action; the path identifies the collection or record. GET reads, POST creates, PATCH changes fields, DELETE removes. JSON object keys and string values use double quotes; a number is unquoted. The outer workshop key groups fields expected by our controller. Content-Type application/json tells Rails how to read the body. The response status states the result, while the body carries data or an error. Two hundred succeeds, two-oh-one creates, two-oh-four intentionally has no body. Four-oh-four means missing here; four-twenty-two means invalid declared data. These are choices for this API contract, not a claim every API works identically. Pause and match every card. A3 and A4 apply those ideas to practice sessions.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

Write the five cards `GET /api/v1/workshops → 200 []`, `GET /:id → 200 {...}`, `POST → 201 {...}`, `PATCH /:id → 200 {...}`, `DELETE /:id → 204 empty`; add invalid POST → 422 errors. Type valid JSON `{"workshop":{"title":"Git practice","capacity":6,"starts_on":"2026-12-01"}}`.

## A3: Practice after Lesson 2

Required

## A3

Match GET/POST/PATCH/DELETE to read/create/change/remove and write expected statuses 200/201/200/204.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## A4: Practice after Lesson 2

Required

## A4

Sketch a valid JSON object for one session and a 422 error response for negative minutes.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 3: Routes and initial controller

Required

# Lesson 3 — Routes and initial controller

Use the supplied local demo and complete the free setup first. Namespace api then v1 creates the path prefix and controller module names. Resources declares collection and member routes for the five named actions. The index controller action currently renders an empty array so we can verify the route before adding persistence. Rails routes shows the verb, path and action together. Start the server and leave its terminal open; the second terminal sends requests. Curl minus-i includes headers so we see the status as well as the JSON. Predict an empty array and run. A connection error means check the server; a route mismatch means inspect the URL and routes. Stop only this server with Control-C. Your separate starter uses practice_sessions. A5 locates its index and A6 temporarily replaces the empty list with one fictional object, then restores it before database work.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

In a disposable copy of workshop_api_demo, replace controller and model from practice/03-routes. Run `bundle check`, `bin/rails db:prepare`, `bin/rails routes`. Start `bin/rails server -b 127.0.0.1 -p 3107`; in a second terminal `curl -i http://127.0.0.1:3107/api/v1/workshops` → 200 [] . Ctrl+C.
### routes.rb

```ruby
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :workshops, only: %i[index show create update destroy]
    end
  end
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Defines the root path route ("/")
  # root "posts#index"
end
```

### model.rb

```ruby
class Workshop < ApplicationRecord
end
```

### controller.rb

```ruby
module Api
  module V1
    class WorkshopsController < ApplicationController
      def index
        render json: []
      end
      def show
        head :not_implemented
      end
      def create
        head :not_implemented
      end
      def update
        head :not_implemented
      end
      def destroy
        head :not_implemented
      end
    end
  end
end
```


## A5: Practice after Lesson 3

Required

## A5

Run `bin/rails routes`, identify the index route, and request it.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## A6: Practice after Lesson 3

Required

## A6

Change the starter index from `[]` to a temporary hard-coded one-record JSON array, request it, then revert before connecting the database.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Checkpoint 1

Required

Explain aloud or in writing what the request `GET /api/v1/practice_sessions` asks for, where Rails routes it, why a successful index returns 200, and why a JSON array is appropriate. Run the starter and submit the response plus route line. Passing evidence: correct route, status, JSON shape, and request path.

## Lesson 4: Storage and validation

Required

# Lesson 4 — Storage and validation

The migration defines a workshops table: text title, integer capacity, date starts-on and timestamps. Database-prepare creates or updates this local SQLite file; it is not a remote database server. Active Record maps each row to a Workshop. Create-bang tries to save and raises if invalid, so use fictional data and read the returned id. Count may exceed one in a reused copy: compare before and after rather than deleting data. Presence rejects a blank title or missing date. Numericality with only-integer rejects a fraction; greater-than-or-equal-to zero accepts zero and rejects negatives. Valid-question checks without saving. Run three otherwise-valid records with negative, zero, fractional capacity. The actual migration controls storage, while model validation checks what should be accepted. Your A7/A8 implement those rules for practice-session minutes and prove a rejected record did not persist.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

Apply 04-model. Show migration and schema. Run `bin/rails db:prepare`; `bin/rails console`; create `Workshop.create!(title: "Git practice", capacity: 6, starts_on: "2026-12-01")`; record returned id/count; `Workshop.new(title: "Git practice", capacity: -1, starts_on: "2026-12-01").valid?` → false. Test capacity 0 → true, 2.5 → false; exit.
### routes.rb

```ruby
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :workshops, only: %i[index show create update destroy]
    end
  end
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Defines the root path route ("/")
  # root "posts#index"
end
```

### model.rb

```ruby
class Workshop < ApplicationRecord
  validates :title, presence: true
  validates :capacity, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
  validates :starts_on, presence: true
end
```

### controller.rb

```ruby
module Api
  module V1
    class WorkshopsController < ApplicationController
      def index
        render json: []
      end
      def show
        head :not_implemented
      end
      def create
        head :not_implemented
      end
      def update
        head :not_implemented
      end
      def destroy
        head :not_implemented
      end
    end
  end
end
```

### 20260927113623_create_workshops.rb

```ruby
class CreateWorkshops < ActiveRecord::Migration[8.1]
  def change
    create_table :workshops do |t|
      t.string :title
      t.integer :capacity
      t.date :starts_on

      t.timestamps
    end
  end
end
```


## A7: Practice after Lesson 4

Required

## A7

Run `bin/rails db:prepare`, then create a fictional session in `bin/rails console` and count records.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## A8: Practice after Lesson 4

Required

## A8

Add model validations for topic, minutes, and date; prove separately that blank topic, missing date, negative minutes and fractional minutes are invalid, while zero minutes is valid. Keep all other fields valid in each test.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 5: Read with callback

Required

# Lesson 5 — Read with callback

This callback is essential. Before-action runs set-session before show, update and destroy; percent-i writes the list of action symbols. Set-session uses find-by to return a model or nil. Rendering a missing error with not-found ends the callback chain, so the action never reads a nil record. An at-sign variable belongs to this controller request and passes the found record to show. Index orders by date then id and map builds one payload per record. Payload selects only id, title, capacity and an ISO date string. Show uses that same shape. Predict a real-id response and a missing-id response before running both. The method alone is not enough: omit the callback and show crashes. Your A9/A10 use practice sessions. Keep the callback, intentional fields, stable ordering and missing-id JSON together.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

Apply 05-read. Highlight `before_action :set_session, only: %i[show update destroy]` before showing methods. Start server3107; GET collection→200 ordered array, GET returned ID→200 fields, GET999999→404 {"error":"workshop not found"}. Keep this server for6–7.
### routes.rb

```ruby
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :workshops, only: %i[index show create update destroy]
    end
  end
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Defines the root path route ("/")
  # root "posts#index"
end
```

### model.rb

```ruby
class Workshop < ApplicationRecord
  validates :title, presence: true
  validates :capacity, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
  validates :starts_on, presence: true
end
```

### controller.rb

```ruby
module Api
  module V1
    class WorkshopsController < ApplicationController
      before_action :set_session, only: %i[show update destroy]
      def index
        sessions = Workshop.order(:starts_on, :id)
        render json: sessions.map { |session| payload(session) }
      end

      def show
        render json: payload(@session)
      end
      def create
        head :not_implemented
      end
      def update
        head :not_implemented
      end
      def destroy
        head :not_implemented
      end
      private
      def set_session
        @session = Workshop.find_by(id: params[:id])
        render json: { error: "workshop not found" }, status: :not_found unless @session
      end

      def payload(session)
        { id: session.id, title: session.title, capacity: session.capacity, starts_on: session.starts_on.iso8601 }
      end
    end
  end
end
```


## A9: Practice after Lesson 5

Required

## A9

Implement index in ascending date/id order and show two records.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## A10: Practice after Lesson 5

Required

## A10

Implement show and return `{"error":"session not found"}` with 404 for an unknown ID.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 6: Create and errors

Required

# Lesson 6 — Create and errors

Require selects the outer workshop object; permit allows only title, capacity and starts-on. Strong parameters restrict writes, not who is authenticated. New builds an unsaved object. Save returns true or false; on true render the payload with created, on false render model errors with unprocessable-content. That status is numeric four-twenty-two. Send one valid body, take its actual id, then change only capacity to negative one. The other fields remain valid so this request tests exactly that rule. Compare collection size before and after: invalid input must not create a row. JSON headers and a correct envelope matter; a malformed request is a different failure. A11/A12 use the separate practice-session endpoint and show both status and body. Keep exact requests in your submission, not screenshots of code only.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

Apply06-create while same demo server reloads development code. POST with header Content-Type:application/json and body {"workshop":{"title":"API practice","capacity":4,"starts_on":"2026-12-02"}} →201; recordid. POST same otherwise-valid body with capacity -1→422; GET count unchanged.
### routes.rb

```ruby
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :workshops, only: %i[index show create update destroy]
    end
  end
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Defines the root path route ("/")
  # root "posts#index"
end
```

### model.rb

```ruby
class Workshop < ApplicationRecord
  validates :title, presence: true
  validates :capacity, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
  validates :starts_on, presence: true
end
```

### controller.rb

```ruby
module Api
  module V1
    class WorkshopsController < ApplicationController
      before_action :set_session, only: %i[show update destroy]
      def index
        sessions = Workshop.order(:starts_on, :id)
        render json: sessions.map { |session| payload(session) }
      end

      def show
        render json: payload(@session)
      end
      def create
        session = Workshop.new(session_params)
        if session.save
          render json: payload(session), status: :created
        else
          render json: { errors: session.errors.full_messages }, status: :unprocessable_content
        end
      end
      def update
        head :not_implemented
      end
      def destroy
        head :not_implemented
      end
      private
      def session_params
        params.require(:workshop).permit(:title, :capacity, :starts_on)
      end
      def set_session
        @session = Workshop.find_by(id: params[:id])
        render json: { error: "workshop not found" }, status: :not_found unless @session
      end

      def payload(session)
        { id: session.id, title: session.title, capacity: session.capacity, starts_on: session.starts_on.iso8601 }
      end
    end
  end
end
```


```sh
curl -i http://127.0.0.1:3107/api/v1/workshops
curl -i -X POST http://127.0.0.1:3107/api/v1/workshops -H 'Content-Type: application/json' -d '{"workshop":{"title":"API practice","capacity":4,"starts_on":"2026-12-02"}}'
curl -i -X POST http://127.0.0.1:3107/api/v1/workshops -H 'Content-Type: application/json' -d '{"workshop":{"title":"API practice","capacity":-1,"starts_on":"2026-12-02"}}'
WORKSHOP_ID=REPLACE_WITH_YOUR_ACTUAL_ID
curl -i "http://127.0.0.1:3107/api/v1/workshops/$WORKSHOP_ID"
curl -i http://127.0.0.1:3107/api/v1/workshops/999999
curl -i -X PATCH "http://127.0.0.1:3107/api/v1/workshops/$WORKSHOP_ID" -H 'Content-Type: application/json' -d '{"workshop":{"capacity":8}}'
curl -i -X PATCH "http://127.0.0.1:3107/api/v1/workshops/$WORKSHOP_ID" -H 'Content-Type: application/json' -d '{"workshop":{"capacity":-1}}'
curl -i "http://127.0.0.1:3107/api/v1/workshops/$WORKSHOP_ID"
curl -i -X DELETE "http://127.0.0.1:3107/api/v1/workshops/$WORKSHOP_ID"
curl -i "http://127.0.0.1:3107/api/v1/workshops/$WORKSHOP_ID"
```

For negative create/update use the identical valid request and change only capacity to -1. Do not run commands with the placeholder id. All requests, fields, file changes and error demonstrations are exercised by `scripts/rehearse_recording.py` against ephemeral app copies without a server. The human capture uses the same states with curl.



## A11: Practice after Lesson 6

Required

## A11

Implement POST and show a valid 201 response.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## A12: Practice after Lesson 6

Required

## A12

Send negative minutes and show a 422 JSON `errors` array; explain why the record was not saved.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Checkpoint 2

Required

With a clean local DB, POST a valid record, GET it by ID, and POST an invalid record. Submit the exact requests, statuses, and bodies. Passing evidence: created ID, persisted show result, validation failure without a new row, and no unpermitted field appearing in the response.

## Lesson 7: Update and delete

Required

# Lesson 7 — Update and delete

Update uses the found at-sign model and the same permitted fields. A partial request need not resend title and date. Predict capacity eight, then send the PATCH. Now deliberately send negative one: validation fails, and a new GET must still show eight. That distinguishes a displayed error from correct stored state. Destroy-bang removes the found row; head no-content gives a two-oh-four response without JSON. Get the deleted id again: it must return missing. Use the id from your response, not an assumed one. The callback serves all these member actions and remains installed. Your Week 3 log shows update, invalid update, delete and subsequent missing lookup on your own practice API. Do not delete unrelated data to prepare a demo.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

Apply07-crud. Set task-specific `WORKSHOP_ID` to actual createdid. PATCH URL with body {"workshop":{"capacity":8}}→200 capacity8; PATCH capacity -1→422; GET shows8. DELETE→204 empty; GET sameid→404.
### routes.rb

```ruby
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :workshops, only: %i[index show create update destroy]
    end
  end
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Defines the root path route ("/")
  # root "posts#index"
end
```

### model.rb

```ruby
class Workshop < ApplicationRecord
  validates :title, presence: true
  validates :capacity, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
  validates :starts_on, presence: true
end
```

### controller.rb

```ruby
module Api
  module V1
    class WorkshopsController < ApplicationController
      before_action :set_session, only: %i[show update destroy]

      def index
        sessions = Workshop.order(:starts_on, :id)
        render json: sessions.map { |session| payload(session) }
      end

      def show
        render json: payload(@session)
      end

      def create
        session = Workshop.new(session_params)
        if session.save
          render json: payload(session), status: :created
        else
          render json: { errors: session.errors.full_messages }, status: :unprocessable_content
        end
      end

      def update
        if @session.update(session_params)
          render json: payload(@session)
        else
          render json: { errors: @session.errors.full_messages }, status: :unprocessable_content
        end
      end

      def destroy
        @session.destroy!
        head :no_content
      end

      private

      def set_session
        @session = Workshop.find_by(id: params[:id])
        render json: { error: "workshop not found" }, status: :not_found unless @session
      end

      def session_params
        params.require(:workshop).permit(:title, :capacity, :starts_on)
      end

      def payload(session)
        { id: session.id, title: session.title, capacity: session.capacity, starts_on: session.starts_on.iso8601 }
      end
    end
  end
end
```


```sh
curl -i http://127.0.0.1:3107/api/v1/workshops
curl -i -X POST http://127.0.0.1:3107/api/v1/workshops -H 'Content-Type: application/json' -d '{"workshop":{"title":"API practice","capacity":4,"starts_on":"2026-12-02"}}'
curl -i -X POST http://127.0.0.1:3107/api/v1/workshops -H 'Content-Type: application/json' -d '{"workshop":{"title":"API practice","capacity":-1,"starts_on":"2026-12-02"}}'
WORKSHOP_ID=REPLACE_WITH_YOUR_ACTUAL_ID
curl -i "http://127.0.0.1:3107/api/v1/workshops/$WORKSHOP_ID"
curl -i http://127.0.0.1:3107/api/v1/workshops/999999
curl -i -X PATCH "http://127.0.0.1:3107/api/v1/workshops/$WORKSHOP_ID" -H 'Content-Type: application/json' -d '{"workshop":{"capacity":8}}'
curl -i -X PATCH "http://127.0.0.1:3107/api/v1/workshops/$WORKSHOP_ID" -H 'Content-Type: application/json' -d '{"workshop":{"capacity":-1}}'
curl -i "http://127.0.0.1:3107/api/v1/workshops/$WORKSHOP_ID"
curl -i -X DELETE "http://127.0.0.1:3107/api/v1/workshops/$WORKSHOP_ID"
curl -i "http://127.0.0.1:3107/api/v1/workshops/$WORKSHOP_ID"
```

For negative create/update use the identical valid request and change only capacity to -1. Do not run commands with the placeholder id. All requests, fields, file changes and error demonstrations are exercised by `scripts/rehearse_recording.py` against ephemeral app copies without a server. The human capture uses the same states with curl.



## Lesson 8: Tests that catch a specific bug

Required

# Lesson 8 — Tests that catch a specific bug

The test client sends requests directly to Rails; it does not need our running web server. Each test gets isolated data. The workflow checks create, list, show, change, delete and missing lookup. The negative-capacity test has a valid title and date, so only capacity can make it fail. Separate tests cover blank title, missing date, a fraction, zero and invalid PATCH preserving the old value. Assert-response checks the status; parsed-body inspects JSON; count proves whether data changed. Run the correct suite first. Comment only the capacity numericality line and run the named negative test. It now creates with two-oh-one when four-twenty-two was expected. Restore that exact line, rerun the targeted test, then the full suite. That is a defect the test truly catches. A copied multi-error input would hide the regression. Write and submit analogous tests for your independent practice API; the final reference remains private.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

Show test/integration/workshops_api_test.rb in worked demo. Stopserver. Run `PARALLEL_WORKERS=1 bin/rails test test/integration/workshops_api_test.rb` → checked count below. In disposable copy comment only capacity numericality validation, run targeted `-n /validation_errors/` → failure201 vs422. Restore exact model and rerun targeted/full; show all pass.
### routes.rb

```ruby
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :workshops, only: %i[index show create update destroy]
    end
  end
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Defines the root path route ("/")
  # root "posts#index"
end
```

### model.rb

```ruby
class Workshop < ApplicationRecord
  validates :title, presence: true
  validates :capacity, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
  validates :starts_on, presence: true
end
```

### controller.rb

```ruby
module Api
  module V1
    class WorkshopsController < ApplicationController
      before_action :set_session, only: %i[show update destroy]

      def index
        sessions = Workshop.order(:starts_on, :id)
        render json: sessions.map { |session| payload(session) }
      end

      def show
        render json: payload(@session)
      end

      def create
        session = Workshop.new(session_params)
        if session.save
          render json: payload(session), status: :created
        else
          render json: { errors: session.errors.full_messages }, status: :unprocessable_content
        end
      end

      def update
        if @session.update(session_params)
          render json: payload(@session)
        else
          render json: { errors: @session.errors.full_messages }, status: :unprocessable_content
        end
      end

      def destroy
        @session.destroy!
        head :no_content
      end

      private

      def set_session
        @session = Workshop.find_by(id: params[:id])
        render json: { error: "workshop not found" }, status: :not_found unless @session
      end

      def session_params
        params.require(:workshop).permit(:title, :capacity, :starts_on)
      end

      def payload(session)
        { id: session.id, title: session.title, capacity: session.capacity, starts_on: session.starts_on.iso8601 }
      end
    end
  end
end
```

### workshops_api_test.rb

```ruby
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
```


## Independent final project

Required

 — complete and verify

| Lesson | Goal | Artifact |
|---|---|---|
| 7. Update and delete | PATCH one field, DELETE a record, return 404 afterward | Submit request/response log for valid PATCH, invalid PATCH preserving the stored value, DELETE and 404 afterward. |
| 8. Request tests | Use Rails integration tests for the full workflow and an invalid request | Submit passing test output and one test that failed before you fixed a bug. |
| 9. Explain the API | Trace route → controller → model → SQLite → JSON; state limits | Submit repository or zip, README with setup and example requests, test output, and 2–4 minute walkthrough or written equivalent. |

## Local setup and acceptance

Use Ruby 3.3.4 and Rails 8.1.3.1 for the supplied reference, or a compatible environment verified by the instructor. In `study_api_starter` run `bundle install`, `bin/rails db:prepare`, and `bin/rails server`. In a second terminal, `curl -i http://127.0.0.1:3000/api/v1/practice_sessions` should initially return status 200 and `[]`. Stop the server when finished. A fresh Rails project may have different dependency versions and command output. Use the supplied starter to keep the recording consistent.

Final acceptance: all five actions work under `/api/v1`; successful create returns 201; bad data returns 422 and explanatory JSON; unknown ID returns 404; delete returns 204; dates are ISO formatted; input only accepts declared fields; request tests pass from a fresh test DB. 

Submit code and request logs in CSG Learn. A Hafa link to a Ruby file is suitable for the bridge, but the Rails project should be shared as a GitHub repository or zip. Never commit `config/master.key`, real credentials, or `storage/*.sqlite3`. This starter contains no credential key.



## Independent work

Use the unfinished starter. Explain your integration and one failed-then-repaired case. The assessed reference is released only after submission.



| Item | Points |
|---|---:|
| GET collection and one-record response, ordered and intentional JSON | 2 |
| POST creates 201, invalid POST returns 422 without a row | 2 |
| PATCH and DELETE update storage, correct statuses | 2 |
| Unknown ID returns clear 404 | 1 |
| Model validations and permitted attributes | 1 |
| Automated request tests cover workflow and invalid input | 1 |
| README explains setup, examples, and local-only limitation | 1 |



Use the supplied study_api_starter project archive. Keep its routes/model/controller/migration together. The setup bridge above defines exact runtime and commands.

### Independent project review

Use the published point weights. Individual scoring applies only when included in the learner’s enrollment. Self-paced learners can use these criteria for self-review.

- **GET responses (2 points):** Return an ordered collection and a one-record response with intentional JSON.
- **POST (2 points):** Return 201 for valid creation; return 422 without persisting invalid input.
- **PATCH and DELETE (2 points):** Update storage and return appropriate statuses for updates and deletion.
- **Unknown ID (1 point):** Return a clear 404 for an unknown record.
- **Validation and parameters (1 point):** Validate model data and permit only intended attributes.
- **Request tests (1 point):** Automated tests cover the request workflow and invalid input.
- **README (1 point):** Explain setup, examples and the limits of a local practice API.

## Lesson 9: Explain and transfer

Required

# Lesson 9 — Explain and transfer

Trace POST through the route into create, through permitted fields into the model, through validation into SQLite, then back through payload to JSON with created status. Trace invalid minutes in your own project separately; do not simply rename my output. Your final practice-session API requires five actions, stable reads, clear missing and invalid errors, boundary tests and a setup README. Explain one test that failed before your fix and one limitation. This local exercise has no authentication, authorization or production deployment. Binding a teaching server to localhost and stopping it afterward keeps the scope honest. Submit your exact repository or zip and request logs; exclude keys, databases and logs. The optional summary endpoint is released after independent submission, not mixed into the core demonstration. No paid agent is needed to pass.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

Show worked routes/controller/model/migration/test output. Show final learner starter TODOs without filling them. Verify README commands and stop owned server if any.
### routes.rb

```ruby
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      resources :workshops, only: %i[index show create update destroy]
    end
  end
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Reveal health status on /up that returns 200 if the app boots with no exceptions, otherwise 500.
  # Can be used by load balancers and uptime monitors to verify that the app is live.
  get "up" => "rails/health#show", as: :rails_health_check

  # Defines the root path route ("/")
  # root "posts#index"
end
```

### model.rb

```ruby
class Workshop < ApplicationRecord
  validates :title, presence: true
  validates :capacity, numericality: { only_integer: true, greater_than_or_equal_to: 0 }
  validates :starts_on, presence: true
end
```

### controller.rb

```ruby
module Api
  module V1
    class WorkshopsController < ApplicationController
      before_action :set_session, only: %i[show update destroy]

      def index
        sessions = Workshop.order(:starts_on, :id)
        render json: sessions.map { |session| payload(session) }
      end

      def show
        render json: payload(@session)
      end

      def create
        session = Workshop.new(session_params)
        if session.save
          render json: payload(session), status: :created
        else
          render json: { errors: session.errors.full_messages }, status: :unprocessable_content
        end
      end

      def update
        if @session.update(session_params)
          render json: payload(@session)
        else
          render json: { errors: @session.errors.full_messages }, status: :unprocessable_content
        end
      end

      def destroy
        @session.destroy!
        head :no_content
      end

      private

      def set_session
        @session = Workshop.find_by(id: params[:id])
        render json: { error: "workshop not found" }, status: :not_found unless @session
      end

      def session_params
        params.require(:workshop).permit(:title, :capacity, :starts_on)
      end

      def payload(session)
        { id: session.id, title: session.title, capacity: session.capacity, starts_on: session.starts_on.iso8601 }
      end
    end
  end
end
```


## Optional review after independent submission

Optional



The required project and rubric above are completed and explained without an agent. After that submission, offer the optional agent-assisted extension. The learner can use Codex desktop, another coding agent they already have, or the saved code and tests without an AI account. They inspect the proposed change and rerun the original project before accepting it. No AI subscription or optional-extension score is required to pass.

**Expected checks:** Original CRUD still works; empty summary is zero; Ruby 60, SQL 20, total 80 in the fictional test. Write tests in your own project for the original behavior and the changed-data/edge cases listed above. Staff assessment tests are not a learner dependency. Ask for a prompt or change request, one accepted or rejected line with a reason, the original and extended outputs, and one edge-case test.  Follow the optional recorded example in this lesson after submitting your independent project.



This is optional and does not affect required completion. You may use an agent you already have or review the saved change without an account. Request instructor release of the review fixture after the independent project.
