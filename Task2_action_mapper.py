#!/usr/bin/env python3
import sys

for line in sys.stdin:
    uid, action, cid = line.strip().split('\t')
    print(f"{uid}\t{action}\t1")
