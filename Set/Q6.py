# This will update the dictnory and also overrides if same key 
frnd = {}
for i in range(2):
    userName = input(f"Enter Name here : ")
    userLan = input(f"Enter {userName}'s  fav here : ")
    frnd.update({userName:userLan})

print(frnd)