# SQL and Data Basics · learner starter

**Course status:** preparation draft. Your instructor will open the course in CSG Learn after the setup and submission flow is checked. Basic variables and tables are helpful; the course teaches SQL from the beginning.

This fictional workshop database has four workshops and eight registration rows. For local Python 3, keep [schema.sql](starter/schema.sql) beside [sql_starter.py](starter/sql_starter.py). Change its `QUERY` string, then run `python3 sql_starter.py`. Begin with `SELECT id, title, capacity FROM workshops ORDER BY id`; it should print four rows, from Python Basics to Git Basics. The five final questions are in [queries_starter.sql](starter/queries_starter.sql), with no answers filled in.

For Hafa Code, create a new SQL project. Replace its `schema.sql` with [hafa/schema.sql](hafa/schema.sql), its `seed.sql` with [hafa/seed.sql](hafa/seed.sql), and its `main.sql` with one query at a time. Run the overview first. The held Hafa preview returned the four expected rows and the confirmed-count `LEFT JOIN` returned `2, 3, 1, 0`, including Git Basics at zero. This does not yet establish the production learner flow.

Submit all five final SQL queries, their output tables, and a short finding in Learn. Paste the SQL and output there even if you add a Hafa or GitHub link. These are teaching numbers, not actual CSG registrations or revenue.
