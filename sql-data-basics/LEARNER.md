# SQL and Data Basics

Learner preparation guide. Use the matching course in CSG Learn for recordings, submissions and questions. Recordings and admissions are pending; these files alone do not grant access. All practice data is fictional.

## Start here: environment and submission

Required

Create a dedicated Hafa SQL worked project. No terminal, Python installation or GitHub is required. schema.sql defines tables, seed.sql defines fictional starting rows, and main.sql holds one question. Put the definitions/rows below into their files and run `SELECT id, title, category, capacity FROM workshops ORDER BY id;`. Submit the four rows and source query in Learn. Keep the independent workshop fixture in a separate project. Placement: identify/count rows matching confirmed. Predict, run, compare and save exact SQL/output; use the course help route with the smallest query and actual error.

Worked schema:
```sql
-- Worked-example schema, separate from the final fixture; use in Hafa schema.sql.
CREATE TABLE workshops (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  category TEXT NOT NULL,
  capacity INTEGER NOT NULL CHECK (capacity >= 0)
);
CREATE TABLE registrations (
  id INTEGER PRIMARY KEY,
  workshop_id INTEGER NOT NULL REFERENCES workshops(id),
  status TEXT NOT NULL CHECK (status IN ('confirmed', 'waitlisted', 'cancelled')),
  fee_cents INTEGER NOT NULL CHECK (fee_cents >= 0)
);
```

Worked seed:
```sql
-- Fictional Guam community-learning sessions, not real CSG enrollments.
INSERT INTO workshops VALUES
  (1, 'Supply Planner', 'code', 4),
  (2, 'Garden Data Lab', 'data', 4),
  (3, 'Poster Coding', 'code', 5),
  (4, 'Git Practice', 'tools', 2);
INSERT INTO registrations VALUES
  (1, 1, 'confirmed', 1000),
  (2, 1, 'confirmed', 1000),
  (3, 1, 'waitlisted', 1000),
  (4, 2, 'confirmed', 1500),
  (5, 2, 'confirmed', 1500),
  (6, 3, 'confirmed', 2000),
  (7, 3, 'cancelled', 2000);
```

## Lesson 1: Trace related tables before writing a report

Required

**Outcome:** Trace related tables before writing a report. Use the separate worked project and predict before Run.

We will ask practical questions about fictional community-learning sessions in Guam. These are Supply Planner, Garden Data Lab, Poster Coding, and Git Practice. They are not real CSG registrations, revenue, or demand. Your final project has a different workshop fixture. The method transfers; the answers do not.

Open the schema. A workshop has an ID, a title, a category, and a capacity. A registration has its own ID, a workshop ID, a status, and a fee in whole cents. Pause for ten seconds. Which ID connects a registration to its workshop?

`workshop_id` refers to `workshops.id`. It is not the registration's own ID. The primary key identifies one row inside its table; the foreign key describes this connection. The schema also rejects negative capacity, negative fee cents, and statuses outside our three teaching values. Those constraints are useful guardrails, not proof that the business data is complete.

The seed creates four workshops and seven registrations. It deliberately leaves Git Practice with none. Keeping that zero row will matter later.

`SELECT` names columns, `FROM` names their table, and `ORDER BY id` makes the displayed order explicit. Our ending query shows ID, title, category, and capacity. We can trace the row with ID one from schema and seed to the result table. A query asks a question; it does not change these workshop rows.

For E1, name both primary keys and the foreign key in your assessed fixture. For E2, count its four workshops and eight registrations. Do not confuse our seven-row worked example with that eight-row final dataset. Submit your short explanation in Learn. Hafa is the place to run; Learn keeps the source and response we review.

**Worked ending code, on different data from assessment:**
```sql
SELECT id, title, category, capacity FROM workshops ORDER BY id;
```


## E1: schema keys

Required

Name tables and primary keys; registrations.workshop_id→workshops.id. Give one fictional example, no real names.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## E2: count rows

Required

Count assessed workshops and registrations, labelled units: 4 and 8. The worked fixture has 7 registrations is different.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Lesson 2: Choose columns and specify row order

Required

**Outcome:** Choose columns and specify row order. Use the separate worked project and predict before Run.

