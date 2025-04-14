# detect spam
spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

message = input("Enter your msg : ")

if(spam1 in message or spam2 in message or spam3 or message or spam4 in message):
    print("Yes its a spam")
else:
    print("No its not a spam")