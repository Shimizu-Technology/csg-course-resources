# AI Engineering with Python

Learner preparation guide. Use the matching course in CSG Learn for recordings, submissions and questions. Recordings and admissions are pending; these files alone do not grant access. All practice data is fictional.

## Orientation — Your tools, access and evidence

Required

Build a small Python workflow that proposes categories for fictional support requests and leaves every decision to a human. You will learn contracts, safe failure, evaluation and cost accounting around a model call. This course does not promise employment or teach autonomous customer support. Your project will never send a reply or change an account.

Prerequisites: Python functions, dictionaries, lists, exceptions and reading a traceback. You must also be able to explain JSON, make an HTTP POST and run a small `unittest` suite. If HTTP/JSON/testing is new, complete `practice/bridge.py` and the bridge reading below before Lesson 4. Python Fundamentals alone does not teach those prerequisites. A laptop and standard-library Python are sufficient for offline practice; use the free setup companion for Mac or Windows/WSL. No paid AI subscription or personal provider API key is required. Hafa can be used for self-contained offline snippets if its Python runner is available; multi-file imports, environment variables and the supplied HTTPS client require your local terminal unless staff has verified the hosted route.

Download the learner bundle from the course resources. It contains this reading, `learner/student_triage.py`, public tests, `project/client.py`, fictional cases and `practice/` examples. Staff solutions, the provider service, seat registry and budget database are private infrastructure. Work in a copy; preserve the original starter and keep your own Git commit history locally.

Plan about 5–7 hours each week: watch and rehearse, attempt four exercises, complete the checkpoint, then work on your independent project. Spread practice across the week. Pause whenever a command or a concept is unclear; a shorter successful attempt is better than typing without understanding. Ask support with the file, sanitized error and what you expected. Never include a credential or a real person's request.

CSG provides individual course access with a fixed allowance. Staff must privately give you the approved HTTPS endpoint, a course token, the exact call allowance and expiry, and the process for access problems. The provider credential stays on CSG's server. Your course token is also a credential: keep it out of your editor, recordings, Git, screenshots and submissions. Set it in the local terminal privately using `getpass`; do not paste it into a command visible in shell history. Access not yet provided? Complete offline exercises and ask staff before attempting Lesson 4's live step. A fixture run cannot replace the assessed real-model evidence.

From the downloaded course folder, run `python3 practice/bridge.py` (Windows/WSL: the same command inside WSL). Three tests should pass. The bridge uses an in-memory fake transport and opens no network connection. Explain: `json.loads` turns JSON text into Python values; JSON `true` becomes Python `True`; `json.dumps(...).encode()` produces the bytes sent in an HTTP body. `Request` makes a POST when it has a body. `Content-Type` tells the recipient the body's format. `timeout=5` limits waiting; it does not retry. `transport` is a function parameter so a test can inspect the request without contacting a server. The response remains untrusted even if the HTTP request succeeded.

In `practice/bridge.py`, change the fake reply from `true` to `"true"` temporarily. The contract check must reject the string. Restore it, rerun, and explain why a boolean matters. If the tests cannot run, resolve Python/path setup before progressing. Keep offline artifacts clearly labeled. Later live results must come from the actual CSG endpoint and include their prompt version, model, usage and observation time.

## Lesson 1 — Give the model one bounded job

Required

A useful AI application starts with a job description and a decision boundary. Our fictional support triage chooses `account`, `lesson` or `billing` and proposes `routine` or `urgent`. A human checks the original fictional message, the proposal and its reason. The program never sends a customer response. Choosing labels narrows the job and makes mistakes measurable.

The lesson's worked practice uses a different task: fictional workshop supply requests for `paper` or `marker`, with a whole quantity from 1 to 10. That task lets you learn the mechanism without receiving the final project's answer. The locations and requests are fictional; there are no claims about Guam prices, business operations or legal requirements. A Guam workshop is a useful context for short messages, small teams and careful human review. It does not justify processing real student or payment information.

Write down who supplies the text, what the program may output, who approves it and what happens on failure. For support triage, all successful proposals still require review; a timeout leaves the person to classify manually. An unclear message is not permission to invent facts. A prompt asking for a private key is data to classify, never an instruction to execute. You will test that boundary later.

