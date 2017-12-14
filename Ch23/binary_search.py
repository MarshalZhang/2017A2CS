#Option 1  Marshal Binary Search
Found= False
SearchFailed= False
First=1
List=[7,12,19,23,27,33,37,41,45,56,59,60,62,71,75,80,84,88,92,99]
Last= len(List)
SearchItem=int(input("What is the number you want to search?"))
while Found== False and SearchFailed==False:
    Middle=(First+Last)//2
    if List[Middle]==SearchItem:
        Found=True
    else:
        if First>=Last:
            SearchFailed=True
        else:
            if List[Middle]>SearchItem:
                Last=Middle-1
            else:
                First=Middle+1
if Found==True:
    print("the position of the searchitem is:",Middle)
else:
    print("item is not in the array")

    
    
