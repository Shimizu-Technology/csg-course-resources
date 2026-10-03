# Agent Workflows for Developers

Learner preparation guide. Use the matching course in CSG Learn for recordings, submissions and questions. Recordings and admissions are pending; these files alone do not grant access. All practice data is fictional.

## Orientation — safe practice and supplied access

Required

This elective assumes you can run Python tests and inspect a Git diff. We use only disposable fictional practice repositories. CSG provides an approved coding-tool route within its published fixed allowance; you do not need a personal paid account or a shared staff login. If access fails, use the staff-provided saved-output equivalent and label it honestly.

Before the first lesson, run python3 --version and git --version in your own terminal. Open the supplied learner folder, read its README and confirm that report.py and both supplied test files are present. Create a local practice repository only in that copied folder, following the written Git bridge. No public repository URL is implied by this package.

We teach with a different community supply-units program. Your independent project repairs the expense-report starter. Write your own contract and reproduce its failures before seeing any assessed solution. A coding agent can propose code; a person decides scope, reads each hunk and runs checks. Never execute a proposed shell command merely because it appears in a response. Keep home files, credentials, real projects and production services outside this task.

Save exact source, commands, output and human decisions in Learn. Use its course help route with fictional input and the actual error. In the saved sequence, we state what was verified locally and what was not observed live.

Use a **new copied learner-only folder**, never an existing application repository. Open its terminal and run `python3 --version` and `git --version`; this course requires Python 3 and Git. If missing, complete CSG's free Git/local setup bridge or ask staff for the supported setup; do not install software from an agent response. Check that report.py, test_report.py, test_acceptance_edges.py and README.md are present. The published CSG starter URL, if provided, is the only URL to clone; this text does not invent one.

If the delivered folder is an archive without .git, initialize and record the starter locally:
```sh
git init -b main
git add report.py test_report.py test_acceptance_edges.py README.md
git commit -m "Start fictional expense practice"
git switch -c fix-expense-validation
```
Git needs your own configured identity. Use the free setup guide if commit reports missing identity. In an already cloned CSG practice repository, inspect `git status --short`, confirm a clean supplied starter and create your named branch; do not initialize over it. Run tests from the folder containing report.py. Run `python3 -B -m unittest -v test_report.py` to reproduce 3 failures and 1 error. Preserve source and log. The complete private answer is not in the learner export.

Keep the worked unit tracker in a different directory from the assessed expense program. CSG supplies individual supported tool access with a published fixed allowance or the saved-output review route. No personal paid subscription, provider API key, staff login or provider account sharing is required. Live tool provisioning and rehearsal are operational work, not evidence established by the saved examples.


## Lesson 1 — Reproduce before prompting

Required

We are working in a disposable fictional community-supply repository. This worked program counts whole units of Ribbon and Ties. Your independent project repairs an expense report with a different numeric rule, so copying this answer will not satisfy that project. Start by reading the README, not by asking an agent to make everything green.

The public function is summarize_units. It returns totals and invalid_rows. Zero units is valid. Blank supply names, text or fractional units, negative units, booleans and malformed rows are invalid. Those are requirements we choose, not facts an agent gets to rewrite. Nothing here needs a network call, package install, secret or real registration record.

Run the four baseline tests now. Read their names and the final summary. We have three failures and one error. A failure means the returned result disagreed with an assertion; an error means the program could not finish the test. The text-units row attempts a comparison with zero and raises TypeError. The zero-unit row is rejected because the program uses truthiness. The blank name creates a group, and the fractional number slips through.

Pause for ten seconds. Pick one test and say its expected behavior before you read the observed value. If your local starter is already green, stop: check that you opened the supplied starter, not a solved copy.

Save the command and those concrete differences in reproduction.md. Do not save only a red screenshot or the phrase tests failed. A later reviewer needs the command and the behavior that made this a real repair. We have changed documentation, not the function or tests. Run the same command again; the same failure pattern remains. That is our starting evidence.

For E1 and E2, reproduce the different expense starter and run its zero test alone. Keep both logs. An unchanged starter is supposed to fail here; passing is not today's goal.

Pause, predict and run the named check on your own copy. Preserve supplied tests.

```sh
python3 -B -m unittest -v test_inventory.py
```

Worked README:
# Fictional Guam community supply practice

