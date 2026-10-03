# Ruby Fundamentals

Learner preparation guide. Use the matching course in CSG Learn for recordings, submissions and questions. Recordings and admissions are pending; these files alone do not grant access. All practice data is fictional.

## Orientation and first run

Required

# Ruby Fundamentals

No prior coding is required. Use the supplied Ruby workspace or a local Ruby 3.3+ terminal. The local environment and GitHub companions are optional if you use the browser route.

Work through three weeks: nine teaching lessons, twelve exercises, two checkpoints and one independent project. Plan roughly 3–5 hours of practice per week, with time to revise. All examples are fictional. Use your own harmless practice data; keep private records and credentials out of submissions. A paid coding agent is not required.

Predict before running, change one thing, compare expected with actual output, then explain the result. Worked examples use separate data; integrate the assessed starter yourself. Save exact source and output in the corresponding exercise. An accessible project/repository link may accompany the saved source. For help, include the smallest failing code, expected result and actual error.

First task: run a greeting (or preview the three frontend starter files), change one word and run again. Submit source and output or a preview screenshot. Done when you can reopen it and reproduce the result.

## Lesson 1: run predict

Required

# Lesson 1 — run predict

Multiplication runs before addition. Quotation marks make text, so the second plus joins two characters instead of adding two numbers. The dot calls upcase on the text hi. Predict each line on paper now; pause before Run. Read the three lines from top to bottom after running. Next replace the entire file with puts greeting. The name is missing, so Ruby raises NameError. Restore this file and put greeting = "Håfa adai" above puts greeting in a separate scratch file. The assignment creates the name before its use. A missing closing quote instead prevents Ruby from parsing the program: that is a SyntaxError. Fix the quote and run again. Copy the actual error from your runner; its surrounding text may differ. Do R1 and R2 with your own predictions and both repairs.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```ruby
puts 2 + 3 * 4
puts "2" + "3"
puts "hi".upcase
```

Expected restored output:

```text
14
23
HI
```

## R1: Practice after Lesson 1

Required

## R1

Predict `puts 2 + 3 * 4`, `puts "2" + "3"`, and `puts "hi".upcase`; run and explain one result.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## R2: Practice after Lesson 1

Required

## R2

Fix `puts greeting` by defining `greeting`; then repair a missing closing quote. Submit both fixes and the error names.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 2: values

Required

# Lesson 2 — values

The equals sign assigns a value to a name. Topic holds a string, minutes an integer. Inside double quotes, hash followed by braces inserts the current value. The colon and the word minutes remain ordinary text. Predict the first line of output, then run. In the second expression to_i converts the digit string before ten is added. Replace that expression with "15" + 10, run, and read the TypeError: Ruby cannot join an integer to text. Restore the file. The last line is deliberate: invalid numeric text becomes zero with to_i. Conversion is not validation, so later we will check input before trusting it. True and false are boolean values: run puts minutes >= 25 to see true, then try 26. Re-run the restored state. Complete R3 and R4 and explain the difference between a value and its display.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```ruby
topic = "Ruby"
minutes = 25
puts "#{topic}: #{minutes} minutes"
puts "15".to_i + 10
puts "not a number".to_i
```

Expected restored output:

```text
Ruby: 25 minutes
25
0
```

## R3: Practice after Lesson 2

Required

## R3

Set `topic = "Ruby"`, `minutes = 25`; print `Ruby: 25 minutes` with interpolation.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## R4: Practice after Lesson 2

Required

## R4

Convert `"15"` with `.to_i`, add 10, and explain why `"15" + 10` fails.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 3: choices

Required

# Lesson 3 — choices

Less-than compares two numbers and produces true or false. If runs its block only when its condition is true. Elsif gives the next condition a chance only if the first was false. Two equals signs compare values; one equals sign assigns. Else handles the remaining case, and end closes the decision. Run nine against ten, then change only minutes to ten and run, then eleven and run. The outputs must be under, on, over. Restore nine afterward. For a separate at-least-goal decision type if minutes > goal, puts "goal reached", else, puts "keep going", end on separate lines. At ten that incorrectly says keep going. Change the comparison to >= and retest nine, ten, eleven. The exact boundary exposes the bug. No loop is needed yet. Complete R5, R6, and Checkpoint A with three observed runs.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```ruby
minutes = 9
goal = 10
if minutes < goal
  puts "under"
elsif minutes == goal
  puts "on"
else
  puts "over"
end
```

Expected restored output:

```text
under
```

## R5: Practice after Lesson 3

Required

## R5

For minutes 9, 10, 11 against goal 10, print under/on/over.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## R6: Practice after Lesson 3

Required

## R6

