x=f()
def f():
    a=10
    def g():
        a+=1
        return a
    return g
print(x)
