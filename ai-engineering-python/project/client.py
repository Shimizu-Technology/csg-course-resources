"""Provided CSG HTTPS transport. Learners implement the application around it."""
import json
import os
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *_):
        raise ValueError("Redirect refused; ask CSG to confirm the endpoint")


def validate_endpoint(endpoint):
    if not isinstance(endpoint, str):
        raise ValueError("Use the HTTPS endpoint supplied privately by CSG")
    url = urlparse(endpoint)
    if url.scheme != "https" or not url.hostname or url.username or url.password or url.query or url.fragment:
        raise ValueError("Use the HTTPS endpoint supplied privately by CSG without credentials or query parameters")
    try:
        url.port
    except ValueError as error:
        raise ValueError("Invalid endpoint port") from error
    return endpoint


def read_response(response):
    raw = response.read(131073)
    if len(raw) > 131072:
        raise ValueError("CSG response too large")
    data = json.loads(raw)
    if not isinstance(data, dict) or not isinstance(data.get("status"), str) or data["status"] not in {"proposed", "blocked", "review_needed", "access_limited"} or data.get("review_required") is not True:
        raise ValueError("Invalid CSG response envelope")
    # The student still validates the proposed result contract independently.
    return data


def request_triage(message, version="v2", transport=None):
    endpoint = validate_endpoint(os.environ.get("CSG_TRIAGE_URL"))
    token = os.environ.get("CSG_COURSE_TOKEN")
    if not isinstance(token, str) or not 1 <= len(token) <= 256 or any(c.isspace() for c in token):
        raise ValueError("Set your individual CSG course token privately")
    if not isinstance(message, str) or not isinstance(version, str):
        raise ValueError("Message and prompt version must be strings")
    request = Request(endpoint, data=json.dumps({"message": message, "version": version}).encode(), headers={"Content-Type": "application/json", "Authorization": "Bearer " + token})
    send = transport or build_opener(NoRedirect()).open
    try:
        with send(request, timeout=20) as response:
            return read_response(response)
    except HTTPError as error:
        if error.code not in (400, 429, 503):
            raise ValueError("CSG endpoint unavailable; contact staff") from None
        with error:
            return read_response(error)
    except (TimeoutError, OSError, URLError):
        return {"status": "review_needed", "review_required": True, "error": "Connection unavailable; classify manually without automatic retry"}

if __name__ == "__main__":
    try:
        print(json.dumps(request_triage("The fictional exercise instructions block me today."), indent=2))
    except ValueError:
        print("Check your private CSG access configuration; do not paste credentials into chat or submissions.")
        raise SystemExit(1)
