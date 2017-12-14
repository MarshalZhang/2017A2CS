#Marshal Zhang from S3C3 Option 1
#This is my binary tree code

NULLPOINTER=-1
class ListNode:
    def __init__(self) :
        self.Data = NULLPOINTER
        self.LeftPointer = NULLPOINTER
        self.RightPointer = NULLPOINTER
List = [ListNode() for i in range(10)]
RootPointer = NULLPOINTER
FreeListPtr = 0
List[0].Data= -10000
for i in range(8) :
    List[i].LeftPointer = i + 1
    List[i].RightPointer = NULLPOINTER
List[9].LeftPointer = NULLPOINTER

def InsertNode():
    global RootPointer
    global FreeListPtr
    global List
    TurnLeft= False
    TurnRight =False
    RootPointer = 0
    
    if FreeListPtr != NULLPOINTER:
        NewNodePointer= FreeListPtr
        FreeListPtr= List[FreeListPtr].LeftPointer
        List[NewNodePointer].Data=NewItem
        List[NewNodePointer].LeftPointer= NULLPOINTER
        List[NewNodePointer].RightPointer= NULLPOINTER
        if RootPointer== NULLPOINTER:
            RootPointer=NewNodePointer
        else:
            ThisNodePointer=RootPointer
            while ThisNodePointer != NULLPOINTER:
                PreviousNodePointer= ThisNodePointer
                if List[ThisNodePointer].Data >NewItem:
                    TurnLeft=True
                    ThisNodePointer=List[ThisNodePointer].LeftPointer
                else:
                    TurnRight=True
                    ThisNodePointer=List[ThisNodePointer].RightPointer
            if TurnLeft==True:
                List[PreviousNodePointer].LeftPointer=NewNodePointer
            else:
                List[PreviousNodePointer].RightPointer=NewNodePointer

def OutputAllNodes() :
    global RootPointer
    global FreeListPtr
    global List
    CurrentNodePtr = RootPointer 
    if RootPointer == NULLPOINTER :
        print("No data in list")
    while CurrentNodePtr != NULLPOINTER:
        print("Pointer:",CurrentNodePtr, "Data: ",List[CurrentNodePtr].Data,"LeftPointer:",List[CurrentNodePtr].LeftPointer,"RightPointer:", List[CurrentNodePtr].RightPointer)
        if List[CurrentNodePtr].LeftPointer == NULLPOINTER and List[CurrentNodePtr].RightPointer == NULLPOINTER:
            CurrentNodePtr = NULLPOINTER
        elif List[CurrentNodePtr].LeftPointer == NULLPOINTER:
            CurrentNodePtr = List[CurrentNodePtr].RightPointer
        elif List[CurrentNodePtr].RightPointer == NULLPOINTER:
            CurrentNodePtr = List[CurrentNodePtr].LeftPointer
        elif List[CurrentNodePtr].LeftPointer > List[CurrentNodePtr].RightPointer:
            CurrentNodePtr = List[CurrentNodePtr].RightPointer
        elif List[CurrentNodePtr].LeftPointer < List[CurrentNodePtr].RightPointer:
            CurrentNodePtr = List[CurrentNodePtr].LeftPointer
            
            
            
            

def Search():
    ThisNodePtr = RootPointer
    while ThisNodePtr != NullPointer and List[ThisNodePtr].Data != Searchitem:
        if Tree[ThisNodePtr].Data > Searchitem:
            ThisNodePtr = List[ThisNodePtr].LeftPointer
        else:
            ThisNodePtr = List[ThisNodePtr].RightPointer
    print("the position of this value is:", ThisNodePtr)
        
    
            
def ChooseOption():
    global RootPointer
    global FreeListPtr
    global List
    global NewItem
    print("1:Insert a value into the tree")
    print("2:Search a value from the tree")
    print("3:End the program")
    Option=int(input("Please choose an operation:"))
    while Option!=3:
       if Option==1:
          NewItem=int(input("Enter the Value you want to input:"))
          InsertNode()
       if Option==2:
          Search1()
       OutputAllNodes()
       Option=int(input("Please choose an operation:"))
  
ChooseOption()
        
    
        

