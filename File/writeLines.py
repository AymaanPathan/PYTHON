lines = ["line1","line2","line3","line4"]
file = open("file.txt","w")
file.writelines(lines)
file.close()