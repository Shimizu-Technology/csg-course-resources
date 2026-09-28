# Course resource release checks

**Status on September 26, 2026:** repository prepared for review. The December learner cohort is not yet enrolled, and these links have not been checked from an enrolled learner account.

**September 28 addition:** Six future courses now have learner-only starter folders in a held branch. They are not visible on `main`, not assigned to students in Learn, and not sale-ready. Check every file and link against its Learn lesson before distributing. In particular, the SQL Hafa fixture was verified in the held Hafa preview, while server sharing failed and fell back to a long snapshot URL. Keep the actual SQL and output in Learn submissions. The Rails starter must be rehearsed on a fresh Mac and Windows/WSL setup before it is required.

## Before giving learners a link

- Compare `python-fundamentals/2026-12/starter/expense_summary.py` with the current Lesson 8 starter in production CSG Learn. The six expense records and budget should match exactly.
- Run `python3 -m compileall -q python-fundamentals/2026-12` locally and copy each runnable practice starter into production Hafa Code. Check a fresh session, not only a warm one.
- Check the README and links from a learner account. A private GitHub repository requires each learner to be granted access. If access is awkward, give learners the files through Learn; GitHub is optional for this pilot.
- Keep the repository private while it contains preparation notes. If any part becomes public, check every file and commit history for staff answers and private information first. A later public learner repository should be a clean copy, not a visibility flip without a history audit.
- Confirm the final Learn page, recording, transcript, starter file, expected output, and feedback wording agree.
- Do not publish the optional local setup or GitHub guides as tested until they have been rehearsed on a current Mac and Windows 11/WSL machine with a fresh demo account.

CSG Learn remains the submission and feedback record. This repository does not grant course access or meeting entitlement.
