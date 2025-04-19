def greatest(num1,num2,num3):
    if(num1 >num2 and num1>num3):
        print(f"num1: {num1} is Greatest")
    elif(num2>num1 and num2>num3 ):
        print(f"num2: {num2} is Greatest")
    else:
        print(f"num3: {num3} is Greatest")


num1 = 23
num2= 12
num3 = 1

greatest(num1,num2,num3)