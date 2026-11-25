"""How Many Tabs Do You Have Open? — one number to /output/entry.txt.

Stdlib only, no network, deterministic.
Revision: count kept, rewritten as a flat authored script.
"""
import os

# The honest number. Every one of them is "just for reference".
COUNT = "47"
PATH = "/output/entry.txt"

os.makedirs(os.path.dirname(PATH), exist_ok=True)
with open(PATH, "w", encoding="utf-8") as fh:
    fh.write(COUNT)
with open(PATH, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == COUNT, f"readback mismatch: {landed!r}"
print(f"wrote {landed!r} to {PATH}")