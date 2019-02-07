

def addfrac(f1,f2):
  d={}
  d["denum"]=f1[1]*f2[1]
  d["num"]=(f1[0]*f2[1])+(f2[0]*f1[1])
  return d

print(addfrac((1,2),(1,3)))