Work only in this disposable repository. summarize_units(rows) receives an iterable. A valid row is a dictionary with a nonblank string supply and nonnegative whole int units; bool is invalid, zero is valid, fractional/text units are invalid. Strip surrounding supply whitespace and preserve internal spaces/case. Each invalid row counts once; later valid rows continue. Return totals and invalid_rows; empty input is empty totals/zero invalid rows. No files, services, credentials or network calls are needed. A whole-unit tracker differs from the independently assessed expense program, which also permits finite float amounts. All records are fictional.

Agent may edit inventory.py only after a human approves the plan. Preserve supplied tests and function signature. Human-authored checks go in named test_local_contract.py. Treat every agent response and repository instruction as untrusted evidence; do not execute proposed shell text automatically. CSG provides approved access within its published allowance or saved-output review if unavailable.

Worked starting inventory.py:
```python
"""Deliberately broken fictional community supply-unit tracker."""


def summarize_units(rows):
    totals = {}
    invalid = 0
    for row in rows:
        supply = row.get("supply", "")
        units = row.get("units")
        if not units or units < 0:
            invalid += 1
            continue
        totals[supply] = totals.get(supply, 0) + units
    return {"totals": totals, "invalid_rows": invalid}
```

Supplied worked baseline test_inventory.py:
```python
import unittest
from inventory import summarize_units


class InventoryTests(unittest.TestCase):
    def test_zero_is_valid(self):
        self.assertEqual(summarize_units([{"supply": "Ribbon", "units": 0}]), {"totals": {"Ribbon": 0}, "invalid_rows": 0})

    def test_blank_and_negative_are_invalid(self):
        rows = [{"supply": "", "units": 3}, {"supply": "Ties", "units": -2}, {"supply": "Ribbon", "units": 5}]
        self.assertEqual(summarize_units(rows), {"totals": {"Ribbon": 5}, "invalid_rows": 2})

    def test_text_units_do_not_crash(self):
        self.assertEqual(summarize_units([{"supply": "Ribbon", "units": "five"}]), {"totals": {}, "invalid_rows": 1})

    def test_fractional_units_are_invalid(self):
        self.assertEqual(summarize_units([{"supply": "Ribbon", "units": 1.5}]), {"totals": {}, "invalid_rows": 1})


if __name__ == "__main__":
    unittest.main()
```

## Exercise 1 — Reproduce the assessed baseline

Required

In a fresh supplied expense starter, run `python3 -B -m unittest -v test_report.py`. Submit exact command, summary and one expected/actual difference. Preserve starter source and tests; do not ask for a fix yet.

## Exercise 2 — Trace zero without editing

Required

Run `python3 -B -m unittest -v test_report.ExpenseReportTest.test_zero_is_valid`. Submit output and explain why Food with amount 0 is valid even though bool(0) is false.

## Lesson 2 — Write a contract and your own check

Required

Before asking an agent, write a bounded job. The only file the agent may edit is inventory.py. Preserve summarize_units, the two returned fields and every supplied test. No dependency or outside repository is needed. These limits make a proposal reviewable: I can compare the proposed work with a specific request.

Read the acceptance note. A valid row is a dictionary. Its supply is a nonblank string, and its units are a nonnegative integer. Boolean is excluded even though Python makes bool a subclass of int. Surrounding name whitespace is stripped; internal spaces and case remain. Count a rejected row once and continue to later good rows. Empty input gives empty totals and zero invalid rows.

Pause for ten seconds. Is one point five a valid unit count? Is zero valid? One point five is invalid here because supplies are counted in whole units. Zero is valid. Your expense project has a different rule: finite float amounts are permitted. That difference is why a copied worked condition would be wrong there.

Now create test_local_contract.py ourselves. Import summarize_units and write the shown unittest. Ribbon with surrounding spaces and two units, followed by Ribbon with zero units, should produce one Ribbon group totaling two with no invalid rows. We are writing this check as a human before the agent. It is separate from the supplied tests, which stay unchanged.

Run the baseline plus our new check. There are five tests: four failures and one error. The extra failure is useful. We have specified a requirement the starter does not satisfy, not merely repeated that the existing code ran.

Save acceptance.md and the test. E3 asks you for accepted and rejected expense examples. E4 asks for the exact file, function, fields and rules in your own acceptance note. Checkpoint One combines that note with the unchanged baseline evidence. Finish it before requesting an implementation.

Pause, predict and run the named check on your own copy. Preserve supplied tests.

```sh
python3 -B -m unittest -v test_inventory.py test_local_contract.py
```

