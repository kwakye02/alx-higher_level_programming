#!/usr/bin/python3
for n in range(0, 100):
    if n == 99:
        print(f"{n}")
    else:
        print("{:02}".format(n), end=", ")
