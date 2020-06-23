a = int(input("Enter the 1st no.:"))
op = input("Enter the operator:")
b = int(input("Enter the 2nd no.:"))
"""
Create faulty calculator
45*3=555
56/6=4
56+9=77
"""
if a==45 and op=='*' and b==3:
    print(555)
elif a==56 and op=='+' and b==9:
    print(77)
elif a==56 and op=='/' and b==6:
    print(4)
else:
    if op=='+':
        print(a+b)
    elif op=='-':
        if a>b:
            print(a-b)
        else:
            print(b-a)
    elif op=='*':
        print(a*b)
    else:
        print(a/b)





