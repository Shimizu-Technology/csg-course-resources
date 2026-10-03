# JavaScript Fundamentals

Learner preparation guide. Use the matching course in CSG Learn for recordings, submissions and questions. Recordings and admissions are pending; these files alone do not grant access. All practice data is fictional.

## Orientation and first run

Required

# JavaScript Fundamentals

No prior programming is required. Use the supplied JavaScript runner; change values in code and inspect console output. This course teaches programming logic. Frontend with JavaScript is the later interactive HTML/CSS/DOM course.

Work through three weeks: nine teaching lessons, twelve exercises, two checkpoints and one independent project. Plan roughly 3–5 hours of practice per week, with time to revise. All examples are fictional. Use your own harmless practice data; keep private records and credentials out of submissions. A paid coding agent is not required.

Predict before running, change one thing, compare expected with actual output, then explain the result. Worked examples use separate data; integrate the assessed starter yourself. Save exact source and output in the corresponding exercise. An accessible project/repository link may accompany the saved source. For help, include the smallest failing code, expected result and actual error.

First task: run a greeting (or preview the three frontend starter files), change one word and run again. Submit source and output or a preview screenshot. Done when you can reopen it and reproduce the result.

## Lesson 1: run repair

Required

# Lesson 1 — run repair

Console dot log displays a value; parentheses hold what to display, and a semicolon finishes this statement. Numbers add; quoted digits join as text. Predict the first two lines, then run. Const creates the name before we use it. Delete the closing parenthesis on the first line and run: the parser gives a SyntaxError. Restore it. Remove the studentName declaration: now its use gives a ReferenceError. Restore that line and rerun. Keep the actual error text from your environment. Two arguments separated by a comma, as in console.log("A", "B"), are displayed together; their separator can vary by console, so record what you observe. A slash-slash comment is for a reader and does not run. Complete E1 and E2 with predictions, errors, repairs and explanations.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```javascript
console.log(4 + 2);
console.log("4" + "2");
const studentName = "Kai";
console.log(studentName);
```

Expected restored output:

```text
6
42
Kai
```

## E1: Practice after Lesson 1

Required

## E1

Predict and then run `console.log(4 + 2);`, `console.log("4" + "2");`, and `console.log("A", "B");`. Submit predictions, actual outputs, and one sentence on number versus text.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## E2: Practice after Lesson 1

Required

## E2

Repair each separately: `console.log("Hello";` and `console.log(studentName);`. Define a sample name before the second log. Submit old error text, fixed code, and output.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 2: values

Required

# Lesson 2 — values

Each const names a value that is not reassigned. Let is for a name we will update, such as a running total. This is a fictional receipt with a made-up ten-percent rate, not a Guam tax calculation. Multiply the subtotal by the rate, then add that tax. To-fixed with two formats display text; do arithmetic before formatting. Predict all three receipt lines. Run, then change first to fifteen: subtotal twenty-three, tax two-thirty, total twenty-five-thirty. Restore twelve. Number converts quoted digits before addition; without conversion the result is text one-two-three. Run Number("not a number") in a scratch line to see NaN: conversion is not a promise of valid input. E3 uses the fictional receipt and E4 fixes text addition. Paste the changed and restored runs, not merely the code.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```javascript
const first = 12;
const second = 8;
const subtotal = first + second;
const taxRate = 0.10;
const tax = subtotal * taxRate;
console.log("Subtotal: $" + subtotal.toFixed(2));
console.log("Tax: $" + tax.toFixed(2));
console.log("Total: $" + (subtotal + tax).toFixed(2));
console.log(Number("12") + Number("3"));
```

Expected restored output:

```text
Subtotal: $20.00
Tax: $2.00
Total: $22.00
15
```

## E3: Practice after Lesson 2

Required

## E3

Start with `const first = 12; const second = 8; const taxRate = 0.10;`. Print `Subtotal: $20.00`, `Tax: $2.00`, and `Total: $22.00`. Change first to 15 and record the changed result, then restore 12.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## E4: Practice after Lesson 2

Required

## E4

Fix `const first = "12"; const second = "3"; console.log(first + second);` so it prints `15`. Explain why the original prints `123`.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 3: branches

Required

# Lesson 3 — branches

