# Enter the number greater than zero
n = int(input("Enter the no.:"))



"""
If you you enter boolean 0 it prints pattern like(if n=3)
***
**
* 

but if you enter boolean 1 it prints pattern
*
**
***
"""
print("Enter the boolean:-",
              "0-False",
              "1-True")

b = int(input())
if b==1:
    for i in range(n):
        for i in range(i+1):
            print("*", end="")
        print()
else:
    for i in range(n):
        for i in range(n-i):
            print("*",end="")
        print()