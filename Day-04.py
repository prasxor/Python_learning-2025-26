# sort lists 
mylist =[1,12,3,4,5,6]
mylist.sort()
print(mylist)

my_Another_list = ['banana', 'Bano', 'apple', 'Aplle']
my_Another_list.sort()
print(my_Another_list)

my_Another_list1 = ['banana', 'Bano', 'apple', 'Aplle']
my_Another_list1.sort(key=str.lower)
print(my_Another_list1)

#reverse()
my_Another_list.reverse()
print(my_Another_list)
mylist.reverse()
print(mylist)

#list Comprehension

newList = [x for x in my_Another_list1 if "b" in x]
print(newList)

# list copy 
mynewList = [12,2,3,4,2,3,4,3,2]
empty_list = mynewList.copy()
print(empty_list)
empty2_list = list(mynewList)
print(empty2_list)
empty3_list = mynewList[:]
print(empty3_list)  

#list extend
list1 = [1,23,4,5,6]
list2 = ['a','b','c']

# for i in list2:
#     list1.append(i)
    
# print(list1)

# or using extend

list1.extend(list2)
print(list1)


# list methods 
# append()
# clear()
# copy()
# count()
# extend()
# index()
# insert()
# pop()
# remove()
# reverse()
# sort()