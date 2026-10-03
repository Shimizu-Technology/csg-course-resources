# Python Automation · learner starter

**Course status:** preparation draft. Your instructor will open the course in CSG Learn when its lessons and access are ready. Python Fundamentals or equivalent variables, loops, dictionaries, functions, and error reading are recommended.

The fictional [orders.csv](starter/orders.csv) contains seven rows. Your final program should read them, skip unpaid rows, report invalid paid rows with line numbers, total valid paid amounts by item using `Decimal`, and create a sorted CSV report. Begin with [automation_starter.py](starter/automation_starter.py). It contains `TODO` functions; it is not a solution.

For browser practice, paste the starter into a new Hafa Code Python project. The same fictional CSV text is embedded as `RAW_CSV` so the browser does not need to open a local file. If you work locally, run `python3 starter/automation_starter.py` from this course folder. The starter raises `NotImplementedError` until you complete the functions.

The sample has four valid paid rows, one unpaid row, and two invalid paid rows. Your sorted report should total Notebook `13.50` and Pen `6.25`, for `19.75` overall. Also test an empty input, a duplicate order ID, and a missing header. Paste your final source, report, counts, and error messages into the Learn project exercise. A repository or Hafa link may accompany that saved copy.