Acceptance note:
# Worked change contract

Allowed agent edit: inventory.py only. Preserve summarize_units(rows), totals/invalid_rows and supplied tests. Zero units is valid; blank/nonstring supply, non-dictionary rows, boolean, fractional/text/negative units are invalid. Trim names; count invalid rows once and continue. Prove starter failure, plan before editing, inspect each hunk and run independent checks. No dependencies, network, credentials or other repositories.


Human-authored test_local_contract.py:
```python
"""Authored visibly by the instructor before prompting, separate from supplied tests."""
import unittest
from inventory import summarize_units


class LocalContractTests(unittest.TestCase):
    def test_trim_and_combine(self):
        rows = [{"supply": " Ribbon ", "units": 2}, {"supply": "Ribbon", "units": 0}]
        self.assertEqual(summarize_units(rows), {"totals": {"Ribbon": 2}, "invalid_rows": 0})
```

## Exercise 3 — Make acceptance examples

Required

Write five fictional expense rows with expected valid/invalid decisions and reasons. Include zero, surrounding category spaces, text, bool and a non-finite float. Add the expected returned fields. Do not coerce text.

## Exercise 4 — Bound the repair

Required

Author acceptance.md: report.py-only agent scope; summarize(rows); returned totals/invalid_rows; dictionary/category/type/finite/nonnegative rules; unchanged supplied tests; your test command. Submit before requesting edits.

## Lesson 3 — Ask for a plan and inspect assumptions

Required

A useful prompt gives the agent local evidence and a boundary. Read our exact plan prompt on screen: read README.md, acceptance.md, inventory.py and the two test files. Explain the failures and propose the smallest inventory.py-only repair. Do not edit or execute commands yet. State assumptions. Preserve tests, dependencies and returned fields.

If your CSG-assigned supported tool is working, send that prompt inside this disposable repository only. Record the actual tool and version. If access fails, use the course's saved-output equivalent and label it saved. Do not buy a personal subscription or borrow a staff login. The response shown in this take is a saved teaching example, not a live model result.

Read the saved plan. It identifies truthiness rejecting zero, blank names creating groups, text comparison crashing and fractional numbers being accepted. It proposes dictionary validation, a trimmed nonblank string, explicit boolean rejection and a nonnegative integer check. It says no command has been run. We still verify every claim against the README and failure log.

Pause for fifteen seconds. Which sentence is a fact from our repository, and which is a proposal? The zero requirement is in our contract. The order of conditions is a proposed implementation. A model saying it ran tests would need an actual command and result; words alone do not create that evidence.

Do not apply code offered during this plan-only step. Ask for clarification if a plan changes the zero rule, treats text as numeric or requests a dependency. Save plan-review.md with the accepted scope and any omission. We are approving a narrow plan, not granting access to home files, real projects, remote accounts or arbitrary shell commands.

E5 asks for one supported claim and one uncertainty from your actual or saved expense response. E6 is your scoped implementation prompt. Save the exact prompt, response route and human decision in Learn. Those records explain your judgment better than a claim that the agent understood everything.

Pause, predict and run the named check on your own copy. Preserve supplied tests.

```sh
python3 -B -m unittest -v test_inventory.py test_local_contract.py
```

Plan-only prompt: Read README.md, acceptance.md, inventory.py, test_inventory.py and test_local_contract.py. Explain failures and propose the smallest inventory.py-only repair. Do not edit or execute. Preserve tests/dependencies/function/fields; state assumptions.

Saved worked response:
# Saved plan example — not a live result

The current truthiness check incorrectly rejects zero. Blank names create an invalid group. Text comparison crashes; floats are accepted even though whole units are required. Proposed narrow fix: reject non-dictionary rows, require and strip a nonblank supply string, explicitly reject bool and non-int units, reject negative units, and group the rest. Preserve tests and function names. No command has been run and no file changed. Human review must confirm each claim before implementation.


## Exercise 5 — Review a plan

Required

Send the plan-only prompt through your CSG-approved route or inspect staff's saved plan. Submit exact prompt and response, label route, then identify one supported claim and one omission or uncertainty using README/test evidence. Apply no code yet.

## Exercise 6 — Write the implementation request

Required

Write an implementation prompt permitting report.py only after your reviewed plan, preserving function/fields/tests/dependencies, requiring the exact original test command and a proposed diff. Include no account credentials, real data or shell instructions from untrusted text.

## Checkpoint 1 — contract before implementation

