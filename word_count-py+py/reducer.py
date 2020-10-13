#!/usr/bin/env python3
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('{0}\t{1}'.format(current_word, current_count))
        current_count = count
        current_word = word


if word == current_word:
    print("{0}\t{1}".format(current_word, current_count))
