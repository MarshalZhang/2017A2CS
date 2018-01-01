#Marshal Zhange from S3C3
# This is my code for "Monopoly"

import random
class ListNode :
   def __init__(self) :
      self.who= 0
      self.pointer=0
      self.whose =0
      self.cost = 0

List = [ListNode() for i in range(10)]
for i in range(10) :
    List[i].pointer = i + 1
    List[i].cost =random.randint(30,200)

List[9].pointer=0

a=random.randint(1,9) # The position of player1
b=random.randint(1,9) # The position of player2

List[a].who=1
List[b].who=2


print("Welcome to the game created by Marshal, a simple rule:1 for yes 0 for no")
print("1 for 1000, 2 for 3000, 3 for 10000, 4 for DIY")
option= int(input("choose the amount of money you want to have at first:"))
if option ==1:
    ma= 1000          #Money of Player1
    mb= 1000          #Money of Player2
if option ==2:
    ma= 3000
    mb= 3000
if option ==3:
    ma= 10000
    mb= 10000
if option ==4:
    ma = mb= int(input("please enter the init money you wish to have:"))

    
    
def playergo(p):
    global a
    global b
    global ma
    global mb
    r=random.randint(1,6)
    rr=random.randint(1,6)
    print("It's player",p,"'s turn")
    ndice=int(input("please choose the number of dice you want to throw 1 or 2:"))
    if ndice==1:
        n=r
    if ndice==2:
        n=r+rr
    print("The number of steps that you go is:",n)
    x=0
    if p==1:
        while List[a].who==p and x!=n:
            List[a].who=0
            if List[List[a].pointer].who==3-p:
                a=List[List[a].pointer].pointer
                List[a].who=p

            else:
                a=List[a].pointer
                List[a].who=p
            x+=1
        if List[a].whose==0:
            buy(p)
        elif List[a].whose==p:
            upgrade(p)
        elif List[a].whose==3-p:
            pay(p)
    if p==2:
        while List[b].who==p and x!=n:
            List[b].who=0
            if List[List[b].pointer].who==3-p:
                b=List[List[b].pointer].pointer
                List[b].who=p

            else:
                b=List[b].pointer
                List[b].who=p
            x+=1
        if List[b].whose==0:
            buy(p)
        elif List[b].whose==p:
            upgrade(p)
        elif List[b].whose==3-p:
            pay(p)
    

def buy(p):
    global a
    global b
    global ma
    global mb
    if p==1:
        cost=List[a].cost
        print("this house is empty, do you want to buy it for:",cost,"dollars?")
        option=int(input("yes or no?"))
        if option==1:
            ma-= cost
            List[a].whose=p
    if p==2:
        cost=List[b].cost
        print("this house is empty, do you want to buy it for:",cost,"dollars?")
        option=int(input("yes or no?"))
        if option==1:
            mb-= cost
            List[b].whose=p

def Lucky():
    
    
def Output():
    for i in range(10):
        print(i, List[i].who, List[i].whose, List[i].cost)
    print("player1 has", ma, "dollars")
    print("player2 has", mb, "dollars")
    if ma<0:
        print("player2
              is the winner, with", mb, "dollars")
    if mb<0:
        print("player1 is the winner, with", ma, "dollars")
        

def upgrade(p):
    global a
    global b
    global ma
    global mb
    print("You have already bought it, Do you want to ungrade it for 77 dollars?")
    print("After unpgrading, the rent will double")
    Option=int(input("please enter your choice:"))
    if Option==1:
        if p==1:
            ma-=77
            List[a].cost*=2
        if p==2:
            mb-=77
            List[b].cost*=2
def pay(p):
    global a
    global b
    global ma
    global mb
    if p==1:
        c=List[a].cost
        ma-=c
        mb+=c
        print("You have stepped onto the other player's area, you have to pay",c,"dollars") 
    if p==2:
        c=List[b].cost
        mb-=c
        ma+=c
        print("You have stepped onto the other player's area, you have to pay",c,"dollars")
        
        
Output()
p=1
while ma>0 and mb>0:
    playergo(p)
    p=3-p
    Output()
        
