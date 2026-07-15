# arr = [2,3]
# arr = [2]
# arr = [1,2,3,5]


# def missingNum(arr):
#     arr.sort()
#     minValue = arr[0]
#     maxValue = arr[-1]
        
#     if len(arr) == 1:
#             return arr[0]+1
#     elif arr[0] == minValue and arr[1] == maxValue:
#         return maxValue+1
#     else:
#         for i in range(minValue,maxValue+1):
#             if i not in arr:
#                 return i
    

# print(missingNum(arr))


# class Solution:
#     def missingNum(self, arr):
#         arr.sort()
#         minValue = arr[0]
#         maxValue = arr[-1]

#         if len(arr) == 1:
#             return arr[0]+1
#         elif arr[0] == minValue and arr[1] == maxValue:
#             return maxValue+1
#         else:
#             for i in range(minValue,maxValue+1):
#                 if i not in arr:
#                     return i

# actual solution 

arr = [2,3]


def missingNum(arr):
    n =len(arr)+1
    
    expected_value = n*(n+1)//2
    sum_value = sum(arr)
    
    return expected_value - sum_value

print(missingNum(arr))