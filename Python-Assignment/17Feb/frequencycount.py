s = "hellooh"

result = ""

for ch in dict.fromkeys(s):  
    result += ch + str(s.count(ch))

print(result)