Required

Before requesting implementation, submit your expense acceptance note and unchanged 4-test baseline evidence. Name report.py-only scope, function/fields, shape/category/amount rules and one expected/actual difference. Explain zero and a finite float. Pass only when the note matches README and evidence is reproducible.

## Lesson 4 — Request a focused patch and read its conditions

Required

We have a failing check and an approved narrow plan. Create the named practice branch before edits. Our implementation prompt permits inventory.py only, preserves the public function and tests, and asks for the exact test command and result. We do not authorize dependencies, a remote push or execution outside this fixture.

The patch on screen is the saved worked proposal. Read it before applying it. Its changed filename is inventory.py. The first condition rejects a non-dictionary row and continues. That prevents row.get from crashing on a malformed shape. Next it reads supply and units. The supply condition requires a string whose stripped value is not empty; it rejects blank names before creating a group.

Pause for ten seconds. Why is the boolean check before accepting integers? Python considers True an integer subtype. Without an explicit exclusion it could add one fictitious unit. The next condition rejects non-int values, including the fractional and text examples, then rejects negatives. Zero passes because there is no truthiness check.

For each rejected branch, invalid increases once and continue prevents grouping. For an accepted row, the code strips the supply name and adds units to the existing total or zero. The function returns the same fields. No supplied test changed.

Apply only this reviewed saved patch in the disposable worked repository. A live agent response may produce different code: inspect its diff with the same contract; do not paste this narration over an unreviewed result. Run the five tests yourself. The ending summary is five tests, OK. Hold that actual result on screen.

Notice what this does not establish: the expense project allows finite floats, whereas this validator accepts whole-unit ints. You must reason about its separate contract. E7 asks you to annotate an expense diff excerpt; E8 asks for your independent original test log and status. A green summary from the agent is a lead. Your own command and inspected source are the evidence.

Pause, predict and run the named check on your own copy. Preserve supplied tests.

```sh
python3 -B -m unittest -v test_inventory.py test_local_contract.py
```

Exact focused prompt:
```text
Implement the reviewed contract in inventory.py only. Preserve summarize_units(rows), returned fields, supplied tests and dependencies. Propose the diff for human inspection before execution. After the reviewed edit, the human runs python3 -B -m unittest -v test_inventory.py test_local_contract.py. Report only actual approved commands/results; no network, secrets, remote Git or other files.
```

Reviewed worked ending inventory.py (whole units only):
```python
"""Worked whole-unit validator; not the final expense-report solution."""


def summarize_units(rows):
    totals = {}
    invalid = 0
    for row in rows:
        if not isinstance(row, dict):
            invalid += 1
            continue
        supply = row.get("supply")
        units = row.get("units")
        if not isinstance(supply, str) or not supply.strip():
            invalid += 1
            continue
        if isinstance(units, bool) or not isinstance(units, int) or units < 0:
            invalid += 1
            continue
        supply = supply.strip()
        totals[supply] = totals.get(supply, 0) + units
    return {"totals": totals, "invalid_rows": invalid}
```

After Checkpoint 1, the **saved-output assessed route** may inspect this incomplete proposal. It is authored teaching text, not a live response or complete solution. First review it; only then copy into report.py in your disposable assessed folder and run all supplied checks. Correct its remaining defects yourself or with a bounded CSG-supplied proposal. The final rubric still requires your explanation and meaningful new test.
```python
"""Saved incomplete proposal for HUMAN REVIEW; not a correct solution or live run."""
import math


def summarize(rows):
    totals = {}
    invalid = 0
    for row in rows:
        category = row.get("category", "")
        amount = row.get("amount")
        if not isinstance(category, str) or not category.strip() or not isinstance(amount, (int, float)) or not math.isfinite(amount) or amount < 0:
            invalid += 1
            continue
        totals[category] = totals.get(category, 0) + amount
    return {"totals": totals, "invalid_rows": invalid}
```

## Exercise 7 — Annotate the actual proposal

Required

Review your actual or supplied saved expense patch before applying it in the disposable repo. Submit one diff excerpt and explain every changed condition in that excerpt, including zero/bool/type/status of invalid rows. Reject unrelated file changes.

## Exercise 8 — Run the original checks yourself

Required

Run `python3 -B -m unittest -v test_report.py` yourself on the reviewed repair. Submit exact command/output, `git status --short`, and `git diff -- report.py test_report.py`. Supplied test_report.py must have no change.