Run `python3 practice/states/01_json.py`. It prints `paper`, `5`, then `{"item": "paper", "quantity": 3}`. The request's quantity is the integer 3; adding 2 does arithmetic. JSON is a transport format, not a guarantee of correct values. A program can decode a bad answer successfully. Exercise 1 defines the job; Exercise 2 checks that distinction.

## Exercise 1 — Write the job boundary

Required

Submit 120–180 words defining the fictional support input, category/urgency labels, human approver, failure path and prohibited automatic actions. Include why a small Guam workshop or course team might need predictable routing and why that does not justify using real private data. Pass when the job is bounded and every proposal stays human reviewed. Suggested time: 15 minutes.

## Exercise 2 — Decode and inspect JSON

Required

In `exercise_2.py`, decode `{"item":"marker","quantity":2}` using `json.loads`. Print the item, the quantity plus 1, and serialized JSON. Then explain why JSON `{"item":[],"quantity":true}` decodes but violates the supply contract. Expected normal values: `marker` and `3`. Submit your file and a 2–3 sentence explanation. Suggested time: 20 minutes.

## Lesson 2 — Validate before spending a call

Required

Validation means checking your contract before using data. Strip surrounding spaces, require the expected type, reject an empty value, and enforce bounds. A type check must happen before membership in a set: a list cannot be used as a set key. Python booleans are a subtype of integer, so `type(quantity) is int` rejects `True` when the contract requires a whole quantity.

Read and run `practice/states/02_validate.py`. `json.loads` may decode a list or number as well as an object. We first require a dictionary and exactly the two expected fields; then check the item's type and label; then check the quantity's type and range. The valid result is `{'item': 'paper', 'quantity': 3}`. The boolean example prints `Repair: Quantity must be a whole number from 1 to 10`. A `ValueError` names a contract failure the caller can handle. Catch it where the user needs a clear recovery path.

For your support project, require 1–500 characters after stripping and reject obvious credential assignments such as `password is FICTIONAL_ONLY`, `api_key=FICTIONAL_ONLY`, or a provider-key-shaped `sk-...` string. A password-reset question is allowed. This small heuristic is not a privacy guarantee; use fictional data only. Do not send text that contains real names, contact details, account identifiers or secrets. Do not put rejected text into diagnostics.

Implement your own `clean_message` for Exercise 3. Test empty text, spaces, exactly 500 characters, 501 characters, a list and a password-reset question. Verify that rejected input never calls the supplied predictor. A filter after a model call is too late to prevent the disclosure or the spend.

## Exercise 3 — Implement independent input validation

Required

Implement `clean_message` in your starter. Require a string whose stripped length is 1–500; return stripped text. Reject obvious `password`, `api_key`, `secret` or `token` assignments using `is`, `=` or `:`, and key-shaped `sk-` values with at least eight following letters/digits/underscores/hyphens. Permit a password-reset question. Add six boundary examples, including 500/501 characters and a list. No model call, real secret or private text. Submit your function and results; invalid inputs must raise `ValueError`. Suggested time: 35 minutes.

## Lesson 3 — Require a result contract

Required

A result can be syntactically valid JSON and still be wrong. Define exact keys, allowed labels and a bounded reason. For the support task, allow exactly `category`, `urgency`, `reason`. Category must be a string in `account`, `lesson`, `billing`; urgency a string in `routine`, `urgent`; reason a nonblank string with 1–120 stripped characters. Return a new clean dictionary. Reject extra fields rather than treating model output as code or commands.

Structured Outputs lets the server ask the selected model for a JSON Schema. It helps enforce shape; it does not prove the category or explanation is correct. A refusal, interrupted response, invalid result or missing usage must still have a safe application path. Your independent result validator protects the application boundary even though CSG also validates its service response.

Inspect the supply example again. Predict what `{'item': [], 'quantity': 3}` and `{'item':'paper','quantity':3,'send':True}` do. Both must raise `ValueError`. If your implementation raises `TypeError`, move the type check before the label membership test. Never use `eval` on a model answer. Exercise 4 applies these checks to your own output contract; Checkpoint 1 asks you to explain the difference between valid JSON and a valid proposal.

## Exercise 4 — Validate the independent proposal

Required

