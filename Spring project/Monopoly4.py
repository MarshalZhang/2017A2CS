#Marshal Zhange from S3C3 Option 1
# This is my code for "Monopoly"

import random
from random import shuffle
class ListNode :
   def __init__(self) :
      self.who= 0
      self.pointer=0
      self.whose =0
      self.cost = 0
      self.previouspointer=0
class Perinfor:
   def __init__(self):          # Init the map
      self.who= 0
      self.position=0
      self.money =sm
      self.pointer =0
      self.previouspointer =0

def initilise():
    global List
    global sm
    global np
    global Char
    global nh
    print("Welcome to the game created by Marshal, a simple rule:1 for yes，0 for no")
    np=int(input("Pleas choose the number of players:"))  #np: number of players
    sm=int(input("please enter the init money you wish to have:"))  #sm: starting money
    nh=int(input("please enter the number of house in the map:")) #nh: number of houses
    List = [ListNode() for i in range(nh)]  # Generate a list for the map
    for i in range(nh) :
       List[i].pointer = i + 1
       List[i].previouspointer = i-1
       List[i].cost =random.randint(30,200)
    List[nh-1].pointer=0
    List[0].previouspointer=nh-1

    Char = [Perinfor() for i in range(np)]    
    for i in range(np):
       Char[i].who=i+1
    #shuffle a list to generate random position for players
    l = list(range(0,nh))
    shuffle(l)
    for i in range(np):
        Char[i].position = l[i]
        Char[i].pointer = i+2
        Char[i].previouspointer =i
        List[l[i]].who=i+1
        List[List[l[i]].previouspointer].pointer=List[l[i]].pointer
        List[List[l[i]].pointer].previouspointer=List[l[i]].previouspointer
    Char[0].previouspointer = np
    Char[np-1].pointer=1
    # for lucky and bad luck
    List[l[nh-1]].whose="good luck"
    List[l[nh-2]].whose="bad  luck"
    List[l[nh-1]].cost=""
    List[l[nh-2]].cost=""


def Lucky(p):
    l=random.randint(1,3)
    if l==1:
       print("you get an extra monney of 1000 dollars")
       Char[p-1].money +=1000
    if l==2:
        print("you get the luck to destory one builing")
        d=int(input("Please choose the position of the place where you want to destroy"))
        List[d].whose=0
    if l==3:
        print("you get the luck to move 2 more steps")
        p=3-p

def Unlucky(p):
    l=random.randint(1,3)
    if l==1:
        print("your money is taken by Marshal, you lost 700 dollars")
        Char[p-1].money-=700
    if l==2:
        print("you have to pay Marshal 10 rmb in order to continue the game")
        print("please ask Marshal to enter the password after the payment")
        password=int(input("Password:"))
        if password!="123":
            print("sorry")
        
            
    if l==3:
        print("Yesterday, a thief came to your house and steal all you money ")
        Char[p-1].money=0
    
       
def playergo(p):
    w=Char[p-1].position     # shortcut for the position of the current player
    r=random.randint(1,6)
    rr=random.randint(1,6)
    print("It's player",p,"'s turn")
    ndice=int(input("please choose the number of dice you want to throw 1 or 2:"))
    if ndice==1:
        n=r
    if ndice==2:
        n=r+rr
    print("The number of steps that you go is:",n)
    x=0   # Count the number of time that we go through
    while List[w].who==p and x!=n:
         List[w].who = 0
         w=List[w].pointer
         List[w].who=p

         x+=1
    Char[p-1].position=w
    if List[w].whose==0:
        buy(p)
    elif p==List[w].whose:
        upgrade(p)
    elif List[w].whose=="good luck":
        Lucky(p)
    elif List[w].whose=="bad  luck":
        Unlucky(p)
    elif p!=List[w].whose:
        pay(p, List[w].whose)
    
def Output():
    for i in range(nh):
        print(i, List[i].who, List[i].whose, List[i].cost)
    print("")
    for i in range(np):
        print(i+1, Char[i].position, Char[i].money,Char[i].previouspointer, Char[i].pointer)

def buy(p):
    cost=List[Char[p-1].position].cost
    print("this house is empty, do you want to buy it for:",cost,"dollars?")
    option=int(input("yes or no?"))
    if option==1:
        Char[p-1].money-= cost
        List[Char[p-1].position].whose=p

def upgrade(p):
    print("You have already bought it, Do you want to ungrade it for 77 dollars?")
    print("After unpgrading, the rent will double")
    Option=int(input("please enter your choice:"))
    if Option==1:
            Char[p-1].money-=77
            List[Char[p-1].position].cost*=2

def pay(p,r):
    c=List[Char[p-1].position].cost   #shortcut for the cost at that location
    Char[p-1].money  -=c
    Char[r-1].money  +=c
    print("You have stepped onto the other player's area, you have to pay",c,"dollars") 

initilise()
Output()
p=1
def checkwin():
    x=np
    for i in range(np):
        if Char[i].money <0:
            print("Player", i+1, "has no money left, his houses are now free to buy")
            Char[Char[i].previouspointer].pointer= Char[i].pointer   #remove the player
            Char[Char[i].pointer].previouspointer= Char[i].previouspointer
            for j in range(nh):
                if List[j].who==i+1:
                    List[j].who==0
                if List[j].whose==i+1:
                    List[j].whose=0    #make all his houses free
        if Char[i].pointer==Char[i].who:
            print("Player", i+1,"is the winner")
            Onlyoneleft=True
        
                
StartPointer=0
Onlyoneleft=False
while Onlyoneleft==False:   #only for 2 playrs now
    playergo(p)
    p=Char[p-1].pointer
    Output()
    checkwin()
    
        