The star means every workshop column. That is useful for inspection, but a report should ask for the fields its reader needs. Today we want ID, title, and capacity. We do not need category in this particular result.

Pause for ten seconds. How many columns should the ending table have? Which workshop should appear first when we order by ID?

Three columns, with Supply Planner first. SQL does not promise a useful display order just because the seed currently inserts records in that order. `ORDER BY` makes our intention part of the query. I keep ID in the result because it lets us check which row we mean even if titles change.

Notice that capacity is a number in the database. Choosing fewer columns did not calculate a new capacity or delete any workshop. The result is a projection of the table: we selected fields for this question.

Now look at the last row. Git Practice has capacity two and still appears. No registration question has been asked yet. Seeing its workshop row does not mean anybody enrolled.

For E3, work in the separate assessed project. List ID, title, and capacity by ID. Its first row is Python Basics with four seats, and its last is Git Basics with two. Copy your SQL and output table into Learn. If your column order differs from the requested order, change the SELECT list rather than rearranging a screenshot. Reproducible source is what lets another person rerun the question.

**Worked ending code, on different data from assessment:**
```sql
SELECT id, title, capacity FROM workshops ORDER BY id;
```


## E3: projection/order

Required

IDs, titles, capacities by ID. First: 1 | Python Basics | 4; last: 4 | Git Basics | 2.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## E4: both predicates

Required

Code category AND capacity>=4, title order. Python Basics 4 / Web Intro 5. Explain AND/inclusive boundary.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Lesson 3: Combine a category rule and a capacity rule

Required

**Outcome:** Combine a category rule and a capacity rule. Use the separate worked project and predict before Run.

All three of these worked workshops have capacity at least four. But our question is narrower: which are code workshops with capacity at least four? Garden Data Lab has enough capacity and the wrong category. That is our counterexample.

Pause for ten seconds. Predict the two rows after adding the category condition. Keep their alphabetical order in your prediction.

Poster Coding and Supply Planner remain. `AND` requires both predicates to be true for a row. Garden Data Lab fails the code-category predicate even though its capacity is four. Git Practice does not appear either: its category is tools and its capacity is two.

The single quotes mark code as text. Capacity is numeric, so four does not need text quotes. Greater than or equal includes a capacity exactly equal to four. If I used greater than instead, Supply Planner would disappear. That is a boundary we can check without guessing.

That temporary change left only Poster Coding. Restoring greater than or equal brings Supply Planner back. We just tested the boundary and returned to our known ending state.

E4 and Checkpoint A use the different assessed fixture. Ask for title and capacity for code workshops with at least four seats, sorted by title. The expected two titles there are Python Basics and Web Intro. Explain why both conditions are needed. A later new data-category workshop might also have a large capacity; your query should still exclude it. Submit the SQL, rows, and your explanation.

**Worked ending code, on different data from assessment:**
```sql
SELECT title, capacity FROM workshops WHERE category = 'code' AND capacity >= 4 ORDER BY title;
```


## Checkpoint A: transfer

Required

In the independent workshop fixture, select title/capacity for code workshops with capacity>=4, sorted by title. Submit SQL, two rows and explanation of AND/inclusive boundary. Do not copy worked session answers.

## Lesson 4: Count registration rows by status

Required

**Outcome:** Count registration rows by status. Use the separate worked project and predict before Run.

The starting query counts seven registration rows. It does not count workshops, filled seats, or distinct people. There are no person identifiers in this teaching dataset. We must name the unit before interpreting a number.

Now our question is how many registrations have each status. `GROUP BY status` collects rows into one group for each status value. The aggregate COUNT then runs inside each group. `ORDER BY status` gives a predictable output order.

Pause for ten seconds. Count the worked seed's confirmed, waitlisted, and cancelled rows. Does their sum return to seven?

Cancelled one, confirmed five, waitlisted one. They add back to seven. COUNT star counts each source row in this grouped query. The alias registration_rows names the number honestly. A confirmed row is the state our later seat rule will count. A waitlist expresses a different state and does not fill a seat in this fictional report.

