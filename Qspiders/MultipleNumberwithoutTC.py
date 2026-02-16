"""
Question:
Given a number, find the product of its digits without using typecasting.
Example:
Input  : 134
Output : 12   (1 * 3 * 4)
"""

x = 516
last = 0
res = 1

while x>0:
    last = x%10
    res = res * last
    x = x//10
    
print(res)