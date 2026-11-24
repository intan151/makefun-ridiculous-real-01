#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun bounty
u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.

Writes one sentence (<=200 chars) pitching a bizarre startup idea
that sounds like a joke until the business logic lands — naming
rights for potholes — to /output/entry.txt. Stdlib only.
"""
import os

SENTENCE = "We sell naming rights to potholes: a local shop sponsors one, the city fixes it, and your logo sits where every driver is already staring."

def main():
    assert 1 <= len(SENTENCE) <= 200, f"sentence is {len(SENTENCE)} chars"
    assert "\n" not in SENTENCE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
