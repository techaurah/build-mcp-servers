"""Smoke test for Lesson 30: the gate suite itself passes."""
import subprocess
import sys

def main():
    out = subprocess.run([sys.executable, "gate_suite.py"],
                         capture_output=True, text=True)
    assert out.returncode == 0, out.stdout + out.stderr
    assert "gate checks passed" in out.stdout
    print("smoke ok: gate suite green")

if __name__ == "__main__":
    main()
