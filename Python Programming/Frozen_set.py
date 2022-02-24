# we can not moified

set = {11, 22, 33, 44, 55}
print(type(set))

# convertint in frozen set

fs = frozenset(set)
print(type(fs))
print("Frozen Set : ",fs)