# userInput = "aaabbc"

# dict_freq = {}
# result_str = ""

# for char in userInput:
#     if char in dict_freq:
#         dict_freq[char] +=1
#     else:
#         dict_freq[char] = 1

# # print(dict_freq)

# for k,v in dict_freq.items():
#     result_str += k + str(v)
    
# print(result_str)

# userInput = "aaabbc"

# dict_freq = {}
# result_str = ""

# for char in userInput:
#     if char in dict_freq:
#         dict_freq[char] +=1
#     else:
#         dict_freq[char] = 1

# # print(dict_freq)

# for k,v in dict_freq.items():
#     result_str += str(v) + k
    
# print(result_str)



# max repeated char
userInput = "aaabcccbc"

dict_freq = {}

freq = {}
result_str = ""

for char in userInput:
    if char in dict_freq:
        dict_freq[char] +=1
    else:
        dict_freq[char] = 1
    # dict_freq[char] += 1 if char in (dict_freq) else dict_freq[char] = 1
        
max_var,key= float("-inf"),None
# print(dict_freq)
for k,v in dict_freq.items():
    if dict_freq[k] > max_var:
        max_var,key = dict_freq[k], k
        # print(dict_freq[k])
        # key = k
        
        
print(key)
    