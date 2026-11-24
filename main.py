#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — write one number to /output/entry.txt."""
import os

COUNT = "47"

OUT = "/output/entry.txt"

def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(COUNT)
    with open(OUT, encoding="utf-8") as f:
        landed = f.read()
    assert landed == COUNT, f"readback mismatch: {landed!r}"
    print(f"wrote {landed!r}")

if __name__ == "__main__":
    main()
