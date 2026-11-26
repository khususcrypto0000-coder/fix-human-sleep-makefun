import os

ENTRY = "Fixed: sleep now supports respawn. Dying in a dream no longer wakes you up; you just respawn at your last checkpoint."

assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
assert "\n" not in ENTRY and ENTRY.strip() == ENTRY

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