Grouping reduces several registration records into three result rows. That is why result-row count and source-row count are different. If you see three result rows, that does not mean there were three registrations.

For E5, group statuses in your assessed fixture and keep the same named unit. It has six confirmed, one waitlisted, and one cancelled registration. Save the SQL and result in Learn, then add a sentence saying you counted registration rows, not unique people. We can answer only what the schema records. If a real business needed distinct people, it would need an appropriate identifier and a new question.

**Worked ending code, on different data from assessment:**
```sql
SELECT status, COUNT(*) AS registration_rows FROM registrations GROUP BY status ORDER BY status;
```


## E5: grouped rows

Required

Group registration rows by status, sorted status. cancelled 1 / confirmed 6 / waitlisted 1. Not unique people.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## E6: inner join

Required

Registration 1 → Python Basics | confirmed. Explain columns and joined IDs.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Lesson 5: Join one registration to its workshop title

Required

**Outcome:** Join one registration to its workshop title. Use the separate worked project and predict before Run.

This registration stores a workshop ID. The title lives in the other table. We should connect the rows through their keys, not copy a title into every registration or guess from row positions.

Pause for ten seconds. Trace registration ID one in the worked seed. Which workshop ID does it reference, and what title belongs to that ID?

`workshops AS w` and `registrations AS r` give short table aliases. `w.title` is the workshop's title; `r.status` is the registration's status. JOIN connects records where `r.workshop_id` equals `w.id`. The ON condition expresses the relationship. The WHERE condition selects the registration with its own ID one. These are different jobs.

I qualify both IDs because two tables have a column named ID. An ambiguous column name can produce an error or hide which table I intended. Writing r.id and w.id makes the question readable.

The output matches the traced key. An ordinary JOIN is an inner join: it returns matched combinations. That is appropriate for finding the workshop attached to this registration. But it will not be enough for a report that must include workshops with no registrations. Git Practice has nothing on the registration side to match.

For E6, use registration one in your assessed fixture. It connects to Python Basics and confirmed. Explain which table contributes each output column. The supplied foreign key rejects a registration pointing to a nonexistent workshop; that protects this relationship, but it does not invent missing registrations. Save your query and output. In the next clip we will intentionally keep the workshop with no match.

**Worked ending code, on different data from assessment:**
```sql
SELECT w.title, r.status
FROM workshops AS w
JOIN registrations AS r ON r.workshop_id = w.id
WHERE r.id = 1;
```


## E7: preserve zero

Required

Count all real registration IDs per workshop, ID order: 3/3/2/0. Explain COUNT(r.id), not COUNT(*).

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Lesson 6: Keep zero-registration workshops with LEFT JOIN

Required

**Outcome:** Keep zero-registration workshops with LEFT JOIN. Use the separate worked project and predict before Run.

The three displayed counts are correct for matched workshops, but the report is incomplete. Git Practice is absent. We need every workshop, including a zero count, so the workshop table must be the preserved side.

Pause for ten seconds. When Git Practice has no matching registration, should COUNT of a registration ID be zero or one?

LEFT JOIN keeps each workshop even when there is no matching registration. For a missing match, registration fields are SQL NULL. COUNT of r.id counts non-NULL registration IDs, so that preserved workshop has zero. COUNT star would count the preserved result row and misleadingly give one.

The status rule belongs inside ON for this question. We match only confirmed registrations while preserving every workshop. A WHERE condition on r.status would run after the join. For Git Practice, r.status is NULL, so WHERE confirmed would remove it again.

Supply Planner two, Garden Data Lab two, Poster Coding one, Git Practice zero. `GROUP BY w.id, w.title` makes one group per workshop. Grouping by the stable ID avoids combining different workshops just because they share a title. We use ORDER BY ID for a stable sequence.

Now temporarily move the status condition back into WHERE, keeping LEFT JOIN, and run. Git Practice disappears. Restore the named ending query and run again. This is a counterexample, not a stylistic preference.

For E7, count all registration IDs per assessed workshop. For E8 and Checkpoint B, count confirmed only and retain Git Basics at zero. Your assessed confirmed counts are two, three, one, zero. Explain why the ON predicate preserves the zero row. Save the full SQL and output, not just a statement that your numbers look right.