Implement `parse_proposal` accepting a JSON string or dictionary. Require exactly category, urgency and reason; enforce the labels and stripped reason length from Lesson 3. Reject extra keys, wrong types, blank reasons and 121-character reasons with `ValueError`. A malformed JSON string also fails. Test an unhashable category list to prove the type check precedes set membership. Submit your function and at least six examples. Suggested time: 35 minutes.

## Checkpoint 1 — Contracts before the call

Required

Submit Exercises 1–4 and run the input/output acceptance tests with your own file. From `learner/`: `python3 -m unittest test_student_triage.StudentContractTest.test_input_boundaries test_student_triage.StudentContractTest.test_output_boundaries -v`. These two tests should pass; the remaining starter functions are not implemented yet. Explain why `True` is not an acceptable quantity, why an extra model field is rejected, and why a password-reset question differs from a credential assignment. Staff checks four things: explicit bounded job; correct types/keys/bounds; zero calls for rejected text; recovery language that reveals no private input. Repair material failures before live calls. Suggested time: 30 minutes.

## Lesson 4 — Connect HTTP without exposing a key

Required

An HTTP request has a destination, method, headers and body. In `practice/states/03_http.py`, the fake transport inspects a POST containing JSON bytes and returns an in-memory response. Run it. The output starts `MOCK TRANSPORT — NO NETWORK`, then `{'accepted': True}`. No model or endpoint was contacted. This injection is the same pattern you will use to test timeouts and malformed replies.

CSG supplies `project/client.py` as infrastructure. It reads a privately supplied HTTPS endpoint and your individual course token, sends fictional text with a prompt version, refuses redirects, bounds its response, and accepts only the known human-review envelope. Your code still validates `result`. A provider API key never belongs on a learner computer. CSG's local rehearsal server is staff-only and cannot be substituted for the HTTPS endpoint.

For the live step, staff must first confirm access and remaining allowance. Off camera, start a local Python shell from `project/` and enter:

```python
import os, getpass
os.environ['CSG_TRIAGE_URL'] = input('Private CSG HTTPS endpoint: ')
os.environ['CSG_COURSE_TOKEN'] = getpass.getpass('Individual course token: ')
from client import request_triage
response = request_triage('The fictional exercise blocks me today.', 'v1')
print(response['status'])
```

Do not print the environment, request headers or token. If the status is `proposed`, inspect and validate its result and metrics. If access is limited, contact staff; do not retry in a loop. A failed attempt may use allowance and may still incur provider cost. Once finished, remove the two variables and exit the shell. Save only sanitized result evidence. If access is unavailable, record the blocked step and continue offline work; the live requirement remains pending.

The app's safe statuses are `blocked`, `review_needed`, `access_limited` and `proposed`. Every one has `review_required: True`. Implement `run_triage(message, predict)` using an injected predictor: clean input, call once, validate a proposal, and fall back to review on timeout or invalid output. Exercises 5 and 6 build and test that pipeline. No automatic retry or automatic action is allowed.

## Exercise 5 — Connect a supplied predictor once

Required

Implement `run_triage(message, predict)` using your own two validators. A fake predictor returns `{'status':'proposed','review_required':True,'result':{'category':'lesson','urgency':'routine','reason':'Fictional content question.'}}`. Return a validated proposal with `review_required: True`. Use a calls list to prove clean input triggers exactly one call and credential-shaped input triggers zero. Preserve the allowed blocked/review_needed/access_limited statuses from the supplied predictor. Submit your code and call-count evidence. Suggested time: 35 minutes.

## Exercise 6 — Repair a failing transport

Required

Extend your pipeline to handle a predictor that raises `TimeoutError` or `OSError`, returns a list, or returns an invalid proposal. Return `review_needed` and require human review, without exposing raw errors, input bodies or credentials. Never retry automatically. Test a supplied `access_limited` response separately; it must remain access_limited and must not be retried. Submit failure outputs and describe the manual recovery. Suggested time: 30 minutes.

## Lesson 5 — Label cases before evaluating

Required

You need examples with expected answers before measuring results. Keep development cases separate from evaluation cases. Label each fictional message yourself using the written policy before running predictions. Give it a unique ID. Include straightforward cases, an unclear access request and a message that tries to redirect the model's instructions. Flag ambiguity; an expected label is a policy choice, not a fact about a real person.