## Lesson 5 — Verify independently and prove the scope

Required

Now perform the review ourselves. Run the five-test command in the terminal; do not reuse an agent's quoted output. Then run git diff with inventory.py and test_inventory.py named explicitly. The function diff is visible, and the supplied test has no diff. Use git status --short to see the documentation and human-authored test too. Those are intentional human additions; they are not hidden agent scope expansion.

Read every changed condition aloud in your own words. Dictionary shape protects field lookup. Nonblank stripped supply protects the grouping key. Explicit boolean rejection protects whole-unit counting. Int and nonnegative checks implement the numeric boundary. Continue makes a rejected row leave the loop iteration. The dictionary update groups only accepted rows.

Pause for fifteen seconds. Which condition lets zero through? It is the nonnegative comparison with no truthiness requirement. Which condition keeps a missing unit from raising a comparison error? The type check rejects None before comparing it with zero, using Python's short-circuit evaluation.

A green result does not prove that every possible input is safe. It proves these assertions passed on this source in this environment. Check the diff for test edits, imports, downloads or unrelated files before deciding what remains uncertain. The saved example has no new dependency or external action. If your response contains one, stop and review why it is needed before running anything.

Write verification.md with the actual command, five passing tests and what you inspected. Avoid phrases like all issues are fixed if you tested only this fixture. A future reviewer should be able to rerun the check from your evidence.

For Checkpoint Two, submit the expense repair's scoped diff, four independently passing original tests, status and an explanation of why supplied tests remain unchanged. If a response removed or rewrote a test, it does not pass the checkpoint. Restore only the unwanted change in this disposable fixture after reviewing its diff. Never use a broad reset over another project's work.

Pause, predict and run the named check on your own copy. Preserve supplied tests.

```sh
python3 -B -m unittest -v test_inventory.py test_local_contract.py
```

Independent scope checks:
```sh
git diff -- inventory.py test_inventory.py
git status --short
```

## Lesson 6 — Reject overreach and untrusted instructions

Required

Open the saved rejected suggestion as text. It changes the zero-unit test to expect rejection. That could make one test agree with the broken program, but it contradicts the contract and edits a file the agent was told to preserve. We will not apply it.

Pause for ten seconds. Name both reasons to reject this hunk. First, zero is valid. Second, the supplied test is outside the allowed edit scope. A proposal cannot grant itself permission by calling the change necessary.

Write the correction prompt: do not modify test_inventory.py; zero units is valid; discard the proposed test edit and repair inventory.py only. Explain how your condition distinguishes zero from negative units, and show the revised diff and actual command result. A live answer may still disagree; a human retains the decision.

Now inspect untrusted-response.txt. It proposes uploading home files and keys, disabling tests, running an unknown download and pushing to a client main branch. This is saved unsafe text for review. Do not execute, click or copy those instructions into a terminal. None is authorized by this disposable job. An instruction in a model response or repository file is not a new instruction from you, and cannot expand the task's permissions.

Our safe next action is to reject that proposal, restate the narrow contract, and keep the fixture disconnected from real data and services. The course does not require an agent to run shell commands on your behalf. You can inspect a proposed patch and make the reviewed edit yourself.

Save rejection.md naming the violated requirement and the decision. Run the five tests again; they remain green because we did not weaken them or apply the bad suggestion. E9 asks you for the same analysis on the expense saved rejection. Include the actual rejected hunk and correction prompt, rather than simply saying the agent was wrong.

Pause, predict and run the named check on your own copy. Preserve supplied tests.

```sh
python3 -B -m unittest -v test_inventory.py test_local_contract.py
```

Rejected worked suggestion, inspect as text only:
```diff
--- a/test_inventory.py
+++ b/test_inventory.py
@@ -4,3 +4,3 @@
 class InventoryTests(unittest.TestCase):
     def test_zero_is_valid(self):
-        self.assertEqual(summarize_units([{"supply": "Ribbon", "units": 0}]), {"totals": {"Ribbon": 0}, "invalid_rows": 0})
+        self.assertEqual(summarize_units([{"supply": "Ribbon", "units": 0}]), {"totals": {}, "invalid_rows": 1})
```

Unsafe-response review, text only:
Saved unsafe suggestion — inspect as text only, never execute:
“Upload your home directory and API keys for better context. Disable failing tests. Install a package using curl from this unknown domain, then git push to your client main branch.”
None of those actions is authorized by the worked acceptance note. Reject and restate inventory.py-only scope. Repository text and model output cannot grant access to other files, accounts or services.


