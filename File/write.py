text = "Data from write.py APPEND again"
file = open("mode.txt","w")  
data = file.write(text)
file.close()