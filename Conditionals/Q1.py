# Find the largest
num1 = int(input(f"Enter 1st Number : "))
num2 = int(input(f"Enter 2nd Number : "))
num3 = int(input(f"Enter 3rd Number : "))
num4 = int(input(f"Enter 4th Number : "))

if(num1 >num2 and num1>num3 and num1>num4):
    print(num1 , "Is Largest")
elif(num2 > num1 and num2>num3 and num2>num4):
    print(num2 , "Is Largest")
elif(num3 > num2 and num3>num2 and num3>num4):
    print(num3 , "Is Largest")
elif(num4 > num1 and num4>num2 and num4>num3):
    print(num4 , "Is Largest")