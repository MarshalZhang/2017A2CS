#Marshal from S3C3 Option1
#This is my dictioary code
class dictionary:
    def __init__(self,Key,Value):
        self.Key=Key
        self.Value=Value
Dictionary =[dictionary(None,None) for i in range (100)]

def Insert(NewItem,Def):
    global Dictionary
    Index=0
    for i in range(len(NewItem)):
        Index+= ord(NewItem[i])
    Index =Index %100
    N=0
    while Dictionary[Index].Key != None and N!=101:
        N+=1
        Index +=1
        if Index == 100:
            Index = 0

    Dictionary[Index].Key = NewItem
    Dictionary[Index].Value = Def
def FindValue():
    global Dictionary
    global SearchItem
    Index=0
    for i in range(len(SearchItem)):
        Index += chr(SearchItem)
    N=0
    while Dictionary[Index].Value != SearchItem and Dictionary[Index].Key !=None and N!=101:
        N+=1
        Index =Index +1
        if Index==100:
            Index = 0
    if Dictionary[Index]==None:
        print("The Item is not in the list")
    if Dictionary[Index].Key == SearchItem:
        print("the definition of this term is:",Dictionary[Index].Value)


def Option():
    global NewItem
    global Dictionary
    global SearchItem
    global Def
    print("If you want to insert one abbreviation into the dictionary, input 1")
    print("If you want to look up one word from the dictionary, input 2")
    print("If you want to end the program, input 3")
    Option =int(input("please choose the operation:"))
    while Option !=3:
        if Option ==1:
            NewItem =str(input("please enter the new word you want to insert:"))
            Def =str(input("please enter the defination of this term:"))
            Insert(NewItem,Def)
            for i in range(100):
                print("index:",i,"Key:",Dictionary[i].Key,"Value:",Dictionary[i].Value)
        if Option ==2:
            SearchItem =str(input("please enter the Key you want to search:"))
            FindValue()
        Option =int(input("please choose the operation:"))
Insert("IP","Internet Protocol")
Insert("DBMS","Data management system")
Insert("DBA","Database administrator")
Insert("LCD","Liquid-crystal display")
Option()
