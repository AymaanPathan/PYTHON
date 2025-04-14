# display unique number that user input (take 8 numbers from user)
uniqueNumber = set()
for i in range(8):
    user = int(input(f"Enter your {i+1} number here "))
    uniqueNumber.add(user)

print(uniqueNumber)