import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = Path(__file__).resolve().parent
ENV = os.environ.copy()
ENV["PATH"] = (
    str(Path(sys.executable).resolve().parent)
    + os.pathsep
    + ENV.get("PATH", "")
)

pages = sorted((ROOT / "pages").glob("*.md"))

for page in pages:
    output = page.with_suffix(".html")
    cmd = [sys.executable, str(BUILD_DIR / "convert_to_canvas.py"), str(page), str(output)]
    print(" ".join(cmd))
    subprocess.run(cmd, check=True, cwd=BUILD_DIR, env=ENV)


subprocess.run(
    [sys.executable, str(ROOT / "administrivia" / "tool" / "build_coursedog.py")],
    check=True,
    env=ENV,
)
subprocess.run(
    [sys.executable, str(ROOT / "administrivia" / "tool" / "build_canvas_schedule.py")],
    check=True,
    env=ENV,
)
subprocess.run(
    [
        sys.executable,
        str(BUILD_DIR / "convert_to_canvas.py"),
        str(ROOT / "administrivia" / "generated" / "syllabus-coursedog.md"),
        str(BUILD_DIR / "syllabus.html"),
    ],
    check=True,
    cwd=BUILD_DIR,
    env=ENV,
)
tmp = BUILD_DIR / "tmp.html"
if tmp.exists():
    tmp.unlink()

print('done!')