**Worked ending code, on different data from assessment:**
```sql
SELECT w.title, COUNT(r.id) AS confirmed
FROM workshops AS w
LEFT JOIN registrations AS r
  ON r.workshop_id = w.id AND r.status = 'confirmed'
GROUP BY w.id, w.title ORDER BY w.id;
```


## E8: confirmed only

Required

LEFT JOIN with status in ON, ID order: 2/3/1/0. Explain why WHERE would lose the zero row.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Checkpoint B: integration

Required

Count confirmed registration IDs on every assessed workshop, including Git Basics 0. Submit all four rows in ID order and explain why WHERE confirmed after LEFT JOIN would lose the no-match row. Explain COUNT(r.id), not COUNT(*).

## Lesson 7: Calculate seats using the stated status rule

Required

**Outcome:** Calculate seats using the stated status rule. Use the separate worked project and predict before Run.

This query subtracts all registration rows from capacity. It reports Supply Planner one open seat and Poster Coding three. That looks plausible, but it violates our rule. Supply Planner's waitlisted row is not a filled seat. Poster Coding's cancelled row is not a filled seat either.

Pause for ten seconds. Recalculate those two answers using only confirmed registrations. Supply Planner has capacity four and two confirmed. Poster Coding has capacity five and one confirmed.

Supply Planner has two open, Garden Data Lab two, Poster Coding four, Git Practice two. The arithmetic is capacity minus confirmed count. We reuse the left-join behavior so a workshop with no registrations still has its whole capacity open.

We have not added an automatic floor of zero. If changed data contains more confirmed rows than capacity, a negative result tells us to investigate the records or the business rule. Silently hiding it with a zero would lose that evidence. We also do not treat waitlisted as a promise of a seat.

The result is current status in this small fixture. It is not a prediction of demand or a booking system.

For E9, calculate assessed open seats in workshop ID order: two, zero, four, two. SQL Basics is full in that different fixture. Do not carry Garden Data Lab's worked count into it. Check the confirmed counts first, then subtract from each actual capacity. If the count is wrong, fix the join or status predicate before changing the subtraction. Submit both the query and table in Learn.

**Worked ending code, on different data from assessment:**
```sql
SELECT w.title, w.capacity - COUNT(r.id) AS open_seats
FROM workshops AS w
LEFT JOIN registrations AS r
  ON r.workshop_id = w.id AND r.status = 'confirmed'
GROUP BY w.id, w.title, w.capacity ORDER BY w.id;
```


## E9: open seats

Required

Capacity-confirmed: 2/0/4/2. Waitlisted/cancelled do not fill; investigate negatives rather than hide them.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## E10: fee cents

Required

Sum confirmed fee_cents, preserve zero, amount descending then title. SQL 9000 / Python 4000 / Web 1500 / Git 0, total 14500. These are recorded fictional fee amounts, not proven collected revenue.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Lesson 8: Sum confirmed fee cents and replace a missing sum with zero

Required

**Outcome:** Sum confirmed fee cents and replace a missing sum with zero. Use the separate worked project and predict before Run.

A registration's fee is stored as whole cents. We will sum fee cents for confirmed records only. We are not proving that money was collected: this schema has no payment transaction field. These are fictional confirmed fees, not actual revenue or CSG sales.

Pause for ten seconds. Garden Data Lab has two confirmed fees of fifteen hundred cents. What should its sum be? What should Git Practice's displayed sum be when it has no confirmed registrations?

SUM adds non-NULL values in each group. With no matching fee values, SUM returns SQL NULL, not zero. COALESCE takes the sum if it exists, otherwise the second value zero. That makes the report's zero case explicit without changing the stored rows.

We still match confirmed only inside ON and preserve all workshops. The alias confirmed_fee_cents tells us both the rule and the unit. Ordering by that amount descending puts the largest first. A second order by title makes ties predictable.

Garden Data Lab three thousand cents; Poster Coding two thousand; Supply Planner two thousand; Git Practice zero. The tie sorts Poster before Supply by title. The total of these worked confirmed fee amounts is seven thousand cents. If I explain that as dollars, it is seventy dollars, and I must label the conversion. The query continues to return integer cents.

