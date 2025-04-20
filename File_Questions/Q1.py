file = open("poem.txt","r")
data =file.read()

if("dof" in data):
    print("YEs")
else:
    print("No")

print(data)