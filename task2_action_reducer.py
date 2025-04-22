#!/usr/bin/env python3
import sys
from collections import defaultdict

current_user = None
action_counts = defaultdict(int)

for line in sys.stdin:
    uid, action, count = line.strip().split('\t')
    if current_user and uid != current_user:
        print(f"{current_user}\t{dict(action_counts)}")
        action_counts.clear()
    current_user = uid
    action_counts[action] += int(count)

if current_user:
    print(f"{current_user}\t{dict(action_counts)}")
