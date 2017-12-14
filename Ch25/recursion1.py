# Marshal for Option1
# This file is what I have done so far for recursion
def fibonacci(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)
print(fibonacci(6))


def bunnyEars(x):
    if x==0:
        return 0
    else:
        return 2+bunnyEars(x-1)

print(bunnyEars(5))

def bunnyEars2(x):
    if x==0:
        return 0
    elif x%2 ==1:
        return 2 + bunnyEars2(x-1)
    else:
        return 3+bunnyEars2(x-1)

print(bunnyEars2(5))

def triangle(x):
    if x==0:
        return 0
    else:
        return x+ triangle(x-1)
print (triangle(3))

def sumDigits (x):
    if x<10:
        return x
    else:
        return x%10+ sumDigits(x//10)
print (sumDigits (126))

def  count7 (x):
    if x==7:
        return 1
    elif x<10:
        return 0
    else:
        if x%10 ==7:
            return 1+ count7(x//10)
        else:
            return count7(x//10)
    
    
print (count7(7767))

def  count8 (x):
    if x==8:
        return 1
    elif x<10:
        return 0
    else:
        if x%10 ==8 and (x//10)%10==8:
            return 2+ count8(x//10)
        else:
            return count8(x//10)    #not working correctly
    
    
print (count8(8868))

def powerN(x,y):
    if y==1:
        return x
    else:
        return x* powerN(x,y-1)

print(powerN(3,3))

def countX(x):
    if len(x)==1 and x[0]=="x":
        return 1
    elif len(x)==1 and x[0]!="x":
        return 0
    else:
        if x[0]=="x":
            return 1+countX(x[1:])
        else:
            return countX(x[1:])
print (countX("xyxxxy"))
    

def countHi(x):
    if len(x)==1:
        return x
    elif len(x)==2 and x[0]+x[1]=="hi":
        return 1
    elif len(x)==2 and x[0]+x[1]!="hi":
        return 0
    else:
        if x[0]+x[1]=="hi":
            return 1+countHi(x[1:])
        else:
            return countHi(x[1:])
print (countHi("h"))

def changeXY(x):
    if len(x)==1 and x=="x":
        return "y"
    elif len(x)==1 and x!="x":
        return x
    else:
        if x[0]=="x":
            return "y"+changeXY(x[1:])  
        else:
            return x+changeXY(x[1:])
print(changeXY("xxhx"))             #not working correctly

def changePi(x):
    if len(x)==1:
        return x
    elif len(x)==2 and x=="pi":
        return "3.14"
    elif len(x)==2 and x!="pi":
        return x
    else:
        if x[0]+x[1]=="pi":
            return "3.14"+changePi(x[2:])
        else:
            return x[0]+changePi(x[1:])
print(changePi("pihhppii"))

def noX(x):
    if len(x)==1 and x=="x":
        return ""
    elif len(x)==1 and x!="x":
        return x
    else:
        if x[0]=="x":
            return noX(x[1:])
        else:
            return x[0]+noX(x[1:])
        
print (noX("xmenarexxy"))

def array6(x,i):
    if i==len(x)-1 and x[i]==6:
        return True
    elif i==len(x)-1 and x[i]!=6:
        return False
    elif x[i]==6:
        return True
    elif x[i]!=6:
        return array6(x,i+1)

print (array6([1,5,4,6],0))
        
def array11(x,i):
    if i==len(x)-1 and x[i]==11:
        return 1
    elif i==len(x)-1 and x[i]!=11:
        return 0
    elif x[i]==11:
        return 1+array11(x,i+1)
    elif x[i]!=11:
        return array11(x,i+1)

print (array11([11,5,4,6,11],0))

def array220(x,i):
    if i==len(x)-2 and x[i+1]== 10* x[i]:
        return True
    elif i==len(x)-2 and x[i+1]!= 10*x[i]:
        return False
    else:
        if x[i+1]== 10*x[i]:
            return True
        else:
            return array220(x,i+1)

print (array220([1,5,5,14,14],0))

def allStar(x):
    if len(x)==1:
        return x
    else:
        return x[0]+"*"+allStar(x[1:])

print (allStar("Marshal"))

def pairStar(x):
    if len(x)==1:
        return x
    else:
        if x[0]==x[1]:
            return x[0]+"*"+pairStar(x[1:])
        else:
            return x[0]+pairStar(x[1:])

print (pairStar("Marrshal"))

def endX(x):
    if len(x)==1:
        return x
    else:
        if x[0]=="x":
            return endX(x[1:])+"x"
        else:
            return x[0]+endX(x[1:])

print(endX("maxshal"))

def countPairs(x):
    if len(x)<3:
        return 0
    else:
        if x[0]==x[2] and x[1]=="x":
            return 1+ countPairs(x[1:])
        else:
            return countPairs(x[1:])

print(countPairs("aaxaxbxbxb"))

def countAbc(x):
    if len(x)<3:
        return 0
    else:
        if x[0:3]=="abc" or x[0:3]=="aba":
            return 1+ countAbc(x[2:])
        else:
            return countAbc(x[1:])
print(countAbc("abcbababc"))

###############

    
def count11(x):
    if len(x)<=1:
        return  0
    elif len(x)>=2 and x[-2]=='1' and x[-1]=='1':
        return count11(x[:-2])+1
    else:
        return count11(x[:-1])

print(count11('11bc1a111dc'))

def stringclean(x):
    if len(x)<=2:
        return x[0]
    if x[-1]==x[-2] and x[-1]==x[-3]:
        return stringclean(x[:-3])+x[-1]
    elif x[-1]==x[-2]:
        return stringclean(x[:-2])+x[-1]
    else:
        return stringclean(x[:-1])+x[-1]

print(stringclean('cxnceii'))

def countHi2(n):
    if len(n)<2:
        return 0
    if len(n)==2 and n[-1]=='i' and n[-2]=='h':
        return 1
    if n[-1]=='i' and n[-2]=='h' and n[-3]!='x':
        return 1+countHi2(n[:-1])
    else:
        return countHi2(n[:-1])
    
print(countHi2('hiiahixhihi'))

def parenBit(n):
    if n=='':
        return ''
    if n[0]!='(':
        return parenBit(n[1:])
    if n[-1]!=')':
        return parenBit(n[:-1])
    else:
        return n
    
print(parenBit('chen(ke)wei'))

def nextparen(n):
    if n=='':
        return True
    if n[0]=='(' and n[-1]==')':
        return nextparen(n[1:-1])
    else:
        return False
    
print(nextparen('(()))'))

def strCount(n,sub):
    if len(n) < len(sub):
        return 0
    if n[0:len(sub)]==sub:
        return 1+strCount(n[1:],sub)
    else:
        return strCount(n[1:],sub)

def nextparen(n):
    if n=='':
        return True
    if n[0]=='(' and n[-1]==')':
        return nextparen(n[1:-1])
    else:
        return False
    
print(nextparen('(()))'))

def strCount(n,sub):
    if len(n) < len(sub):
        return 0
    if n[0:len(sub)]==sub:
        return 1+strCount(n[1:],sub)
    else:
        return strCount(n[1:],sub)

print(strCount('ckwwwwwckw','ckw'))

def strCopies(n,sub,count):
    if len(n) < len(sub):
        if count==0:
            return True
        else:
            return False
    if n[0:len(sub)]==sub:
        return strCopies(n[1:],sub,count-1)
    else:
        return strCopies(n[1:],sub,count)

print(strCopies('ckwwwwckw','ckw',2))

def strDist(n,sub):
    
    
    if n[-len(sub):] != sub:
        return strDist(n[:-1], sub)
    if n[0:len(sub)] != sub:
        return strDist(n[1:], sub)
    else:
        return len(n)

print(strDist('cckwwwwckwei','ckw'))

    


    
