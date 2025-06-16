marks1 = int(input("Enter marks for student 1: "))
marks2 = int(input("Enter marks for student 2: "))
marks3 = int(input("Enter marks for student 3: "))

total_percentage = (marks1 + marks2 + marks3) / 300

if(total_percentage >= 40):
    print("you are pass")

else:
    print("you are fail, please try again") 