For E10, write the assessed confirmed-fee query. Its values are nine thousand, four thousand, fifteen hundred, and zero, with a total fourteen thousand five hundred cents. Keep Git Basics in the report and explain that this is the fixture's confirmed fee amount. Your final finding must not claim it is actual CSG income. Submit source, units, and output.

**Worked ending code, on different data from assessment:**
```sql
SELECT w.title, COALESCE(SUM(r.fee_cents), 0) AS confirmed_fee_cents
FROM workshops AS w
LEFT JOIN registrations AS r
  ON r.workshop_id = w.id AND r.status = 'confirmed'
GROUP BY w.id, w.title ORDER BY confirmed_fee_cents DESC, w.title;
```


## Independent final project

Required

Independently write five SELECT queries in queries_starter.sql on the assessed Hafa schema/seed, not the worked sessions. End every query with a semicolon and run each separately in main.sql:

1. ID, title, capacity by ID.
2. Code-workshop title/capacity, capacity>=4, title order.
3. Confirmed counts for every workshop, including zero, by ID.
4. Capacity minus confirmed count as open seats, by ID.
5. Confirmed fee cents, including zero, amount descending then title.

Submit exact SQL and all five output tables plus three sentences: which workshop has no open seats, which has most, and one fixture limit. Confirm waitlisted/cancelled do not fill seats, Git Basics remains zero and sum confirmed fees 14500 cents. The schema does not prove payment collection or unique people; these are not actual CSG registrations/sales. Run E11/E12 in a throwaway copy and Reset. Finish after Lesson 9; the project opens earlier to begin.

10-point rubric: 2 projection/filter/order; 2 zero-preserving joins; 2 confirmed counts/open/cents; 2 reproducible five outputs/negative checks; 1 grounded finding; 1 limits. Optional extension is outside the rubric.

### Workshop data brief — 10 points

Assess five runnable questions, reproducible result tables and a finding limited to the supplied fictional records.

- **Projection, predicates and order — 2 points:** Selects requested columns, applies every required predicate and supplies explicit stable ordering.
- **Zero-preserving joins — 2 points:** Preserves workshops without matching registrations and explains the join and predicate placement.
- **Status, counts, seats and cents — 2 points:** Uses the stated counting unit and status rules, computes open seats and labels integer fee cents correctly.
- **Reproducible outputs and counterexamples — 2 points:** Provides all five SQL queries and result tables, checks zero/mixed-status cases and restores the private practice fixture.
- **Grounded finding — 1 point:** States the requested findings from the submitted results without extending beyond what the data supports.
- **Data limits — 1 point:** Identifies a relevant missing field or limitation, including the distinction between registration rows, people and payment evidence.

## Lesson 9: Prove a finding with a counterexample and a reset

Required

**Outcome:** Prove a finding with a counterexample and a reset. Use the separate worked project and predict before Run.

This starting question finds Poster Coding and Supply Planner because each has a cancelled or waitlisted row. It does not answer which workshops have zero confirmed registrations. Both have confirmed rows as well, and the inner join loses Git Practice entirely.

Pause for ten seconds. Which worked workshop really has no confirmed registrations?

Git Practice. WHERE filters source or joined rows before grouping. HAVING filters the grouped result. We keep all workshops, match confirmed only, group each workshop, then keep the groups whose registration-ID count is zero. The question is now precise.

That does not mean nobody ever showed interest. It means this fixture has zero confirmed records for that workshop. The schema does not record every inquiry, and this four-workshop sample cannot predict future enrollment.

This probe adds one fictional waitlisted Garden Data Lab row. It then asks for confirmed counts and open seats. Garden remains two confirmed and two open because the new row is not confirmed. If every registration were counted as a seat, its answer would wrongly drop to one open.

I will now Reset database in this throwaway project. Reset rebuilds from its saved schema and seed. The added row is not in seed, so it disappears. I run SELECT COUNT star FROM registrations and expect seven. This checks the reset, rather than assuming a button label means it worked.

