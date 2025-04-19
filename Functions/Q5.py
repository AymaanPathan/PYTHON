l = ["chair","pen","table","Ac"]
def replaceWord(word):
    if(word not in l ):
        print(word ,"is Not Present on List")
        return
    else:   
        for i in l:
            if(word in l ):
                l.remove(word)

    print(f"From {l}, {word} is Removed ")

replaceWord("pen")