# Code School of Guam course resources

This repository holds small, copyable code examples and starter files for Code School of Guam courses. **CSG Learn is the course home:** use it for lessons, due dates, submissions, feedback, and questions. [Hafa Code](https://code.shimizu-technology.com/) lets you run the Python examples in a browser without installing anything.

## Courses

| Course | Status | Start here |
| --- | --- | --- |
| Python Fundamentals, December 2026 pilot | Prepared for invited learners; course opens in Learn | [Course resources](python-fundamentals/2026-12/README.md) |
| Python Automation | Learner resources prepared; recordings/admissions pending | [Course resources](python-automation/README.md) |
| SQL and Data Basics | Learner resources prepared; recordings/admissions pending | [Course resources](sql-data-basics/README.md) |
| Ruby Fundamentals | Learner resources prepared; recordings/admissions pending | [Course resources](ruby-fundamentals/README.md) |
| JavaScript Fundamentals | Learner resources prepared; recordings/admissions pending | [Course resources](javascript-fundamentals/README.md) |
| Frontend with JavaScript | Learner resources prepared; recordings/admissions pending | [Course resources](frontend-javascript/README.md) |
| APIs with Ruby on Rails | Learner resources prepared; recordings/admissions pending | [Course resources](rails-apis/README.md) |
| AI Engineering with Python | Offline resources prepared; live CSG access pending | [Course resources](ai-engineering-python/README.md) |
| Agent Workflows for Developers | Disposable Git practice prepared; live CSG access pending | [Course resources](agent-workflows/README.md) |

The Python course runs December 1–20, 2026. It has three weeks of short lessons and practice, plus one private hour each week for each enrolled learner. Your instructor will give you access to the course in Learn when the recording and admissions gates are cleared. A GitHub account and local Python installation are optional.

Free/included companions: [GitHub and local setup guide](free-companions/LEARNER.md).

## How to use these files

1. Open the matching lesson in CSG Learn first. The lesson tells you what to build and where to submit it.
2. Use the setup route in that course's README. Hafa Code supports the beginner browser projects; the Rails project runs locally.
3. Change and test your code. Paste the version you want reviewed into the Learn exercise. You can add a GitHub or Hafa Code link as a second reference.

A link alone is not the reviewed snapshot: repository branches and shared Hafa projects can change. Keep the code itself in Learn when you submit.

## For course staff

Keep learner files here free of answers, private meeting links, student work, personal information, tokens, and client data. Staff solutions and assessment notes belong in the staff-only CSG Learn fields and the private Brain Dump pilot assets. Before a cohort starts, compare the starter and examples here with the current Learn lesson and rehearse its supported runtime. See [release checks](RELEASE.md).

This is the staff preparation repository for all nine courses. Do not grant whole-repository access to learners enrolled in only one course. Run `python3 tools/build_course_bundles.py` to prepare a separate ZIP for each course, including its free setup companion. Upload only the matching ZIP to that course's protected Learn resources after verifying the cohort entitlement. The build writes a SHA-256 manifest to `dist/`; GitHub access is not required for learners.

This repository is private during course preparation. The learner folders are preparation material, not enrollment offers. Do not describe this repository as a public download until its access has been deliberately changed and checked.
