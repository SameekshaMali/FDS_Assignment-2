#!/usr/bin/env python3
import sys

current_cid = None
total = 0
THRESHOLD = 100  # Example

for line in sys.stdin:
    cid, count = line.strip().split('\t')
    if current_cid and cid != current_cid:
        if total > THRESHOLD:
            print(f"{current_cid}\t{total}")
        total = 0
    current_cid = cid
    total += int(count)

if current_cid and total > THRESHOLD:
    print(f"{current_cid}\t{total}")
