# Count the frequency of each character in a given string
from collections import Counter
string = "banana"
freq = {}
# counts = Counter(string)
# print(counts)

# or solution 

for ind in string:
    if ind in freq:
        freq[ind] += 1
    else:
        freq[ind] = 1
        
print(freq)        
