# Expense-summary project checklist

Use the [starter](../starter/expense_summary.py). The complete project brief and rubric are in CSG Learn. Keep the starter's `description`, `category`, and `amount` fields even if you change the example descriptions or numbers.

## Required report

- Overall total.
- Total for each category in the input.
- Largest expense, or a clear `none` result for an empty list.
- Under, exactly on, or over budget result.

## Test before submitting

| Case | Input to try | What to check |
| --- | --- | --- |
| Provided sample | Six expenses and budget 120 | Total 118; Food 61, Transport 48, Supplies 9; largest Groceries 42; under by 2. |
| Empty list | `[]` and budget 120 | No crash; total 0; no largest expense. |
| Missing category | Ask `total_for_category` for `Health` | Result 0. |
| Exact budget | Six expenses and budget 118 | Exactly on budget, not under or over. |

Paste your final code, output for the required cases, and a short explanation into Learn. You may also add a Hafa Code or GitHub link. If you revise after feedback, submit the revised code and say what changed.

Required cases: normal records; empty records; absent Health category; budget exactly equal to the total; and a $100 budget producing $18 over for the unchanged $118 fixture. No taxes are modeled.
