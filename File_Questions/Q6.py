file1 = open("file1.txt")
file2 = open("file2.txt")

data1 = file1.read()

data2 = file2.read()

if(data1==data2):
    print("yes both file content is same")
else:
    print("No Both files are different ")