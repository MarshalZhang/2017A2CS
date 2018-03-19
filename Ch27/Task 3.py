class NodeClass():
    def __init__(self):
        self.__Data=""
        self.__Pointer=-1
    def SetData(self, D):
        self.Data=D

    def GetData(self):
        return(self.__Data)
    
    def SetPointer(self, x):
        self.__Data = x
        
    def GetPointer(self):
        return(self.__Pointer)

class QueueClass:
    def __init__(self):
        self.__Queue = [NodeClass() for i in range(51)]
        self.__Head = -1
        self.__Tail = -1

    def JoinQueue(self, d):
        if Head == -1 :
            Head = 0
        self.__Tail += 1 
        i = self.__Tail
        self.__Queue[i].SetData(d)
