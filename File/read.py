f = open("file.txt")
data = f.read()
close = f.close() # always close the file
print(data)
print(close)