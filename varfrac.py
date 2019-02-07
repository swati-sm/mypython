f1=[1,2]
f2=[1,3]
def addfrac(f1,f2):
    denum=f1[1]*f2[1]
    num=(f1[0]*f2[1])+(f2[0]*f1[1])
    return (num,denum)
print(addfrac(f1,f2))
