#!/usr/bin/env python3
import sys
import json
from datetime import datetime

def is_valid_timestamp(ts):
    try:
        datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ")
        return True
    except:
        return False

for line in sys.stdin:
    fields = line.strip().split('\t')
    if len(fields) != 5:
        continue
    ts, uid, action, cid, meta = fields
    if not is_valid_timestamp(ts):
        continue
    try:
        json.loads(meta)
        print(f"{uid}\t{action}\t{cid}")
    except:
        continue