The comparison produces a boolean. If chooses its block when true; else-if tries the next condition only when the first did not match. Three equals signs compare without converting types. One equals sign assigns and is the wrong tool here. Run seventy-five, then change only amount to one hundred, then one hundred twenty-five: Under, On, Over. At exactly one hundred, replace less-than with less-than-or-equal. The first branch now wrongly says Under and hides the equality branch. Restore less-than and retest all three. Braces group statements in each branch. This is a program run with changed constants, not a browser form. Complete E5, E6, and Checkpoint 1 with the three inputs and an explanation of why the first matching branch matters.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```javascript
const amount = 75;
const budget = 100;
if (amount < budget) {
  console.log("Under budget");
} else if (amount === budget) {
  console.log("On budget");
} else {
  console.log("Over budget");
}
```

Expected restored output:

```text
Under budget
```

## E5: Practice after Lesson 3

Required

## E5

Write a program that prints exactly `Under budget`, `On budget`, or `Over budget` for 75, 100, and 125 against 100. Submit code and a three-row input/output table.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## E6: Practice after Lesson 3

Required

## E6

Debug `if (amount <= budget) console.log("Under budget"); else if (amount === budget) console.log("On budget"); else console.log("Over budget");` with `amount = 100`. Submit failing output, one-line correction, and corrected output.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Checkpoint 1

Required

Submit one clean decision program, the three cases, and two sentences explaining the equality bug.

## Lesson 4: loops

Required

# Lesson 4 — loops

Square brackets hold ordered values. For-of gives price each value once. Total and count are let variables because each pass updates them. Plus-equals adds to the previous value. Predict twelve, twenty, thirty-five, forty before Run. Twelve and fifteen exceed ten, so the count is two. Insert total = 0 just inside the loop, keeping its outside declaration. Run again: the final total is five because every pass erases earlier additions. Remove only the inside reset. Declaring let total only inside the loop would instead make it unavailable afterward: that is a different scope error. Replace prices with an empty array: zero visits leave total and count at zero. Restore the state. E7 adds and counts; E8 now supplies this exact reset bug for you to repair and trace.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```javascript
const prices = [12, 8, 15, 5];
let total = 0;
let overTen = 0;
for (const price of prices) {
  total += price;
  if (price > 10) overTen += 1;
  console.log("Running: " + total);
}
console.log("Total: " + total);
console.log("Over 10: " + overTen);
```

Expected restored output:

```text
Running: 12
Running: 20
Running: 35
Running: 40
Total: 40
Over 10: 2
```

## E7: Practice after Lesson 4

Required

## E7

Print `Total: 40` and `Over 10: 2` for `[12, 8, 15, 5]`. Check an empty array returns two zeros. A price equal to 10 is not over 10.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## E8: Practice after Lesson 4

Required

## E8

Repair the reset bug: `const prices = [12, 8, 15, 5]; let total = 0; for (const price of prices) { total = 0; total += price; } console.log(total);` (prints 5). Keep the outer declaration; remove only the inner reset. Submit a four-row running-total trace and corrected code.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 5: objects

Required

# Lesson 5 — objects

These fictional trip durations are practice data, not travel estimates. An object groups named fields; a dot reads a known field. The array groups three objects. Totals begins as an empty object. Brackets let the current area value choose the key. Question-question supplies zero only when the existing value is null or undefined; this starts a missing group without discarding a valid zero. The first Hagatna creates twelve; the last adds eight. Predict the grouped object, then run. JSON.stringify turns the object into text with stable visible punctuation instead of relying on a console-specific object view. Change one area to Tamuning and predict the new group. Restore the data. E9 and E10 use the separate expense records. Print records from their fields and group by category without rewriting the originals.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```javascript
const trips = [{ area: "Hagatna", minutes: 12 }, { area: "Dededo", minutes: 18 }, { area: "Hagatna", minutes: 8 }];
const totals = {};
for (const trip of trips) {
  const area = trip.area;
  totals[area] = (totals[area] ?? 0) + trip.minutes;
}
console.log(JSON.stringify(totals));
```

Expected restored output:

```text
{"Hagatna":20,"Dededo":18}
```

## E9: Practice after Lesson 5

Required

## E9

With the first three records, print `Groceries: 42`, `Bus: 18`, and `Lunch: 13`. Submit code and output.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## E10: Practice after Lesson 5

Required

## E10

Starting with all six records, build an object of totals by category using `(totals[category] ?? 0) + amount`. Submit code and the three totals; do not edit original records.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 6: functions

Required

# Lesson 6 — functions

