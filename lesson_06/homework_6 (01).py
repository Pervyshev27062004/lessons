import collections
from collections import Counter

text = ["Alex", "PErvyshev", "PErvyshev", "key", "key", "key"]
Counter = collections.Counter(text)
most_common = Counter.most_common()
longest = max(text, key = len)
print(most_common)
print(longest)