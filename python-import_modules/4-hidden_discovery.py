#!/usr/bin/python3
import marshal

with open("hidden_4.pyc", "rb") as f:
    f.read(16)  # Skip the .pyc header (magic number, flags, timestamp, etc.)
    code = marshal.load(f)

namespace = {}
exec(code, namespace)

for name in sorted(namespace):
    if not name.startswith("__"):
        print(name)
