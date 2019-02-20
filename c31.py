
try:
    hours=int(input("enter the hours"))
    rate=int(input("enter the rate"))
    pay=int(hours*rate)
    print("the pay is ",pay)
except:
    print("enter a numeric value")

