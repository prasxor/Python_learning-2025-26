my_list = []

def add(e):
    total_sum = 0
    for i in e:
        total_sum += i
    print(total_sum)
def max(e):
    largest_value=0
    for i in e:
        if largest_value < i:
            largest_value = i
    print(largest_value)
    
def min(e):
    smallest_value=1000000
    for i in e:
        if smallest_value > i:
            smallest_value = i
    print(smallest_value)
def avg(e):
    if not e:
        return 0
    avg_value = sum(e)/len(e)
    print(avg_value)

# def avg(e):
#     sum_value = sum(e)
#     len_value = len(e)
#     avg_value = sum_value/len_value
#     print(avg_value)
#     return avg_value

runAgain = False
while runAgain==False:
    user_input = int(input("Enter the your value:\t"))
    my_list.append(user_input)
    print("your list :",my_list)
    print("Want to see sum,max,min,average, then press 0")
    if(user_input==0):
        break

my_list.pop()
print("your list is", my_list)
add(my_list)
max(my_list)
min(my_list)
avg(my_list)
# print(sum(my_list))