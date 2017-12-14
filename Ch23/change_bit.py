def testbit(x,bitnumber):
    y= x>>bitnumber
    if y%2==1:
        print("true")
    if y%2==0:
        print("false")
def setbit(x,bitnumber):
    y= x>>bitnumber
    if y%2==1:
        print(x)
    if y%2==0:
        print(x+2**5(bitnumber))
def clearbit(x,bitnumber):
    y= x>>bitnumber
    if y%2==0:
        print(x)
    if y%2==1:
        print(x-2**(bitnumber))
def togglebit(x,bitnumber):
    y= x>>bitnumber
    if y%2==0:
        print(x+2**(bitnumber))
    if y%2==1:
        print(x-2**(bitnumber))
x=int(input("Enter the number:"))
bitnumber=int(input("Enter the bit number:"))



    
