#Marshal Zhang from S3C3 Option 1
#This file is my que and deque

NULLPOINTER = -1
class ListNode :
   def __init__(self) :
      self.Data = 2
      self.Pointer = NULLPOINTER
List = [ListNode() for i in range(8)]
StartPointer = NULLPOINTER
FreeListPointer = 0
RearPointer = 0
for Index in range(7) :
    List[Index].Pointer = Index + 1
List[7].Pointer = NULLPOINTER
def que():
    global StartPointer
    global FreeListPointer
    global List
    global RearPointer
    F=List[FreeListPointer].Pointer
    if StartPointer ==NULLPOINTER:
       List[0].Data=NewItem
       List[0].Pointer = NULLPOINTER
       FreeListPointer =1
       StartPointer =0
       RearPointer =0
    else:
       List[FreeListPointer].Data= NewItem
       List[FreeListPointer].Pointer =NULLPOINTER
       List[RearPointer]=FreeListPointer
       List[RearPointer]=F
       
    
def OutputAllNodes() :
    global StartPointer
    global FreeListPointer
    global List
    CurrentNodePtr = StartPointer # start at beginning of list
    if StartPointer == NULLPOINTER :
        print("No data in list")
    while CurrentNodePtr != NULLPOINTER : # while not end of list
        print(CurrentNodePtr, " ",List[CurrentNodePtr].Data) # follow the pointer to the next node
        CurrentNodePtr = List[CurrentNodePtr].Pointer
def deque():
    global StartPointer
    global FreeListPointer
    global List
    print("The First one you input is:",List[StartPointer].Data)
    S=List[StartPointer].Pointer
    List[StartPointer].Data=List[StartPointer].Data
    List[StartPointer].Pointer= FreeListPointer
    FreeListPointer=StartPointer
    StartPointer= S
def ChooseOption():
    global StartPointer
    global FreeListPointer
    global List
    global NewItem
    print("1:Que a value")
    print("2:Deque a value")
    print("3:End the program")
    Option=int(input("Please choose an operation:"))
    while Option!=3:
       if Option==1:
          NewItem=int(input("Enter the Value you want to input:"))
          que()
       if Option==2:
          deque()
       OutputAllNodes()
       Option=int(input("Please choose an operation:"))
ChooseOption()
