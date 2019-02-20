def fibo():
    a,b=0,1
    yield a
    yield b
    for i in range(20):
        ans=a+b
        a,b=b,ans
        yield ans

x=fibo()

for i in x:
    print(i)