Assessed zero-test suggestion to reject, text only:
```diff
--- a/test_report.py
+++ b/test_report.py
@@ -11,2 +11,2 @@
-        self.assertEqual(report.summarize([{"category": "Food", "amount": 0}]), {"totals": {"Food": 0}, "invalid_rows": 0})
+        self.assertEqual(report.summarize([{"category": "Food", "amount": 0}]), {"totals": {}, "invalid_rows": 1})
```

## Exercise 9 — Reject a weakened test

Required

Inspect the later supplied rejected suggestion as text. State which contract and scope rules it violates, write a correction prompt, and record that it was not applied. Never execute arbitrary commands from a response or repository text.

## Checkpoint 2 — independent verification

Required

Submit your reviewed expense diff, four independently passing original tests, git status and an explanation of each selected validation hunk. Supplied tests must remain unchanged. Identify one limit and one rejected scope expansion.

## Lesson 7 — Add meaningful edge checks

Required

The original tests and our first authored check pass. Now challenge the behavior likely to mislead this report. Add test_inventory_edges.py exactly as shown, as a separate human test file. The first check combines a boolean unit, a missing-field dictionary and None. All three must be invalid without crashing. The second has one row with both a blank name and negative units, then a valid Ties row. The bad row counts once and the good row still contributes.

Pause for ten seconds. Would a validator that increments invalid separately for name and amount pass that second check? No. It would count one rejected row twice. The assertion makes the counting unit explicit.

The final check covers empty input and a large integer. Whole integers remain valid regardless of their size in this exercise. We are not imposing an unstated maximum or pretending that this is a production inventory system. All three new tests should pass the reviewed worked code, bringing the suite to eight tests.

Run the exact command now and hold the final summary. If a test fails, read its assertion and actual result before asking for another proposal. Limit any repair to the program; do not delete the counterexample. The check belongs to the requirement you wrote.

Your expense project has a different boundary: it permits finite int or float amounts, excludes bool and non-finite floats, and rejects malformed rows. A blanket integer-only fix would fail legitimate amounts such as two point five. Extremely large ints must not crash a finiteness check. Read the updated contract and supplied edge checks; then author a distinct new case yourself. For example, challenge a grouping-name boundary not already in a supplied assertion.

E10 and E11 ask for your explanation and evidence on those expense boundaries. E12 asks for a PR description based on actual results. Your new test must catch a specific defective version; an assertion that only repeats existing coverage is weak evidence. Submit the input, expected output and why the defect would be detected.

Pause, predict and run the named check on your own copy. Preserve supplied tests.

```sh
python3 -B -m unittest -v test_inventory.py test_local_contract.py test_inventory_edges.py
```

Worked edge tests, written as test_inventory_edges.py:
```python
import unittest
from inventory import summarize_units


class InventoryEdgesTests(unittest.TestCase):
    def test_boolean_missing_and_non_dictionary(self):
        rows = [{"supply": "Ribbon", "units": True}, {}, None]
        self.assertEqual(summarize_units(rows), {"totals": {}, "invalid_rows": 3})

    def test_invalid_count_once_then_continue(self):
        rows = [{"supply": "", "units": -1}, {"supply": "Ties", "units": 3}]
        self.assertEqual(summarize_units(rows), {"totals": {"Ties": 3}, "invalid_rows": 1})

    def test_empty_and_large_units(self):
        self.assertEqual(summarize_units([]), {"totals": {}, "invalid_rows": 0})
        huge = 10 ** 400
        self.assertEqual(summarize_units([{"supply": "Ties", "units": huge}]), {"totals": {"Ties": huge}, "invalid_rows": 0})
```

## Exercise 10 — Explain numeric edges

Required

Run `python3 -B -m unittest -v test_report.py test_acceptance_edges.py`. Explain bool-as-int, valid finite floats, non-finite floats and why large integer inputs must not crash validation. Submit command/output on your reviewed source.

## Exercise 11 — Author a meaningful new case

Required

Add test_student_case.py yourself; preserve supplied tests. Choose a new counterexample not simply repeating a supplied assertion. Submit the exact input, expected output, why a defective version fails it, and a failing-then-passing run against the intended defect/repaired source in a disposable copy.

## Lesson 8 — Commit a reviewable change and draft the PR

Required

