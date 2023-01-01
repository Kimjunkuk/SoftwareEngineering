s="anagram"
t="nagaram"

import collections

counter= collections.Counter

sl=counter(list(s))
tl=counter(list(t))


print(sl)
print(tl)

if sl== tl:
    print("Good")