Start with `minutes = 10; goal = 10; if minutes > goal; puts "goal reached"; else; puts "keep going"; end`. The intended rule is at least the goal. Repair the comparison; show 9, 10 and 11 before/after and name the input that exposes the bug.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Checkpoint 1

Required

Without notes, write a two-input goal classifier using a method-free Ruby snippet, then test below, equal and above. Submit code, three outputs, and a two-sentence explanation of the equal case. Passing evidence: all three branches, numeric conversion where needed, and an explanation tied to the actual comparison. Retry after feedback before Week 2.

## Lesson 4: loops

Required

# Lesson 4 — loops

Square brackets hold an ordered array. Each visits one value at a time, and the bars name that current value minutes. Total starts outside the block so later code can use it. Plus-equals means add to the existing value. The counter adds one only when the value is strictly greater than twenty. Predict the three running totals before Run. Now insert a second total = 0 immediately inside the block. Keep the original outer declaration. Every pass discards earlier work, so the final total becomes thirty-five. Remove only that inner reset and retest. If you move the sole declaration into the block, puts total outside raises NameError instead; that is a different scope bug. Finally replace the array with an empty array: total and counter stay zero. Restore the original array and complete R7 and R8.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```ruby
total = 0
over_twenty = 0
[25, 20, 35].each do |minutes|
  total += minutes
  over_twenty += 1 if minutes > 20
  puts "Running: #{total}"
end
puts "Total: #{total}"
puts "Over 20: #{over_twenty}"
```

Expected restored output:

```text
Running: 25
Running: 45
Running: 80
Total: 80
Over 20: 2
```

## R7: Practice after Lesson 4

Required

## R7

Sum `[25, 20, 35]` to 80 and count items over 20.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## R8: Practice after Lesson 4

Required

## R8

Repair `total = 0; [25, 20, 35].each do |minutes|; total = 0; total += minutes; end; puts total`. Keep the outer declaration and remove only the inner reset. Submit before/after output and the three running totals.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 5: records

Required

# Lesson 5 — records

This is fictional break-planning data, not health advice. Curly braces group fields into a hash. Activity-colon writes a symbol key; rest[:activity] retrieves that field. The array holds three hashes. Hash.new with zero gives an unseen activity a starting value of zero. On the first Water record zero plus five becomes five; the next Water adds four to that same entry. Predict Water and Walk by hand, then run. P displays a data structure for inspection. The final line uses index zero to select the first array record, then reads its activity. Change Water to Shade on the final record and predict the extra group before running. Restore it. R9 and R10 use study sessions rather than breaks: apply the same lookup and accumulation to topic and minutes. Explain where each total starts.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```ruby
breaks = [{ activity: "Water", minutes: 5 }, { activity: "Walk", minutes: 8 }, { activity: "Water", minutes: 4 }]
totals = Hash.new(0)
breaks.each do |rest|
  totals[rest[:activity]] += rest[:minutes]
end
p totals
puts "First: #{breaks[0][:activity]}"
```

Expected restored output:

```text
{"Water"=>9, "Walk"=>8}
First: Water
```

## R9: Practice after Lesson 5

Required

## R9

Print `Ruby: 25` from `{ topic: "Ruby", minutes: 25 }`.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## R10: Practice after Lesson 5

Required

## R10

Use `sessions = [{topic: "Ruby", minutes: 25}, {topic: "SQL", minutes: 20}, {topic: "Ruby", minutes: 15}]`. Calculate totals in a hash and explain the default zero.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Lesson 6: methods

Required

# Lesson 6 — methods

Def starts a named method; the name in parentheses is its input. End closes the method. A fresh local total starts at zero on every call. The final expression is the return value. Here we return a number so the caller can choose how to print or compare it. Run all three calls. Now replace the final total line inside the method with puts total. The method prints the number but returns nil. Add p break_total([]) to make the returned nil visible. Restore the returning version and rerun. We can replace the loop with breaks.sum { |rest| rest[:minutes] }; sum adds the values produced by the block and returns zero for no records. Both implementations are acceptable. R11 uses sessions and R12 repairs a print-versus-return error. Checkpoint B combines a reusable total with your three-way goal method; test zero, equal, and over.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```ruby
def break_total(breaks)
  total = 0
  breaks.each { |rest| total += rest[:minutes] }
  total
end
puts break_total([{ minutes: 5 }, { minutes: 8 }])
puts break_total([])
puts break_total([{ minutes: 0 }])
```

Expected restored output:

```text
13
0
0
```

## R11: Practice after Lesson 6

Required

## R11

Write `total_minutes(sessions)` and test `[{topic: "Ruby", minutes: 25}, {topic: "SQL", minutes: 20}]` plus `[]`.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## R12: Practice after Lesson 6

