#Marshal Zhang from S3C3 Option 1
#This file is my Stack Push and Pop
NULLPOINTER = -1

class ListNode :
   def __init__(self) :
      self.Data = 2
      self.Pointer = NULLPOINTER
List = [ListNode() for i in range(8)]
StartPointer = NULLPOINTER
FreeListPtr = 0
for Index in range(7) :
    List[Index].Pointer = Index + 1
List[7].Pointer = NULLPOINTER
def push():
    global StartPointer
    global FreeListPtr
    global List
    List[FreeListPtr].Data=NewItem
    List[FreeListPtr].Pointer=FreeListPtr-1
    FreeListPtr=FreeListPtr+1
    StartPointer=StartPointer+1
    
def OutputAllNodes() :
    global StartPointer
    global FreeListPtr
    global List
    CurrentNodePtr = StartPointer # start at beginning of list
    if StartPointer == NULLPOINTER :
        print("No data in list")
    while CurrentNodePtr != NULLPOINTER : # while not end of list
        print(CurrentNodePtr, " ",List[CurrentNodePtr].Data) # follow the pointer to the next node
        CurrentNodePtr = List[CurrentNodePtr].Pointer
def pop():
    global StartPointer
    global FreeListPtr
    global List
    print("The Last one you input is:",List[StartPointer].Data)
    List[StartPointer].Pointer=FreeListPtr
    StartPointer-=1
    FreeListPtr-=1
    
def ChooseOption():
    global StartPointer
    global FreeListPtr
    global List
    global NewItem
    print("1:Push a value")
    print("2:Pop a value")
    print("3:End the program")
    Option=int(input("Please choose an operation:"))
    while Option!=3:
       if Option==1:
          NewItem=int(input("Enter the Value you want to input:"))
          push()
       if Option==2:
          pop()
       OutputAllNodes()
       Option=int(input("Please choose an operation:"))
  
ChooseOption()