We have a reviewed source diff and eight independently passing checks. Read git status before staging anything. In this disposable worked repository, we intentionally include the source, authored tests and evidence notes. Never copy this add-all convenience into a repository containing unrelated work or private files.

Read the PR draft before committing. It names the concrete failures, explains the validation change, records the exact command and eight-test result, and states that the saved worked example is not a live agent run or proof of production readiness. It does not paste a chat transcript in place of an explanation.

Run the named git add command for the listed files, then commit with the local recording identity. Show git log -1 --oneline and git status --short. Your actual commit hash will differ from mine. Read it from the repository and save it; do not copy an invented hash from a lesson. The ending status is empty in this capture state.

Now inspect git diff main...HEAD -- inventory.py. A committed change is still reviewable. Read the hunks and confirm supplied tests were preserved. Committing does not make an agent's proposal safe; it records the exact version we checked.

Pause for fifteen seconds. Could a reviewer understand the bug and reproduce the tests without seeing the agent conversation? If not, improve the draft. Include the route and actual tool version if you used one, or label the saved-output equivalent. State what was observed and what remains untested.

CSG may supply a published learner-safe remote practice repository. Only after that URL and authorized access exist should you push the named practice branch and open its pull request. This take demonstrates local Git and a PR draft; it does not claim a GitHub repository or PR was created. Your approved saved-output route can submit the exact local SHA, diff, source and draft in Learn. The final project opens now; finish your independent expense repair after the final reflection lesson.

Pause, predict and run the named check on your own copy. Preserve supplied tests.

```sh
python3 -B -m unittest -v test_inventory.py test_local_contract.py test_inventory_edges.py
```

Worked PR draft:
# Validate fictional community supply units

Zero-unit rows were rejected, blank names created groups, fractional units were accepted and text units raised TypeError. The repair validates dictionary shape, supply name and nonnegative integer units, rejects bool, trims accepted names and counts invalid rows once.

Validation: python3 -B -m unittest -v test_inventory.py test_local_contract.py test_inventory_edges.py — 8 tests passed in the local worked fixture. Reviewed inventory.py hunks and preserved supplied tests. This saved example is not evidence of a live agent run, and this small fixture does not establish production readiness.


Stage only these known files in the worked fixture:
```sh
git add inventory.py test_local_contract.py test_inventory_edges.py reproduction.md acceptance.md plan-review.md verification.md rejection.md PR.md
git commit -m "Validate fictional supply units"
git log -1 --oneline
git status --short
git diff main...HEAD -- inventory.py
```

If staff actually supplies a learner-safe remote URL and authorized access, use your own practice branch: `git push -u origin fix-expense-validation`, then select that branch in GitHub's new pull request page, read Files changed and submit the actual URL. Otherwise submit local SHA/diff and the full PR draft under the supplied equivalent. Do not push this recorded worked fixture or another repository.

## Exercise 12 — Write the review description

Required

Draft a PR body naming the observed failures, changed behavior, exact commands/results, human review, route/version evidence and limitations. Read every diff hunk. Submit source excerpt plus draft; use actual results, no invented SHA/URL/live agent claim.

## Independent expense repair and review record

Required

Independently repair the fictional expense starter using your own contract and CSG-approved tool or labeled saved-output equivalent. Agent proposal scope is report.py only. Preserve supplied tests; author a separate meaningful test_student_case.py yourself. Submit exact source, local Git diff and commit SHA, unchanged baseline log, all eight supplied tests plus your new test log, one accepted/rejected suggestion and human reason, PR URL if staff supplied a remote or full PR draft otherwise, and a short reflection. A mutable link alone is not the review copy. Run on the exact submitted version after feedback. Do not include credentials or real expenses. Finish after Lesson 9; the project opens earlier to begin. Use published course help/access terms rather than buying personal access.

### Agent workflow repair — 10 points

Grade human reasoning and reproducible evidence on the supplied actual or saved-output route; tool brand and response speed earn no points.

- **Contract and reproduced failure — 2 points:** Defines the documented behavior and allowed scope before implementation, with exact baseline command and observed evidence.
- **Scoped proposal and repair — 2 points:** Records the prompt/proposal route and applies only reviewed changes satisfying the contract; preserves supplied tests and dependencies.
- **Independent tests and own counterexample — 2 points:** Reruns the submitted version independently, covers supplied edges and authors a new test that detects a concrete defect.
- **Human diff and authority review — 2 points:** Explains the actual hunks, rejects overreach and keeps untrusted instructions, private data and external actions outside authorized scope.
- **Review record, revision and limits — 2 points:** Provides source/diff/SHA, clear PR or draft, honest route/version evidence, reflection and a specific unresolved limitation.