Required

## R12

Repair `def add_minutes(a, b); puts a + b; end; p add_minutes(25, 20)`. Show its printed output and return value before and after.

Submit exact source, expected and actual output (or observed screen behavior), and your explanation. A link may accompany the source.

## Checkpoint 2

Required

Implement `total_minutes` and `goal_status` from the starter without using the reference. Test zero, exact goal, and over goal. Submit code and the three outputs. Passing evidence: a reusable method, no hard-coded sample result, and correct exact-goal behavior.

## Lesson 7: plan

Required

# Lesson 7 — plan

These printed expectations are a plan, not the implementation. I calculate the three fictional break durations by hand. Grouping by activity produces two totals; selecting the longest chooses the eight-minute Walk. For a twenty-minute target the difference is three. An empty list must not attempt to read fields from a missing record. Pause and name the functions that could produce these results. Your assessed study report has different records and field names. Open its starter, identify all six TODOs including valid_session, and write expected results from its six sessions. The required total is one hundred thirty-five. Plan validation, total, groups, longest, goal, and formatting as separate jobs. Write the empty and exact-goal expectations before implementation. Keep the final starter unfinished here: your plan is the Lesson 7 submission.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```ruby
# Fictional break report: plan before filling the separate final project.
puts "Water 5 + Walk 8 + Water 4 = 17"
puts "Water 9; Walk 8; longest Walk 8"
puts "Target 20: short by 3"
puts "Empty list: total 0; longest none"
```

Expected restored output:

```text
Water 5 + Walk 8 + Water 4 = 17
Water 9; Walk 8; longest Walk 8
Target 20: short by 3
Empty list: total 0; longest none
```

## Lesson 8: integration

Required

# Lesson 8 — integration

The question-mark method returns a boolean. Is-a checks a type; and-and requires every check, stopping when one is false. Strip removes outside whitespace; exclamation reverses empty, so a blank activity fails. All asks whether every record passes. Raise stops invalid data with a clear error. Sum gets the total; the ordinary loop gets groups. Max-by compares the block values and returns the original longest record, or nil for an empty array. Lines is an array of output strings. Sort orders the group pairs alphabetically; the two block names unpack each pair. Double-less-than appends one line. If longest prevents a field lookup on nil. Join combines lines with a newline and returns the finished string. Run the normal and empty examples, then try a negative minute. Restore the file after the error. Adapt these mechanisms to your study report; do not copy a staff answer. Your goal method must still handle under, on, and over.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```ruby
def valid_break?(rest)
  rest.is_a?(Hash) && rest[:activity].is_a?(String) && !rest[:activity].strip.empty? && rest[:minutes].is_a?(Integer) && rest[:minutes] >= 0
end
def break_summary(breaks, target)
  raise ArgumentError, "invalid break" unless breaks.all? { |rest| valid_break?(rest) }
  total = breaks.sum { |rest| rest[:minutes] }
  groups = Hash.new(0)
  breaks.each { |rest| groups[rest[:activity]] += rest[:minutes] }
  longest = breaks.max_by { |rest| rest[:minutes] }
  lines = ["Total: #{total}"]
  groups.sort.each { |activity, minutes| lines << "#{activity}: #{minutes}" }
  if longest
    lines << "Longest: #{longest[:activity]} #{longest[:minutes]}"
  else
    lines << "Longest: none"
  end
  lines << "Difference: #{total - target}"
  lines.join("\n")
end
puts break_summary([{ activity: "Water", minutes: 5 }, { activity: "Walk", minutes: 8 }, { activity: "Water", minutes: 4 }], 20)
puts break_summary([], 20)
```

Expected restored output:

```text
Total: 17
Walk: 8
Water: 9
Longest: Walk 8
Difference: -3
Total: 0
Longest: none
Difference: -20
```

## Independent final project

Required



Start with `starter/study_report_starter.rb`. Use the six fictional sessions and goal of 120. Produce overall minutes, alphabetically displayed topic totals, the longest session or “none,” and under/on/over goal status. Required sample output:

```text
Total: 135 minutes
Git: 15 minutes
Ruby: 70 minutes
SQL: 50 minutes
Longest: Ruby (35 minutes)
Goal: over goal by 15 minutes
```

Accept an array, a nonnegative integer goal and records with nonblank string topics and nonnegative integer minutes. Reject malformed input with ArgumentError. Use singular minute when the goal difference is exactly one. Test `[]`, an exact goal, a one-minute difference, changed topics and a negative-minutes record. A clear error for invalid records earns full validation credit.  A different topic set is fine if it passes the same behaviors. This is an introductory programming exercise, not a study-performance assessment.



