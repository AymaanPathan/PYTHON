def printOneToN(n):
    if(n==0):
        return
    printOneToN(n-1)
    print(n)

printOneToN(7)