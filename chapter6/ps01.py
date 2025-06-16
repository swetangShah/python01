a1 = int(input("enter number 1: "))
a2 = int(input("enter number 2: "))
a3 = int(input("enter number 3: "))
a4 = int(input("enter number 4: "))

if(a1 > a2 and a1 > a3 and a1 > a4):
    print("Number 1 is the largest")

elif(a2 > a1 and a2 > a3 and a2 > a4):
    print("Number 2 is the largest")

elif(a3 > a1 and a3 > a2 and a3 > a4):    
    print("Number 3 is the largest")

elif(a4 > a1 and a4 > a2 and a4 > a3):      
    print("Number 4 is the largest")
