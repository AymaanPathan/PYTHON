s = {1,2,[1,2]} #error in set mutable / hashable cannot be stored
validS = {1,2,(1,2)} # right immutable tuple
print(s)