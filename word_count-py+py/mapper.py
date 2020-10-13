#!/usr/bin/env python3

import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print('{0}\t{1}'.format(word, 1))
