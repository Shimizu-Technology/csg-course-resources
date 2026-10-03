# Validate fictional community supply units

Zero-unit rows were rejected, blank names created groups, fractional units were accepted and text units raised TypeError. The repair validates dictionary shape, supply name and nonnegative integer units, rejects bool, trims accepted names and counts invalid rows once.

Validation: python3 -B -m unittest -v test_inventory.py test_local_contract.py test_inventory_edges.py — 8 tests passed in the local worked fixture. Reviewed inventory.py hunks and preserved supplied tests. This saved example is not evidence of a live agent run, and this small fixture does not establish production readiness.
