#!/usr/bin/env python3

import sys
import re 
for line in sys.stdin:
    line = line.strip()
    words = re.split(r'[\s\,\;\:]+', line)
    for word in words:
        print('{0}\t{1}'.format(word, 1))
