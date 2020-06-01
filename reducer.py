# Reducer

import sys

# maps words to their counts
words_count = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # covert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        words_count[word] = words_count[word] + count
    except:
        words_count[word] = count

for word in words_count.keys():
    print('%s\t%s' % (word, words_count[word]))
