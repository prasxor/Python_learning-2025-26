# we need to count the upper case , lower case, digit, special case 


txt = "ABcd@1$z"

upperCount,LowerCount,DigitCount,specialCount = 0,0,0,0

s = 0

while s <= (len(txt) - 1):
    char = txt[s]

    if 'A' <= char <= 'Z':
        upperCount += 1
    elif 'a' <= char <= 'z':
        LowerCount += 1
    elif '0' <= char <= '9':
        DigitCount += 1
    else:
        specialCount += 1

    s += 1

print("count of UpperCase:", upperCount)
print("count of Lowercase:", LowerCount)
print("count of Digits:", DigitCount)
print("count of Special Characters:", specialCount)


# assignment : 
# 1. find out the no of primitive and non - primitive
l = [1,3.4,"hi", {"hi", "bye"}, 3+5j]