Function declares reusable work, and its parameters are inputs from each call. A new total starts on every call. Only matching records add minutes. Return passes the number back to the caller; console.log outside decides how to display it. Predict a match, an absent area, and an empty list. Run all three. Temporarily replace return total with console.log(total): the inside print appears, but the caller then prints undefined. Restore return and rerun. E11 uses the same pattern for totalForCategory, including Health returning zero. E12 repairs print-versus-return. Carry your category function into the final starter: it now has an explicit TODO and tests. Checkpoint 2 combines reusable totals, categories, and an absent or empty case, not a copied sample constant.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```javascript
function totalForArea(trips, area) {
  let total = 0;
  for (const trip of trips) {
    if (trip.area === area) total += trip.minutes;
  }
  return total;
}
const trips = [{ area: "Hagatna", minutes: 12 }, { area: "Dededo", minutes: 18 }];
console.log(totalForArea(trips, "Hagatna"));
console.log(totalForArea(trips, "Yigo"));
console.log(totalForArea([], "Hagatna"));
```

Expected restored output:

```text
12
0
0
```

## E11: Practice after Lesson 6

Required

## E11

Write `totalForCategory(expenses, category)` and test `Food` → 61 and `Health` → 0 on the six records.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## E12: Practice after Lesson 6

Required

## E12

Repair `function add(a, b) { console.log(a + b); } const result = add(2, 3); console.log(result);` so the caller receives 5 rather than `undefined`. Explain print versus return.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Checkpoint 2

Required

Submit a summary using at least one function, overall 118 and the three category totals, plus either an empty-list or missing-category test.

## Lesson 7: plan

Required

# Lesson 7 — plan

This file records expected results; hard-coded messages are not an implementation. Calculate the six supplied expenses by hand. The independent starter has six blank functions: total, categories, category query, largest, budget, and formatted report. Name what each accepts and returns. Empty data has no largest object; an absent category returns zero; equality says On budget. We will teach maximum selection and formatting on different fictional readings in the next lesson so your integrated expense report remains your work. Pause and write your own plan before typing the project. This course changes records in code and logs a report. It does not attach event listeners or build forms; Frontend with JavaScript teaches that next. Submit the plan, function contracts, and four expected tests.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```javascript
console.log("Total 118; Food 61; Transport 48; Supplies 9");
console.log("Largest Groceries 42; budget 120: Under by 2");
console.log("Empty: total 0; largest none");
console.log("Budget 118: On budget; Health: 0");
```

Expected restored output:

```text
Total 118; Food 61; Transport 48; Supplies 9
Largest Groceries 42; budget 120: Under by 2
Empty: total 0; largest none
Budget 118: On budget; Health: 0
```

## Lesson 8: max format

Required

# Lesson 8 — max format

These fictional readings are not a forecast. First handle empty data so index zero is never read when missing. Null is our explicit no-result value. Start the candidate from the first actual record, not zero; each later record replaces it only when strictly greater. Equal values keep the first. Return the original object so its area and number stay together. The report calls that function, builds an array of output lines, appends the appropriate message with push, and joins them with newline text. Predict both outputs and run. Try two tied readings and check the first wins. Restore the file. For category formatting, Object.keys returns names; sort orders those names; a for-of loop can append each total. Apply this technique with your previous budget branches to the expense report. Test every function before integration. The full expense reference stays hidden until your independent submission.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```javascript
function largestReading(readings) {
  if (readings.length === 0) return null;
  let largest = readings[0];
  for (const reading of readings) {
    if (reading.degrees > largest.degrees) largest = reading;
  }
  return largest;
}
function readingReport(readings) {
  const largest = largestReading(readings);
  const lines = ["Readings: " + readings.length];
  if (largest === null) lines.push("Largest: none");
  else lines.push("Largest: " + largest.area + " (" + largest.degrees + ")");
  return lines.join("\n");
}
console.log(readingReport([{ area: "Hagatna", degrees: 27 }, { area: "Yigo", degrees: 29 }, { area: "Dededo", degrees: 28 }]));
console.log(readingReport([]));
```

Expected restored output:

```text
Readings: 3
Largest: Yigo (29)
Readings: 0
Largest: none
```

## Independent final project

Required



### Lesson 7 — plan before building

Use the six supplied fictional expenses and `BUDGET = 120`. Expected: total 118; Food 61, Transport 48, Supplies 9; largest Groceries 42; under by 2. **Submit:** a five-step plan for total, categories, largest, budget, and report; names of two functions; expected empty-array and exact-budget results. Empty data has no largest item. With budget 118, status is on budget. **Done when:** another student could implement from your plan.

### Lesson 8 — implement and test

