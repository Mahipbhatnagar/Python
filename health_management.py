#This getdate function to enroll the real-time for entry
def getdate():
    import datetime
    return datetime.datetime.now()

"""
This log function helps to build/create the file
for excercise and food for the person and also helps to
append the data to the file.
"""
def log(k):
    if k == 1:
        c = int(input("Enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("mahip-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("mahip-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    elif (k == 2):
        c = int(input("Enter 1 for excersise and 2 for food:"))
        if (c == 1):
            value = input("type here\n")
            with open("keshav-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("keshav-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    elif (k == 3):
        c = int(input("Enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("sid-ex.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("sid-food.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully written")
    else:
        print("Please enter valid input (1(Mahip),2(Keshav),3(Sid)")

"""
This function helps to retrive or read the data 
for the particular values of the files
"""
def retrive(k):
    if k==1:
        c=int(input("Enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("mahip-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("mahip-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("Enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("keshav-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("keshav-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("Enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("sid-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("sid-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter valid input (Mahip,Keshav,Sid)")



#Main program
print("\"Health Management System\"")
print("What you want log or retrive?\n",
      "Press 1 for Log\n",
      "Press 2 for Retrive")
inp = int(input("Press the key:"))
print("For which person?\n",
      "Press 1 for Mahip\n",
      "Press 2 for Keshav\n",
      "Press 3 for Sid")
p = int(input("Press the key:"))
if inp == 1:
    log(p)
elif inp ==2 :
    retrive(p)
else:
    print("Enter the valid number for 1-Log and 2-Retrive")