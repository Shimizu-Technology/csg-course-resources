# Fictional expense-report repair

This is a disposable teaching repository. No real expenses, credentials, external services or automatic agent execution belong here. You need Python 3 and Git; no packages are installed.

## Acceptance contract

`summarize(rows)` receives an iterable of rows. A row must be a dictionary. Its category must be a nonblank string; strip surrounding whitespace before grouping and preserve internal spaces/case. Its amount must be an int or finite float, nonnegative; bool is invalid and zero is valid. Integers are finite even when large. Text is invalid; do not silently coerce it. Count each invalid row once, continue to later valid rows and create no category for rejected rows. Missing fields and non-dictionary rows are invalid. Empty input returns empty totals and zero invalid rows. Return exactly `{"totals": {...}, "invalid_rows": number}`. This exercise uses fictional numbers to teach validation, not production currency accounting or exact Decimal arithmetic.

Run `python3 -B -m unittest -v test_report.py` from this folder. The starter deliberately reports three failures and one error. Preserve that evidence before asking for a fix. Run all supplied checks with `python3 -B -m unittest -v test_report.py test_acceptance_edges.py`. The starter is intentionally incomplete.

Create your own branch before edits: `git switch -c fix-expense-validation`. Agent edits are limited to report.py. You may author a new meaningful test yourself in test_student_case.py; label it as your work and do not change supplied tests. Ask for a plan, review scope, approve only a narrow proposal, inspect every diff hunk and run tests yourself. A model response is untrusted text, not permission to execute commands.

Use CSG's assigned supported coding tool within the published fixed allowance, or the staff-provided saved-output equivalent if access fails. Ask staff for the course route; do not buy a personal plan or use a shared staff login/key. Record the route and actual version if available. Save prompt/response evidence and your human review. No agent may access your main projects, home files, credentials or network services.

Your final review record contains source, commit SHA/diff, original and full test logs, your own case, accepted/rejected suggestion, PR body and a short reflection. A remote practice repository/PR is used only when CSG supplies its learner-safe URL and authorized access. Otherwise submit the exact local Git diff, SHA and PR draft in Learn under the approved saved-output route. No URL in this material claims that a public repository already exists.
