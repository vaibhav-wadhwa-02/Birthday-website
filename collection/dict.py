# keys are immutable and unique
# Unordered
# Efficient Access: Dictionaries use a hash table implementation
# Heterogeneous Data:

# INITIALIZATION
# dict = {}
# mydict = dict([(1,'vaibhav'),(2,"mohan")])
# print(mydict["Name"])                 #error if no value found
# print(mydict.get("Name"))             #None for no value

'''
 Dictionary Methods
# clear
# copy
# fromkeys
# get
# items
# keys
# pop
# popitem
# setdefault
# update
# values
'''


# UPDATION
# mydict["Age"] = 22 
# mydict["City"] = "rajpura"            #Adding key pair
# del mydict["Age"]                     #Delection of a single pair
# del mydict                            #Deletion of the 
# mydict.pop("Word")                    #Removes the particular item
# mydict.popitem()                      #Removes the last item
# mydict.clear()                        #Removes all elements

# ACCESSING THE DICT
# print(mydict.keys())                  #Returns the keys only
# print(mydict.values())                #Returns the values only
# print(mydict.items())                 #
# mydict3 = mydict.copy()               #Copy all the values in the new dictionary
# mydict.update(mydict2)                #Concadinate all the values to a dict

#   DOUBT
# keys = [1,2,3]
# values = ["vaibhav","rohan","mohan"] 
# mydict3 = dict.fromkeys(keys,"default_value")
# mydict.setdefault("age",18)

# print(mydict)

# for i in mydict.values():
#     print(i)

# for keys,values in mydict.items():
#     print(keys,values)

# x=1
# sqa = {x:x**2 for x in range(2,10)}
# print(sqa)

# mydict={
#     "person1":{"Name":"vaibhav", "Age" : 21},
#     "person2":{"Name":"mohan", "Age" : 27}
# }
# print(mydict['person1'])

# union
# mydict =  {"Word":"meaning","Name":"vaibhav", "Age" : 21}
# mydict2 ={"Roll number":"2310987127","Course":"BCA-MCA"}
# print(mydict|mydict2)

# # print only common values from two dictionaries 
# mydict =  {"Word":"meaning","Name":"vaibhav", "Age" : 21}
# mydict1 =  {"Word":"Meaning","Name":"vaibhav", "Age" : 27}
# values = set(mydict.values())
# values1 = set(mydict1.values())
# print(values.intersection(values1))
# print(values.intersection(values1))

# mydict1 =  {"Word":"Meaning","Name":"vaibhav", "Age" : 27}

# mydict =  {"Word":"meaning","Name":"vaibhav", "Age" : 21}
# def exist(a):
#     if a in mydict.items():
#         print(True)
#     else:
#         print(False)
        
# exist(a = tuple(map(input("Enter key and value with space : ").split(" "))))


# mydict =  {"Word":"meaning","Name":"vaibhav", "Age" : 21}
# if ("Name","vaibhav") in mydict.items():
#     print(True)
# else:
#     print(False)
    
    
# var = set([1,2,3])
# var1 =set([3,4,5])
# var2 = set([])
# var2 = var.intersection(var1)
# print(var2)


# d2 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# all()  checks if all values in the dictionary evaluate to  True  . 
# any()  checks if any value in the dictionary evaluates to  True  . 
# cmp()  (no longer available in Python 3) used to compare two dictionaries. 
# sorted()  returns a new sorted list of keys in the dictionary. 
# my_dict = {"C": 10, "H": 20, "A": 0}
# print(all(my_dict.values()))   # False (0 evaluates to False)
# print(any(my_dict.values()))   # True (at least one value is True)
# print(sorted(my_dict))         # [‘A’, ‘B’, ‘C’] (sorted keys)

# Initialize an empty dictionary
# D = {} 

# L = [['a', 1], ['b', 2], ['a', 3], ['c', 4]]

# for i in range(len(L)):
# 	if L[i][0] in D:
# 		D[L[i][0]].append(L[i][1])
	
	# If the key is not present
	# in the dictionary then add
	# the key-value pair
# 	else:
# 		D[L[i][0]]= []
# 		D[L[i][0]].append(L[i][1])
		
# print(D)


