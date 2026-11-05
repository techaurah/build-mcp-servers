"""Smoke test for Lesson 31."""
import subprocess
import sys

def main():
    out = subprocess.run([sys.executable, "release_check.py"],
                         capture_output=True, text=True)
    assert out.returncode == 0, out.stdout + out.stderr
    print("smoke ok: release rehearsal checks pass")

if __name__ == "__main__":
    main()
