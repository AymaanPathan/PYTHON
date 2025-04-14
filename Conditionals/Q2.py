# Wether a student pass or fail

userName = input("Enter Student Name: ")
marks1 = int(input(f"Enter {userName} 1st Marks Here : "))
marks2 = int(input(f"Enter {userName} 2st Marks Here : "))
marks3 = int(input(f"Enter {userName} 3st Marks Here : "))
marks4 = int(input(f"Enter {userName} 4st Marks Here : "))

total = marks1+marks2+marks3+marks4 

if(marks1 >33 and marks2>33 and marks3>33 and marks4>3 and (marks1+marks2+marks3+marks4) /4 <40):
    print(userName , "is passed marks is ", total ,"/100")
else:
    print(userName , "is failed marks is", total , "100"  )