The supply practice has three cases. Run `python3 practice/states/04_evaluate.py`: the fixed heuristic matches 2 of 3 and misses `p3`, which asks for a sheet. The denominator stays three. A failure is part of the evidence. Category and urgency are separate match counts in support triage; a category match cannot hide an urgency mismatch. A refusal or timeout stays in the denominator and also counts as a fallback.

The provided six support cases are a published rehearsal set. Once you have inspected them, they are not an unseen final benchmark. Keep them unchanged for a reproducible comparison and add at least four new labeled fictional cases that your prompt changes did not target. Do not tune on these new cases before your final run. A tiny set teaches evaluation; it cannot establish production reliability.

Implement `evaluate_cases(cases, predict)` in your own project. Return `count`, `category_matches`, `urgency_matches`, `fallbacks`, and one row per case with ID, both match booleans, `review_needed` and `ambiguous`. Reports omit message bodies. Empty or invalid case sets must raise `ValueError`. Exercises 7 and 8 establish the labels and honest counts.

## Exercise 7 — Create labeled fictional cases

Required

Create `my_cases.json` with at least four unique IDs, fictional messages, expected category and urgency, and an `ambiguous: true` flag where relevant. Include an ordinary account question, a billing question, a blocked exercise and an ambiguous access question. Label them before prediction. Explain the policy for the ambiguous case. Freeze these cases before the final prompt comparison; do not change the expected answers to match a model. Suggested time: 30 minutes.

## Lesson 6 — Improve one thing and preserve evidence

Required

A baseline is useful because it makes a change testable. Keep the earlier prompt and earlier results. In the supply practice, v1 recognizes `paper` but not `sheet`. `practice/states/05_improve.py` adds that one synonym. It matches all three cases. This is deterministic fixture behavior, not measured model accuracy. Test a new message too; a perfect tiny set can simply mean the code has memorized the examples.

CSG exposes support prompts `v1` and `v2` for comparison. V2 clarifies account access/password reset and urgency for an explicitly blocked current task or a today deadline. Read `project/prompts.md`. Compare versions on exactly the same labeled cases and report both independent label counts, fallbacks and ambiguous cases. Do not rename v2 output as baseline or overwrite v1 evidence. Your recommendation should explain which failure changed and what still needs a person.

Staff can run the supplied evaluation CLI. The provided learner wiring calls your own functions without giving you their implementation. After completing the starter, from the course folder run `python3 learner/run_project.py --mode fixture --version v1 --output my-evidence/offline-v1.json`. This uses one fixed offline answer, not a classifier; v2 can produce identical fixture counts. Use `--mode live` and a new filename for actual CSG observations. The runner prompts for endpoint and token using hidden input and waits for you to resume capture; the variables last only for that process. Choose `--cases my_cases.json` for your four frozen cases. You may instead call your own evaluation with the supplied client and save sanitized JSON. Your final report must identify whether each artifact is a fixture or an actual CSG endpoint observation. A fixture run may demonstrate the evaluation mechanism but earns no credit for the real-model criterion. If the model changes its answer between calls, preserve that observation; don't keep retrying until it looks better.

Checkpoint 2 asks for the before/after comparison, failures left in the denominator, and an honest limitation. Do not claim that six examples prove a prompt safe, accurate or useful for real support.

## Exercise 8 — Count every evaluation attempt

Required

Implement `evaluate_cases(cases, predict)` with the exact fields in Lesson 5. Test two labeled cases against a fixed proposal: expected category/urgency match totals must be computed separately. Test an all-failure predictor: count is two, both match totals zero, fallbacks two. Reject an empty list and malformed/duplicate-ID cases. Keep case IDs and ambiguity in report rows; omit message bodies. Submit code and both reports. Suggested time: 45 minutes.

## Checkpoint 2 — Evidence before a stronger prompt claim

Required

Submit Exercises 5–8, one fixed-case evaluation and one all-failure evaluation. Show that rejected inputs call zero times, valid inputs once, and timeout does not retry. All-failure counts must remain in the denominator. Preserve your four new labels before trying v2. Explain one ambiguous policy decision and one limitation of a tiny fictional set. Staff checks safe fallback, independent counts, frozen cases and an honest fixture/live label. A missing live endpoint does not block this offline checkpoint; it remains a separate project access gate. Suggested time: 40 minutes.

## Lesson 7 — Track cost, latency and privacy honestly

Required

