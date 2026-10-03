# Saved plan example — not a live result

The current truthiness check incorrectly rejects zero. Blank names create an invalid group. Text comparison crashes; floats are accepted even though whole units are required. Proposed narrow fix: reject non-dictionary rows, require and strip a nonblank supply string, explicitly reject bool and non-int units, reject negative units, and group the rest. Preserve tests and function names. No command has been run and no file changed. Human review must confirm each claim before implementation.
