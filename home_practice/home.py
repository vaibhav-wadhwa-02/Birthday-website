n=5
# -------------------------------------
'''
*
**
***
****
***** 
'''
# for i in range(n):
#     for j in range(i):
#         print( "*" , end="")
#     print()
# -------------------------------------
'''
****
***
**
* 
'''
# for i in range(n):
#     for j in range(n-i):
#         print("*", end="")
#     print()

# -------------------------------------
'''
      *
     **
    ***
   ****
  *****
'''
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end = "")
#     for k in range(i+1):
#         print("*",end="")
#     print()
# -------------------------------------
'''
****
 ***
  **
   *
'''
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(n-i-1):
#         print("*", end="")
#     print()
# -------------------------------------
# top hill
#     *
#    ***
#   *****
#  *******
# *********

# for i in range(n):
#     for j in range(n-i):
#       print(" ",end="")
#     for k in range(2*i+1):
#       print("*",end="")
#     print()
# -------------------------------------
# bottom hill
# *********  
#  *******
#   *****
#    ***
#     *
# for i in range(n):
#     for j in range(i):
#       print(" ",end="")
#     for k in range(2*(n-i)-1):
#       print("*", end="")
#     print()

# -------------------------------------
# diamond
#     *
#    ***
#   *****
#  *******
# *********  
#  *******
#   *****
#    ***
#     *

# for i in range(n):
#     for j in range(n-i):
#       print(" ",end="")
#     for k in range(2*i+1):
#       print("*",end="")
#     print()
# for i in range(n):
#     for j in range(i+1):
#       print(" ",end="")
#     for k in range(2*(n-i)-1):
#       print("*", end="")
#     print()










#     *
#    ***
#   *****
#  *******
# *********  
#  *******
#   *****
#    ***
#     *

# for i in range(n):
#   for k in range(n-i):
#     print(" ", end="")
#   for j in range(i+i+1):
#     print("*", end="")
#   print()
# for l in range(n):
#   for m in range(l):
#     print(" ",end="")
#   for n in range():
#     print("*",end="")
#   print()

