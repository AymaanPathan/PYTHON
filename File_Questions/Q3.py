file = open("donkey.txt")
data = file.read()
file.close()
print(data)
if("donkey" in data):
   data = data.replace("donkey","####")
print(data)

file = open("donkey.txt","w")
file.write(data)
file.close()