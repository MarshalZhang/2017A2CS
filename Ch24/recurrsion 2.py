#Marshal Zhang from S3C3 Option 1
#This is my recurssion2

def groupSum(s, x, t):
    if t==0:
        return True
    if s==len(x):
        return False
    return groupSum(s+1, x, t- x[s]) or groupSum(s+1, x, t)

print(groupSum(0,[2,4,8],0))

def groupSum6(s,x,t):
    if t==0 and s==len(x):
        return True
    if t!=0 and s==len(x):
        return False
    if x[s]==6:
        return groupSum6(s+1, x, t- 6)
    else:
        return groupSum6(s+1, x, t- x[s]) or groupSum(s+1, x, t)

print(groupSum6(0,[1,2,6],3))

def groupNoAdj(s,x,t):
    if t==0:
        return True
    if s==len(x) or s==len(x)+1:
        return False
    return groupNoAdj(s+2, x, t-x[s]) or groupNoAdj(s+1, x, t)

print(groupNoAdj(0, [2, 5, 10, 4], 7) )
        
def groupSum5(s,x,t):
    if t==0:
        return True
    if s==len(x):
        return False
    if x[s]%5==0 and x[s+1]==1:
        return groupSum5(s+1,x, t)
    if x[s]%5==0 and x[s+1]!=1:
        return groupSum5(s+1,x, t-x[s])
    return groupSum5(s+1, x, t- x[s]) or groupSum5(s+1, x, t)
print(groupSum5(0, [2, 5, 1,10,1, 4], 17))

def groupSumClump(s,x,t):
    if t==0:
        return True
    if s==len(x):
        return False
    n=1
    while s+n<len(x) and x[s]==x[s+n]:
        n+=1
    return groupSumClump(s+n,x,t) or groupSumClump(s+n,x,t-n*x[s])
  
print(groupSumClump(0, [2, 4, 4, 8], 14))


def findSum(x):
    if len(x)==0:
        return 0
    return x[0]+findSum(x[1:])
    
    
def splitArray(x):
    t=findSum(x)/2
    return groupSum(0, x, t)

print(splitArray([1,2,2,10,10,1,1]))

def helper(s,x,sum1,sum2):
    if s>= len(x):
        return(sum1==sum2)
    return helper(s+1,x, sum1+x[s],sum2) or helper(s+1,x,sum1,sum2+x[s])

def splitArray2(x):
    return helper(0,x,0,0)

print(splitArray2([1,2,2,10,10,1,1]))

def Odd10helper(s,x,sum1,sum2):
    if s>=len(x):
        return (sum1 %2==1 and sum2 %10==0)
    return Odd10helper(s+1,x,sum1+x[s],sum2) or Odd10helper(s+1,x,sum1, sum2+x[s])
            
    

def splitOdd10(x):
    return Odd10helper(0,x,0,0)

print(splitOdd10([1,2,1,5,5]))

def helper53(s,x,sum5,sum3):
    if s>=len(x):
        return( sum5==sum3)
    if x[s]%5==0:
        return helper53(s+1,x,sum5+x[s],sum3)
    if x[s]%3==0:
        return helper53(s+1,x,sum5,sum3+x[s])
    return helper53(s+1,x,sum5+x[s],sum3) or helper53(s+1,x,sum5,sum3+x[s])

def split53(x):
    return helper53(0,x,0,0)

print(split53([3,5,3,3,3,3,5,5]))
    

