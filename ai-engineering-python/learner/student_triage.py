"""Your independent project. Standard-library Python; no provider key here.
The CSG transport is supplied separately as client.py. Do not import staff service.
"""

def clean_message(message):
    """Return stripped fictional text or raise ValueError; see LEARNER.md."""
    raise NotImplementedError('Implement input contract')

def parse_proposal(raw):
    """Return validated category/urgency/reason dictionary or raise ValueError."""
    raise NotImplementedError('Implement output contract')

def run_triage(message, predict):
    """Call injected predict once at most; always return a human-review envelope."""
    raise NotImplementedError('Implement safe pipeline')

def evaluate_cases(cases, predict):
    """Preserve denominator, two independent match counts, fallbacks and case rows."""
    raise NotImplementedError('Implement evaluation')

def human_review(response, category, urgency):
    """Record explicit allowed human labels and whether they changed the proposal."""
    raise NotImplementedError('Implement human decision')


def summarize_attempts(attempts):
    """Known cost sum, missing-usage count, all attempts and fallbacks; see spec."""
    raise NotImplementedError('Implement honest metrics summary')