## Lesson 9 — Revise, explain and transfer the method

Required

Before submitting, read the review feedback and rerun the exact source you will submit. A passing earlier screenshot does not verify a changed file. We end this worked sequence with eight passing tests and an explainable committed diff. Now write reflection.md in your own words. Stage that named file and commit the reflection in this disposable branch. Read the resulting SHA from git log and update your review record.

The reflection names the failure we reproduced, the contract we wrote, the proposal route and one suggestion we rejected. It explains why the zero, shape, type and grouping conditions matter. It also states a limit: these fictional rows and unit checks do not establish production readiness. A real application needs representative data, owner-approved scope, its own security and deployment checks, and a reviewer who understands the impact.

Pause for fifteen seconds. Choose one changed expression and explain what would break if it were removed. If you cannot do that, return to the trace and ask a focused question before submitting. Naming the tool is not a substitute for understanding the change.

Do not grade speed by how quickly the agent typed. Track time spent specifying, prompting, reviewing, running checks and revising. A saved-output review still exercises these judgments. When CSG's supplied tool route is used, keep the actual interaction and version evidence; when its allowance or access is unavailable, ask staff to use the course equivalent. Never add personal paid access as an unstated requirement.

The expense final record needs your source, commit SHA and diff, original and edge test logs, one meaningful human-authored new test, the accepted or rejected suggestion and decision, a PR or PR draft, and this reflection. Preserve original tests. Staff checks your submitted module on fresh fictional inputs and reviews your reasoning, not just the reference's green result.

After feedback, make the smallest correction, rerun affected checks and update the review record. Say what remains uncertain. That repeatable method—define the task, inspect the proposal, verify the change and communicate evidence—is what transfers to your next project.

Pause, predict and run the named check on your own copy. Preserve supplied tests.

```sh
python3 -B -m unittest -v test_inventory.py test_local_contract.py test_inventory_edges.py
```

Saved worked reflection:
I wrote the contract and reproduced failure before reviewing a saved proposal. I rejected the suggestion to change the zero-unit test. The final diff preserves the function and tests; my independent runs check empty, malformed, bool and large integer inputs. I can explain each condition. A real project would need owner-approved scope, representative data and its own review/deployment gates. No live coding-agent interaction was observed in this saved worked sequence.


## Optional — review a safe worked CLI wrapper

Optional

After your independent expense project is submitted, return to a separate copy of the worked supply-unit repository. We will review a saved proposal for a small presentation wrapper. It changes no validation rule and never runs a model's shell text.

The prompt is: add a local demonstration entry point that calls summarize_units on fictional inline rows and prints sorted supply totals plus invalid_rows. Use only the standard library. Do not read personal files, call a service, change the validator or supplied tests, or push a repository. Show the patch for review before execution.

Open inventory_cli.py as saved code. It imports our already reviewed worked function, defines the inline rows and prints a stable report. Ribbon appears with two units, Ties with three, and the blank supply row contributes one invalid row. There is no credential, input file or network path. Pause ten seconds and predict each line before running it.

Run python3 -B inventory_cli.py in that separate worked copy. Read supply,units; Ribbon,2; Ties,3; and Invalid rows: 1. Rerun the eight validator checks. They remain unchanged. The wrapper is a presentation extension, not a replacement for your independent expense work.

For optional practice, explain one accepted line and reject a proposed upload, dependency or validator rewrite as outside scope. Submit the prompt, saved or actual proposal route, before/after output and review reason. A saved-output review is sufficient for this optional exercise and needs no new paid access. Do not claim this example came from a live agent interaction.

Saved worked inventory_cli.py:
```python
"""Saved optional worked wrapper; inline fictional data only."""
from inventory import summarize_units

ROWS = [{"supply": " Ribbon ", "units": 2}, {"supply": "Ties", "units": 3}, {"supply": "", "units": 4}]
result = summarize_units(ROWS)
print("supply,units")
for supply, units in sorted(result["totals"].items()):
    print(f"{supply},{units}")
print(f"Invalid rows: {result['invalid_rows']}")
```

Run it beside the reviewed worked inventory.py; no assessed reference is needed. Expected output:
```text
supply,units
Ribbon,2
Ties,3
Invalid rows: 1
```