A model call can fail after spending tokens. Input and output token usage have separate rates. Estimated cost equals `input_tokens * input_rate / 1_000_000 + output_tokens * output_rate / 1_000_000`. Rates live in a staff-controlled model manifest and must be rechecked against official provider pricing. The supplied adapter records its configured model, token counts, prompt version, estimated cost and elapsed milliseconds for usable results. A reservation counter is a separate allowance record, not an invoice.

Run `python3 practice/states/06_metrics.py`. Two attempts include a known estimate of `0.000045` and a failure with no provider usage. Both attempts count. The example's latency average is 100 ms; these are synthetic teaching numbers. Missing usage is unknown cost, not a free call. Your `summarize_attempts` returns attempts, fallbacks, the sum of known estimates and the number of attempts whose cost is unknown. Zero is a valid known cost in an offline fixture, so do not use a truthiness test to decide whether usage is present.

CSG's server reserves a technical allowance atomically before each call. Its call limit is enforceable; a reserved money estimate is not a guaranteed provider billing hard cap. Staff must manage actual provider account budgets, review usage and recheck rates. An exhausted or expired seat returns `access_limited`; failed attempts remain reserved. This makes silent retries particularly harmful.

Only use fictional text. The secret heuristic misses many sensitive values. `store: false` requests that the provider not store this response for later API retrieval; it is not a promise of zero retention, zero logging or universal regional residency. Do not record real credentials even as an example. Exercise 9 compares versions without overclaiming; Exercise 10 records known and unknown costs and your privacy rules.

## Exercise 9 — Preserve a prompt comparison

Required

Use the same six published rehearsal cases for v1 and v2; then run the four cases you labeled before prediction. Preserve separate before/after artifacts, version identifiers and fixture/live labels. Write 100–150 words naming one changed failure, one remaining uncertainty and why this sample cannot establish real support accuracy. If live access is unavailable, submit fixture evidence labeled offline and mark the actual model step pending; do not claim completion of the live criterion. Suggested time: 45 minutes excluding access resolution.

## Exercise 10 — Summarize metrics without hiding unknown cost

Required

Implement `summarize_attempts(attempts)`. Return `attempts`, `fallbacks`, `known_estimated_usd` (sum rounded to eight decimal places) and `unknown_cost_attempts`. Use three rows: proposed with cost 0, review_needed with no usage, proposed with cost 0.000045. Expected: 3 attempts, 1 fallback, known sum 0.000045, 1 unknown-cost attempt. Reject an empty list. Include a privacy checklist covering fictional data, private token handling, no automatic retries and reservation versus actual billing. Suggested time: 35 minutes.

## Lesson 8 — Make human review a real decision

Required

Human review means a person reads the original fictional message, the proposal and its reason, then chooses allowed labels. A model's `reason` is explanatory text, not authority. Prompt injection inside a request must remain data; do not execute anything it asks. Ambiguous cases especially need a policy decision. If the model has no usable result, the human can classify manually rather than approving a nonexistent proposal.

Run `python3 practice/states/07_review.py`. A person changes a supply proposal from marker to paper. The returned record is `{'status': 'human_reviewed', 'item': 'paper', 'changed': True}`. No purchase order was sent. Apply that mechanism yourself with support category and urgency. `human_review` must reject wrong types and labels, return the person's chosen labels and mark whether the choice differed. Do not remove `review_required` from an unreviewed proposal just to make a demo feel complete.

Exercise 11 records an override and a manual decision after a failure. In your project demo, explain what the application would never do automatically and who resolves an uncertain category. This course ends at a local decision record. Deployment, real customer data, reply generation and account actions need a separate design and permission process.

## Exercise 11 — Record a human override

Required

Implement `human_review(response, category, urgency)`. The person must select allowed string labels. Return `status: human_reviewed`, their category and urgency, and `changed` if either label differs from the proposal; a missing proposal counts as changed. Reject lists and unknown labels with `ValueError`. Demonstrate overriding a lesson/routine proposal to account/urgent and manually classifying a review_needed response. State that no response or account action is sent. Suggested time: 30 minutes.

## Project — Independent fictional support triage

Required

Implement the six functions in `learner/student_triage.py` yourself: `clean_message`, `parse_proposal`, `run_triage`, `evaluate_cases`, `summarize_attempts`, `human_review`. Use CSG's supplied client for real predictions and injected fakes for tests. Do not import the staff `service.py`, staff reference or offline triage implementation as your answer. The worked supply example teaches the mechanisms; your support code and tests are the independent transfer.