## Independent work

Use the unfinished starter. Explain your integration and one failed-then-repaired case. The assessed reference is released only after submission.



| Item | Points |
|---|---:|
| Correct overall total and empty total | 2 |
| Correct per-topic totals for changed data | 2 |
| Longest session and empty case | 2 |
| Under/on/over goal boundary | 2 |
| Clear method names, sample run, and explanation | 1 |
| Negative minutes rejected or clearly flagged | 1 |

Do not claim completion because only the sample output matches; alter one amount/topic when assessing. The reference in `the private reference released separately after assessment` is the staff answer, not the only acceptable implementation.


### study_report_starter.rb

```ruby
# Ruby Fundamentals final project starter
# Run: ruby study_report_starter.rb
# Replace each TODO in order. Keep the sample data so your result can be checked.

SESSIONS = [
  { topic: "Ruby", minutes: 25 },
  { topic: "SQL", minutes: 20 },
  { topic: "Ruby", minutes: 35 },
  { topic: "Git", minutes: 15 },
  { topic: "SQL", minutes: 30 },
  { topic: "Ruby", minutes: 10 }
]
GOAL = 120

def valid_session?(session)
  # TODO: require a hash, a nonblank string topic, and nonnegative integer minutes.
end

def total_minutes(sessions)
  # TODO: add every session's minutes. An empty array should return 0.
end

def totals_by_topic(sessions)
  # TODO: return a hash of topic => total minutes.
end

def longest_session(sessions)
  # TODO: return the session with the most minutes, or nil if there are none.
end

def goal_status(total, goal)
  # TODO: return "under goal by N minutes", "on goal", or "over goal by N minutes".
  # Use "minute" for a difference of exactly 1.
end

def report(sessions, goal)
  # TODO: require an array and nonnegative integer goal; reject invalid sessions
  # using valid_session?, then combine results.
  # Raise ArgumentError for bad input; return a string, not printed output.
end

puts report(SESSIONS, GOAL)
```


### Independent project review

Use the published point weights. Individual scoring applies only when included in the learner’s enrollment. Self-paced learners can use these criteria for self-review.

- **Total (2 points):** Compute the overall total and return zero for empty input.
- **Topic totals (2 points):** Compute per-topic totals for changed data.
- **Longest session (2 points):** Find the longest session and handle an empty collection.
- **Goal decisions (2 points):** Distinguish under, equal and over goal.
- **Explanation (1 point):** Use clear method names, show a sample run and explain the flow.
- **Invalid minutes (1 point):** Reject or clearly flag negative minutes.

## Lesson 9: test present

Required

# Lesson 9 — test present

Each assertion states a behavior. Raise unless means fail when the expected condition is false. Raise if means fail when an unwanted condition is true. The last puts appears only after all checks passed. Run, then change <= to <. The equal check now stops with equal failed. Restore <= and rerun. That is evidence that the check catches a specific defect. Apply the same discipline to your own report: normal sample, empty list, exact goal, negative minutes, and one altered topic or duration. Call your submitted file, not the staff reference. Explain the input, the six jobs, and one bug with its failing and repaired result. Use the rubric to review; submit exact code and observed output. Staff will change data when assessing so a hard-coded sample does not count. The optional agent extension appears only after this independently built project is submitted and explained.

Pause before each run and predict the output. Save changed and restored results. Use a fresh worked-example state, then apply the mechanism to your own exercise.

```ruby
def within_target?(minutes, target)
  minutes <= target
end
raise "below failed" unless within_target?(9, 10)
raise "equal failed" unless within_target?(10, 10)
raise "above failed" if within_target?(11, 10)
puts "3 boundary checks passed"
```

Expected restored output:

```text
3 boundary checks passed
```

## Optional review after independent submission

Optional



The required project and rubric above are completed and explained without an agent. After that submission, offer the optional agent-assisted extension. The learner can use Codex desktop, another coding agent they already have, or the saved code and tests without an AI account. They inspect the proposed change and rerun the original project before accepting it. No AI subscription or optional-extension score is required to pass.

**Expected checks:** Original 135 minutes; week 49 is 135, week 50 is 55; two invalid sessions skipped; zero minutes valid. Write tests in your own project for the original behavior and the changed-data/edge cases listed above. Staff assessment tests are not a learner dependency. Ask for a prompt or change request, one accepted or rejected line with a reason, the original and extended outputs, and one edge-case test.  Follow the optional recorded example in this lesson after submitting your independent project.



This is optional and does not affect required completion. You may use an agent you already have or review the saved change without an account. Request instructor release of the review fixture after the independent project.
