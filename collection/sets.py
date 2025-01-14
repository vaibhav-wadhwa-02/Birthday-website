# SETS

# Unordered:
# Unique:
# Mutable:  you can add or remove elements.
# Immutable Elements: The elements within a set must be of an immutable
'''
Methods
# add
# clear
# copy
# difference
# difference_update
# discard
# intersection
# intersection_update
# isdisjoint
# issubset
# issuperset
# pop
# remove
# symmetric_difference
# symmetric_difference_update
# union
# update
'''
# 1 Sets are initialised as set()
# 2 sets have no indexing
# 3 sets elements are not mutable but we can add or remove elements
# 4 we can store list, tuple and dict in sets
# 5 functions
# myset1 = {1,2,3,5,6,7,8,9}
# myset2 = {11,8,13,14,2}
# myset.add()
# myset.pop() #removes the smallest element
# myset1.update(myset2)
# myset1.remove(oneArgument)  # throws error if the element is not available
# myset1.discard(oneArgument) # doesn't throws error if the element is not available
# myset1.clear()
# del myset1
# union myset1|myset2  or myset1.union(myset2) #used to combine the new sets
# intersection myset1.intersection(myset2)
# symmyteric difference ^ myset1.symmetric_difference(myset2) #doesn't returns the common elements
# frozen sets frozenset([10,20,30]) #frozenset(()) frozenset({}) immutable sets

'''
myset1 = {1,2,3,5,6,7,8,9}
myset2 = {11,8,13,14,2}
list1 = [1,2,3,4,5,6,1,2,3]
myset3 = set(list1)
# print(myset1)
myset1.pop()
print(myset1)
myset1.pop()
print(myset1)
myset1.pop()
print(myset1)
'''