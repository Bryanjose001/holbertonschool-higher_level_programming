#!/usr/bin/python3
print(", ".join("{:01}{:01}".format(i, j) for i in range(10) for j in range(i + 1, 10)))
