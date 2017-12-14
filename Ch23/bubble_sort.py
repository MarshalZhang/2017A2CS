def Bubblesort(array):
    for i in range(5):
        if array[i-1]>array[i]:
            c=array[i-1]
            array[i-1]=array[i]
            array[i]=c
            for i in range(5):
                if array[i-1]>array[i]:
                    c=array[i-1]
                    array[i-1]=array[i]
                    array[i]=c
array=[5,4,2,1,3]
Bubblesort(array)
print(array)



#Marshal Option1
