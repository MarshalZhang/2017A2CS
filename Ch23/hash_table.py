#Marshal from S3C3 Option1
# this is my hash table code


HashTable =[0 for i in range(10)]
def Insert(NewItem):
    global HashTable
    Index= NewItem % 10
    X=1
    for i in range(10):
        X=X*HashTable[i] #calculate the product of all the values in the table
    while HashTable[Index] != 0 and X==0:
        Index +=1
        if Index == 10:
            Index = 0
    if X!=0:
        print("There is no space for the NewItem")

    HashTable[Index] = NewItem

def FindValue():
    global HashTable
    global SearchItem
    Index = SearchItem %10
    N=0
    while HashTable[Index]!= SearchItem and HashTable[Index]!=0 and N!=11:
        N+=1
        Index =Index +1
        if Index==10:
            Index = 0
    if HashTable[Index]==0:
        print("The Item is not in the list")
    if HashTable[Index] == SearchItem:
        print(HashTable[Index],"is at position", Index)
def Option():
    global NewItem
    global HashTable
    global SearchItem
    print("If you want to insert one number into the Hashtable, input 1")
    print("If you want to find one numebr from the Hashtable, input 2")
    print("If you want to end the program, input 3")
    Option =int(input("please choose the operation:"))
    while Option !=3:
        if Option ==1:
            NewItem =int(input("please enter the new item:"))
            Insert(NewItem)
            for i in range(10):
                print(HashTable[i])
        if Option ==2:
            SearchItem =int(input("please enter the value you want to search:"))
            FindValue()
        Option =int(input("please choose the operation:"))
            
Option()

    

        
