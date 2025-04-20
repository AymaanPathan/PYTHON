def game():
    userHighScore = input("Enter Your Score: ")
    file = open("high_Score.txt","r")
    data = file.read()
    fileWrite = open("high_Score.txt","w")
    if(data==""):
        fileWrite.write(userHighScore)
    elif(int(data) <int(userHighScore)):
        fileWrite.write(userHighScore)
        print("You Beat The High Score")
    else:
        print("You Did't Bead The High Score")




game()