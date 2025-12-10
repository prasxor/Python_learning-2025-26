my_list = []

def sum(e):
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
    smallest_value=0
    for i in e:
        if smallest_value > i:
            smallest_value = i
    print(smallest_value)
# def avg(e):
#     return avg(e)

user_input = int(input("Enter the your value:\t"))
runAgain = False
if user_input == 00:
    runAgain=True
while runAgain==True:
    print("Want to see sum,max,min,average, then press 00")
    my_list.append(user_input)
    if(user_input==00):
        print("your list :",my_list)
        break

print("your list is", my_list)
sum(my_list)
max(my_list)
min(my_list)
# avg(my_list)
# print(sum(my_list))