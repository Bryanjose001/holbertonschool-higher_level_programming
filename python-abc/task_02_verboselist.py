#!/usr/bin/python3
__import__("sys")


class VerboseList(list):
    """List modifying class"""

    def append(self, item):
        print(f"Added [{item}] to the list.")
        return super().append(item)

    def extend(self, x):
        print(f"Extended the list with [{len(x)}] items.")
        return super().extend(x)

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        return super().remove(item)

    def pop(self, item=-1):
        print(f"Popped [{self[item]}] from the list.")
        return super().pop(item)
