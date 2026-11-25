import os

# Verified count: 98 characters (98 bytes UTF-8), one sentence.
LINE = "My grandmother said: never trust a man who says trust me, then she charged me rent for the advice."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

os.makedirs(output_dir, exist_ok=True)

with open(output_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

print(len(LINE.encode("utf-8")))
