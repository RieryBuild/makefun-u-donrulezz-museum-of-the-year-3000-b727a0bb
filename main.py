import os

ENTRY = "Hotel shower dial, c. 2024. Calibrated in scald, freeze, and two seconds of just right before a toilet flushed down the hall."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