For E11, find assessed workshops with no confirmed registrations and explain the limit. For E12, use a private assessed copy to add a SQL Basics waitlist with a fresh ID. Confirmed stays three and open stays zero. Reset before continuing. Your final brief submits five queries, all five output tables, and three sentences: the full workshop, the workshop with most open seats, and one data limit. Save exact SQL in Learn. Similar output on this small dataset is expected; being able to explain and test the question is what matters.

**Worked ending code, on different data from assessment:**
```sql
SELECT w.title
FROM workshops AS w
LEFT JOIN registrations AS r
  ON r.workshop_id = w.id AND r.status = 'confirmed'
GROUP BY w.id, w.title
HAVING COUNT(r.id) = 0
ORDER BY w.title;
```

In a throwaway worked copy, use this exact probe, Reset database, then run COUNT registrations to verify 7 again:
```sql
-- Separate practice copy only. Reset to original seed after this probe.
INSERT INTO registrations VALUES (8, 2, 'waitlisted', 0);
SELECT w.title, COUNT(r.id) AS confirmed, w.capacity - COUNT(r.id) AS open_seats
FROM workshops AS w
LEFT JOIN registrations AS r
  ON r.workshop_id = w.id AND r.status = 'confirmed'
GROUP BY w.id, w.title, w.capacity ORDER BY w.id;
```


## E11: zero confirmed

Required

Find assessed workshops with no confirmed rows: Git Basics. A non-confirmed row alone does not imply zero confirmed rows.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## E12: counterexample/reset

Required

In a throwaway assessed copy add registration 9, workshop 2, waitlisted, fee 0. SQL Basics stays 3 confirmed/0 open. Reset, then COUNT registrations returns 8. Leave shared seed unchanged.

Submit exact source/query, input where changed, output and requested explanation. Fictional data only. A mutable link may accompany the saved review copy.

## Optional saved-example or agent extension

Optional

Only after submitting the independent five-query brief: review the saved CASE-count demand query or an optional agent change. Display original confirmed fee total 14500 cents and all demand rows. In a separate copy add Git Basics waitlist row 9; Git changes 0 confirmed/0 waitlisted/2 open to 0/1/2. Explain CASE and why waitlists do not reduce seats. Rerun original fee total and Reset the copy. Submit one reviewed line with a reason, the before/after Git rows and one test input/output. Saved-example review needs no AI account and does not affect required project points.

Run this saved proposal in a separate assessed-fixture practice project, one query at a time:
```sql
-- Optional extension after the independent five-query project.
-- Preserve workshops with no registrations and count only each intended status.
SELECT w.title,
       COUNT(CASE WHEN r.status = 'confirmed' THEN 1 END) AS confirmed,
       COUNT(CASE WHEN r.status = 'waitlisted' THEN 1 END) AS waitlisted,
       w.capacity - COUNT(CASE WHEN r.status = 'confirmed' THEN 1 END) AS open_seats
FROM workshops AS w
LEFT JOIN registrations AS r ON r.workshop_id = w.id
GROUP BY w.id, w.title, w.capacity
ORDER BY w.id;
```

`CASE WHEN` returns 1 for the requested status and NULL for other statuses. COUNT ignores NULL, so each column counts that status without removing workshops from the LEFT JOIN. Open seats subtract confirmed registrations only. Read the four original rows aloud: Python Basics 2 confirmed / 1 waitlisted / 2 open; SQL Basics 3 / 0 / 0; Web Intro 1 / 0 / 4; Git Basics 0 / 0 / 2.

Check the fee sum, add the fictional waitlist, and run the saved query again:
```sql
SELECT COALESCE(SUM(fee_cents), 0) AS confirmed_fee_cents
FROM registrations WHERE status = 'confirmed';
```
```sql
INSERT INTO registrations VALUES (9, 4, 'waitlisted', 0);
```

Git changes to 0 / 1 / 2; every other row remains unchanged and the confirmed fee sum remains 14500 cents. Reset the practice database, then verify `SELECT COUNT(*) FROM registrations;` returns 8. An optional agent prompt is: “Add waitlisted counts beside confirmed and open seats. Keep all workshops, preserve confirmed fee totals, show a diff and a waitlist counterexample. Fictional data only.” Review every changed predicate before accepting it.
