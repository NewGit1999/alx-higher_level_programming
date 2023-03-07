#!/usr/bin/python3
for let in range(97, 123):
    if let == 113 or let == 101:
        continue
    print('{:c}'.format(let), end="")