Copy `starter/tracker-starter.js`. Complete the six TODO functions. Use the output above as your first check. Test **four cases**: six supplied records with budget 120; `[]`; `totalForCategory(EXPENSES, "Health")` → 0; and six records with budget 118. Submit code pasted into Learn plus exact results. If a test fails, note expected, observed, and one fix. Do not submit `tracker-reference.js`; that is a staff key. **Done when:** normal and edge cases work.

### Lesson 9 — share and revise

Paste the final code and four results into Learn. You may include a Hafa or GitHub link as an additional way to explore it. Describe what the program expects, one bug you found or choice you improved, and what you would add next. Re-run the normal case after your change. **Final project:** the tracker and explanation are the Week 3 checkpoint. Use the 10-point rubric in the project rubric below for self-check.  **Done when:** another person can run your exact submitted copy and understand its output.



## Independent work

Use the unfinished starter. Explain your integration and one failed-then-repaired case. The assessed reference is released only after submission.

## Rubric (10 points)

Normal sample and category totals4;empty list and exact-budget3;clear functions2;explanation and evidence-based revision1.
### tracker-starter.js

```javascript
// JavaScript Fundamentals final project. Change the sample data only after your first run.
const EXPENSES = [
  { name: "Groceries", category: "Food", amount: 42 },
  { name: "Bus", category: "Transport", amount: 18 },
  { name: "Lunch", category: "Food", amount: 13 },
  { name: "Notebook", category: "Supplies", amount: 9 },
  { name: "Fuel", category: "Transport", amount: 30 },
  { name: "Snack", category: "Food", amount: 6 },
];
const BUDGET = 120;

function totalAmount(expenses) {
  // TODO: return the sum. Empty list => 0.
}

function totalsByCategory(expenses) {
  // TODO: return an object, for example { Food: 61 }.
}

function totalForCategory(expenses, category) {
  // TODO: sum only matching categories; absent category => 0.
}

function largestExpense(expenses) {
  // TODO: return an expense object, or null for an empty list.
}

function budgetStatus(total, budget) {
  // TODO: return "Under by N", "On budget", or "Over by N".
}

function makeReport(expenses, budget) {
  // TODO: return a readable string with total, categories, largest, and status.
}

console.log(makeReport(EXPENSES, BUDGET));
```


### Independent project review

Use the published point weights. Individual scoring applies only when included in the learner’s enrollment. Self-paced learners can use these criteria for self-review.

- **Normal report (4 points):** Correctly total all expenses, group categories, find the largest expense and present a readable report on changed data.
- **Empty and boundary cases (3 points):** Handle empty input, an absent category and budget boundaries.
- **Functions (2 points):** Use readable reusable functions rather than sample-specific constants.
- **Explanation and revision (1 point):** Explain a decision and make a focused revision. Guided pass requires 8/10 and a correct normal report.

## Lesson 9: revise

Required

# Lesson 9 — revise

A guard handles the exceptional case before normal field access. Remove the guard and run empty data: reading name from an absent record throws an error. Restore it and rerun both cases; a fix must preserve the case that already worked. Your final checks are the six expenses at budget one hundred twenty, an empty list, Health returning zero, and the six expenses at budget one hundred eighteen. Run your own exact submitted copy. Include code, observed results, and one revision with its reason. If you attach a Hafa share, also paste code because a share may import a copy. Self-check with the rubric; personal grading depends on your actual edition. Do not infer financial accuracy from this whole-dollar fictional exercise. The optional monthly extension comes afterward and does not affect the required score.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```javascript
function firstName(records) {
  if (records.length === 0) return "none";
  return records[0].name;
}
console.log(firstName([{ name: "Practice" }]));
console.log(firstName([]));
```

Expected restored output:

```text
Practice
none
```

## Optional review after independent submission

Optional



The required project and rubric above are completed and explained without an agent. After that submission, offer the optional agent-assisted extension. The learner can use Codex desktop, another coding agent they already have, or the saved code and tests without an AI account. They inspect the proposed change and rerun the original project before accepting it. No AI subscription or optional-extension score is required to pass.

**Expected checks:** Original 118; December 118, January 60; two invalid records skipped; zero amount valid. Write tests in your own project for the original behavior and the changed-data/edge cases listed above. Staff assessment tests are not a learner dependency. Ask for a prompt or change request, one accepted or rejected line with a reason, the original and extended outputs, and one edge-case test.  Follow the optional recorded example in this lesson after submitting your independent project.


This is optional and does not affect required completion. You may use an agent you already have or review the saved change without an account. Request instructor release of the review fixture after the independent project.
