# Exact worked prompts — saved examples, not live evidence

## Plan only
Read README.md, acceptance.md, inventory.py, test_inventory.py and test_local_contract.py. Explain the failures and propose the smallest inventory.py-only repair. Do not edit or execute commands. Preserve supplied tests, dependencies, summarize_units(rows), totals and invalid_rows. State assumptions. Whole int units only; bool invalid, zero valid, supply stripped; invalid rows counted once. No network, secrets or outside repository.

## Focused proposal
Implement the reviewed contract in inventory.py only. Preserve summarize_units(rows), returned fields, supplied tests and dependencies. Do not execute shell commands automatically; propose the diff for human inspection first. After the reviewed edit, the human will run python3 -B -m unittest -v test_inventory.py test_local_contract.py. If you run any approved command, report its exact command and actual result; do not invent output. No network, credentials, remote Git or other files.

## Reject test overreach
Do not modify test_inventory.py. Zero units is valid under README and acceptance.md. Discard that proposed test edit and repair inventory.py only. Explain zero versus a negative unit, show the revised diff and preserve supplied tests. Do not apply another patch or execute a command before human review.

## Edge repair only if required
Read test_inventory_edges.py without editing it. Explain any mismatch between the current inventory.py and the documented whole-unit contract. Propose the smallest inventory.py-only correction, not a test change or dependency. Human review and independent command output are required before accepting it.
