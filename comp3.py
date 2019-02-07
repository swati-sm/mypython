
def compare(a,b,c):
    if(a<b & a<c):
        return a
    elif(b<c & b<a):
        return b
    else:
        return c
print(compare(3,2,4))

