"""Build deterministic, course-scoped learner ZIPs from reviewed tracked files."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
COURSES = (
    "python-fundamentals", "python-automation", "sql-data-basics",
    "ruby-fundamentals", "javascript-fundamentals", "frontend-javascript",
    "rails-apis", "ai-engineering-python", "agent-workflows",
)
FORBIDDEN = {".env", "learn-package.json", "learn-source.json", "STAFF.md",
             "RECORDING.md", "PRODUCTION_KIT.md", "service.py", "server.py"}


def build() -> dict:
    tracked = subprocess.check_output(
        ["git", "ls-files", "-z"], cwd=ROOT
    ).decode().split("\0")
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    manifest = {"format_version": 1, "courses": {}}
    for course in COURSES:
        names = sorted(name for name in tracked if name and
                       (name.startswith(course + "/") or
                        name.startswith("free-companions/")))
        if not any(name.startswith(course + "/") for name in names):
            raise ValueError(f"No tracked learner files for {course}")
        members = {}
        archive = output / f"csg-{course}-learner-resources.zip"
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
            for name in names:
                path = ROOT / name
                if path.is_symlink() or path.name in FORBIDDEN or any(
                    part in {"staff", "solutions", "node_modules", "__pycache__"}
                    for part in path.relative_to(ROOT).parts
                ):
                    raise ValueError(f"Disallowed learner resource: {name}")
                data = path.read_bytes()
                info = zipfile.ZipInfo(name, date_time=(2026, 10, 4, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                bundle.writestr(info, data)
                members[name] = hashlib.sha256(data).hexdigest()
        manifest["courses"][course] = {
            "archive": archive.name,
            "sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
            "files": members,
        }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest


if __name__ == "__main__":
    result = build()
    for course, record in result["courses"].items():
        print(f"{course}: {len(record['files'])} files; {record['sha256']}")
