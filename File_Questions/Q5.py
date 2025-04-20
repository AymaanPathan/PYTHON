censoredWords = ["im" ,"aymaan"]
file = open("censored.txt")
data = file.read()
file.close()
ans = ""

for i in censoredWords:
    if(i in data):
        data = data.replace(i,"####")

file = open("censored.txt","w")
data = file.write(data)
file.close()