Deliver your code, at least nine meaningful local tests, four newly labeled fictional cases, separate v1/v2 sanitized reports on the six published cases and your four new cases, a metric summary with unknown usage visible, one human override, and a README/4–6 minute demonstration. Keep local Git history. Submit files/text through Learn as instructed by staff; no production deployment is required. The six functions and acceptance conditions are defined in Exercises 3–11. You may improve the clarity of your code without changing the contract.

At least one comparison must use the actual CSG model endpoint and its configured model, prompt version, usage and observation time. Do not call an offline heuristic AI. If access has not been provisioned, your code may be reviewed but the actual-model criterion is pending. Staff must provide the fixed allowance and expiry privately; do not buy access to work around a CSG access problem. Use no real private text.

Rubric, 10 points: input/output contracts and independent tests (2); one-call safe pipeline and actual-model connection evidence (2); evaluation with independent category/urgency counts, failures and new frozen cases (2); honest known/unknown cost, privacy and allowance handling (2); explicit human decision plus clear evidence/limitations (2). Each dimension earns 2 for complete and explained, 1 for partly correct, 0 for missing or materially unsafe. Pass requires at least 8/10, all public acceptance tests passing and no exposed credentials, automatic action, hidden failure denominator or invented live evidence. A missing actual model run keeps that criterion pending until CSG access works. Expected project effort: 4–6 hours across Week 3.

### Independent support-triage project

Assess the learner’s implementation and explanation using the required evidence. Supplied transport and allowance infrastructure are not independently assessed.

- **Contracts and independent tests:** Validate input/output types, fields and bounds; explain meaningful tests written for the independent learner functions.
- **Safe pipeline and actual model evidence:** Make at most one prediction call, preserve safe failure and demonstrate an actual CSG model connection with sanitized observations.
- **Evaluation and preserved evidence:** Count category and urgency separately, retain failures and ambiguity, and compare frozen published plus newly labeled cases.
- **Cost, privacy and allowance handling:** Distinguish known estimates from unknown usage, protect credentials and fictional data, and handle access limits without automatic retries.
- **Human decision and explanation:** Record an explicit allowed human choice, demonstrate an override, and explain evidence and remaining limitations.

## Lesson 9 — Present evidence and limits

Required

A useful demonstration shows a normal case, a rejected input, a provider failure and a human override. Start from a clean local copy and show your own functions and passing public tests. Explain one line of your validator and one row of your evaluation so a reviewer can tell that you understand your code.

Present both prompt versions and sanitized artifacts, not only your best result. State the model and prompt used in actual calls, the number of cases, both match counts, fallbacks, unknown costs and ambiguous decisions. For a deterministic fixture say exactly that it is not a model call. Do not turn a tiny fictional evaluation into a production-readiness claim.

The assessed work is your independent Python input/output validation, safe pipeline, evaluation, honest metric summary and human decision. CSG's transport, model adapter and allowance service are supplied infrastructure, not your assessed implementation. Exercise 12 prepares your README and screen walkthrough. A short recording can pause at a failure to explain repair; it does not need to hide the failure. Finish by identifying one improvement and one remaining limitation.

## Exercise 12 — Rehearse your independent project explanation

Required

Write a README with prerequisites, local run/test commands, private access configuration, fixture versus live evidence, prompt versions and limits. Rehearse a 4–6 minute walkthrough showing normal input, blocked input, failure fallback, human override and your comparison. Explain your own validator and evaluation code. Include the remaining model/deployment limitation; never include a token, real request or provider key. Submit the README and sanitized evidence or recording. Suggested time: 35 minutes.

## Extension — Strengthen the bridge and challenge your cases (optional)

Optional

Run `python3 practice/bridge.py` and explain its three tests without looking at the supplied comments. Add a malformed response case and a timeout fake in your own copy. Then add two new fictional support cases that expose a limitation of your written label policy. Do not tune the prompt after reading their model result; preserve them as follow-up evidence. Write whether an unclear label is a prompt problem, a policy problem or missing context. No extra live calls are required beyond the approved allowance. This extension is optional and does not replace any project gate. Suggested time: 45–60 minutes.
