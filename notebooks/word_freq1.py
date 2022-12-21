def word_freq(text):
    def strip_punctuation(s):
        return s.strip(".,?!\"\':;()[]{}")
    freq = {}
    for line in text.split("\n"):
        for word in map(str.lower, map(strip_punctuation, line.split())):
            if word in freq:
                freq[word] = freq[word] + 1
            else:
                freq[word] = 1
    return freq

import sys
f = open(sys.argv[1], "r")
n = int(sys.argv[2])
ffreq = word_freq(f.read())
def val(kv):
    return kv[1]
import more_itertools
for word, freq in more_itertools.take(n, sorted(ffreq.items(), key=val, reverse=True)):
    print(f"{word} ⇒ {freq}")

# Further improvements.
# - Specify a range.
# - Filter out common words like "the"...
