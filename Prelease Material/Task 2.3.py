class Toy:
    def __init__(self, Name, ID,  Price, Minimumage):
        self.__Name= Name
        self.__ID= ID
        self.__Price= Price
        self.__Minimumage= Minimumage
    def Constructor(self):
        self.Name=""
        self.ID=0
        self.Price=-1
        self.__Minimumage=-1
    def SetName(self,N):
        self.Name=N
    def SetID(self,N):
        self.ID=N
    def SetPrice(self,P):
        self.Price=P
    def SetMinimuage(self,N):
        self.MinimumTOyage=Minimumage
    def GetName(self):
        return(self.__Name)
    def GetID(self):
        return(self.__ID)
    def GetPrice(self):
        return(self.__Price)
    def GetMinimumage(self):
        return(self.__Minimumage)

    def Output(self):
        print("Name:", self.GetName(),"ID:", self.GetID(),"Price:",self.GetPrice(),"MinimumAge:",self.GetMinimumage())
    


class ComputerGame(Toy):
    def __init__(self, N, I, P, M, C, Co):
        Toy.__init__(self,N, I, P, M)
        self.__Category =C
        self.__Console = Co

    def Constructor(self):
        self.Constructor()
        self.Category = ""
        slef. Console =""

    def SetCategory(self, C):
        self.Category = C

    def SetConsole(self, Co):
        self.Console= Co

    def GetCategory(self):
        return(self.__Category)

    def GetConsole(self):
        return(self.__Console)

    def Output(self):
        print("Name:", self.GetName(),"ID:", self.GetID(),"Price:",self.GetPrice(),"MinimumAge:",self.GetMinimumage())
        print("Category:", self.GetCategory(), "Console:", self.GetConsole())
        

class Vehicle(Toy):
    def __init__(self, N, I, P ,M ,T, H, L, W):
        Toy.__init__(self,N, I, P, M)
        self.__Type=T
        self.__Height=H
        self.__Length=L
        self.__Weight= W

    def Constructor(self):
        self.Constructor()

    def SetHeight(self,H):
        self.Height=H

    def SetLength(self,L):
        self.Length=L

    def SetWeight(self,W):
        self.Weight=W

    def GetHeight(self):
        return(self.__Height)

    def GetLength(self):
        return(self.__Length)

    def GetWeight(self):
        return(self.__Weight)

    def Output(self):
        print("Name:", self.GetName(),"ID:", self.GetID(),"Price:",self.GetPrice(),"MinimumAge:",self.GetMinimumage())
        print("Weight:", self.GetWeight(), "Height:", self.GetHeight(), "length:", self.GetLength(), "Weight:", self.GetWeight())
        

def Main():
    global A
    global B
    global C
    global D
    global List
    A=Vehicle("red Sports Car", "RSC13", 15.00,6,"car",3.3,12.1,0.08)
    B=ComputerGame("Monopoly","RSC12", 300,10,"Management", "Camping")
    C=Toy("Dick", "RSC14", 0,18)
    D=ComputerGame("Move your dick","HHC11", 13,2,"Action'","sexual")
    List=[A,B,C,D]

def SearchID(N):
    for i in range(len(List)):
        if List[i].GetID()==N:
            List[i].Output()

def Sort():
    for j in range(len(List)):
        for i in range(len(List)-1):
            if List[i].GetPrice()>List[i+1].GetPrice():
                temp= List[i]
                List[i]=List[i+1]
                List[i+1]=temp
    print(List)
            
Main()

        
        
        
    
    
        
        
        
