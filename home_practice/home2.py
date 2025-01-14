n=5
# -------------------------------------
'''
1
22
333
4444
55555
'''
# for i in range(n+1):
#     for j in range(1,i+1):
#         print( i , end="")
#     print()

'''
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''
# num=0
# for i in range(n+1,0,-1):
#     num +=1
#     for j in range(i-1):
#         print(num, end="")
#     print()

'''
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5
'''

# for i in range(n):
#     for j in range(n-i):
#         print(n,end="")
#     print()

'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
# for i in range(n):
#     for j in range(n-i):
#         print(i+j+1,end="")
#     print()

'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''

# for i in range(n):
#     for j in range(i+1):
#         print(i-j+1,end="")
#     print()

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="")
#     print()

'''
0
0 1
0 2 4
0 3 6 9
0 4 8 12 16
'''
# for i in range(n):
#     for j in range(i+1):
#         print(j*i, end=" ")
#     print()

'''
1
3 3
5 5 5
7 7 7 7
9 9 9 9 9
''' 
# for i in range(n):
#     for j in range(i+1): 
#         print(i+i+1, end=" ")
#     print()

'''
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1

'''
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     for k in range(i):
#         print(i-k,end=" ")
#     print()
