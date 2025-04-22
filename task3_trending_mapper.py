#!/usr/bin/env python3
import sys

for line in sys.stdin:
    uid, action, cid = line.strip().split('\t')
    if action in ["like", "share"]:
        print(f"{cid}\t1")
