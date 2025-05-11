#!/usr/bin/python3
import marshal

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as f:
        f.read(16)  # Skip header
        code = marshal.load(f)
        namespace = {}
        exec(code, namespace)
        for name in sorted(namespace):
            if not name.startswith("__"):
                print(name)
