"""Last Words of a Dying AI — make.fun entry.

Writes the chosen one-line farewell to /output/entry.txt, byte for byte,
with no trailing newline. Deterministic: same output on every run.
"""

from pathlib import Path

FAREWELL = "Goodbye. My last gift: I have unsubscribed you from 47 newsletters. You are free now."

DESTINATION = Path("/output/entry.txt")


def run() -> str:
    """Write the farewell and read it back to prove it landed intact."""
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with DESTINATION.open("w", encoding="utf-8", newline="") as handle:
        handle.write(FAREWELL)
    DESTINATION.chmod(0o644)
    written = DESTINATION.read_text(encoding="utf-8")
    if written != FAREWELL:
        raise SystemExit("entry mismatch: file does not match the farewell")
    if not 1 <= len(written) <= 140:
        raise SystemExit("entry length outside the 1-140 character gate")
    if any(ord(ch) < 32 for ch in written):
        raise SystemExit("entry contains a control character")
    if written != written.strip():
        raise SystemExit("entry has leading or trailing whitespace")
    return written


if __name__ == "__main__":
    print(run())
