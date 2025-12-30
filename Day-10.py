# python regex
# a regex or regular expression is a sequence of characters that forms a search patterns.
# RegEx can be used to check if a string contains the specified search pattern.
import re

txt = 'the fox jumps over the log'
x = re.search("^the.*log$", txt)
# print(x)

text1 = 'I love python programming'
result = re.search("python", text1)
print(result)

# example 2 

# Character Matching
# a - matches 'a'
# . - any character
# \d - digit (0-9)
# \w - letter, number,underscore
# \s - whitespace
# \d - not digit 


print(re.findall(r"\d", "age 21 and age 45"))
print(re.findall(r"\s", "age 21 and 45"))

# Quantifiers (very important )

# * - 0 or more
# + - 1 or more 
# ? - 0 or 1
# {n} - exactly n
# {n, m} - between n and m 

