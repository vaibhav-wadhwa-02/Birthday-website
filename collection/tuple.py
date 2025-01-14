# tuple 
'''
Tuple Methods
# count
# index
'''

# They are indexed.
# Tuples are ordered.
# These are immutable.
# They can contain duplicate items.

# my_tuple = (10, 20, 30, 20, 40, 20)
# tuplecount = my_tuple.count(20)  # Output: 3
# tupleindex = my_tuple.index(30)  # Output: 2
# tuplelength = len(my_tuple)  # Output: 6
# tupleexists = 20 in my_tuple  # Output: True
# tupleelement = my_tuple[1]  # Output: 20
# tuplesliced = my_tuple[1:4]  # Output: (20, 30, 20)
# new_tuple = my_tuple + (50, 60)  # Output: (10, 20, 30, 20, 40, 20, 50, 60)
# tuplemax = max(my_tuple)  # Output: 40
# tuplemin = min(my_tuple)  # Output: 10
# tuplesum = sum(my_tuple)  # Output: 140


# my_tuple = (10, 20, 30, 20, 40, 20)
# # del my_tuple
# # mylist = list[my_tuple]
# # print(type(mylist))
# l
# mylist = list(my_tuple)

# set = {1,2,3}
# print(type(set))

# list1 = [1,2,3,4,5]
# list2 = [10,20,30,40]

# newlist1 = list1 + list2
# print(newlist1)
# newlist2 = list.extend(list2)
# print(newlist2)

# string = "Welcome to bebo, technologies"
# str = string.split(",")
# print(str)

# tuple1 = tuple(map(int,input("Enter 5 numbers more than 10 : ").split(" ")))
# print(tuple1)

# tuple2 = tuple(map(int,input('Enter : ').split(",")))
# print(tuple2)

# float to int
# floatvariable = 89.9
# integervariable = int(floatvariable)
# print(integervariable)


# list = [10,40,60,90,20,70,30,40,40]
# list.sort(reverse=True)
# print(list.count(40))
# print(list)


# import string
# var = "aabbcccc"
# newvar = ""
# count = 1
# for i in range(1,len(var)):
#     if var[i] == var[i-1]:
#         count+=1
#     else:
#         newvar += var[i-1] + str(count)
#         count = 1
        
# newvar += var[-1] + str(count)
# print(newvar)

# a = "fizz"
# b = "buzz"
# c = "fizzbuzz"
# for i in range(1,20):
#     if i%3==0 and i%5==0:
#         print(c)
#     elif i%3==0:
#         print(a)
#     elif i%5==0:
#         print(b)
#     else:
#         print(i)
        
# d = int(input("Enter the number : "))
# if i%3==0 and i%5==0:
#     print(c)
# elif i%3==0:
#     print(a)
# elif i%5==0:
#     print(b)
# else:
#     print(d)
    
# sum of digits
# list = [10,20,30,40,50]
# sum = 0
# for i in range(len(list)):
#     sum = sum+ list[i] 
# print(sum)

# duplicates

# list = [0,0,0,1,1,2,2,2,3,4,5]
# i = 1
# while i < len(list):
#     if list[i] == list[i-1]:
#         list.pop(i)
#         i-=1
#     i+=1
# print(list)