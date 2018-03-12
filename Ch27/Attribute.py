import datetime
class LibraryItem:
    def __init__(self,t,a,i):
        self.__Title =t
        self.__Author__Artist=a
        self.__ItemID=i
        self.__OnLoan = False
        self.__DueDate= datetime.date.today()
        self.__BorrowerID = ""

    def GetTitle(self):
        return(self.__Title)

    def Borrowing(self,a):
        self.Onloan= True
        self.DueDate =self.__DueDate + datetime.timedelta(weeks=3)
        self.__BorrowerID = a

    def Returning(self):
        self.__OnLoan =False

    def PrintDetails(self):
        print(self.__Title,';',self.__Author__Artist,';',end='')
        print(self.__ItemID,';',self.__OnLoan)
        print(self.__DueDate, ' ; Borrower: ', self.__BorrowerID)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t,a, i)
        self.__IsRequested = False
        self.__RequestedBy =0

    def GetIsRequested (self):
            return(self.__IsRequested)

    def SetIsRequested(self,a):
        self.__IsRequested =True
        self.__RequestedBy = a

    def PrintDetails(self):
        print("Book Details")
        LibraryItem.PrintDetails(self)
        if self.__IsRequested:
            print('Requested by ', self.__RequestedBy)
        else :
            print('no requests')

class CD(LibraryItem):
    def  __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre =""

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self,g):
        self.Genre=g

    def PrintDetails(self):
        print("CD Details")
        LibraryItem.PrintDetails(self)
        print(self.__Genre)

class Borrower():
    def __init__(self,n,a,i,o):
        self.BorrowerName=n
        self.EmailAddress=a
        self.BorrowerID= i
        self.ItemsOnloan =o

    def Constructor(self):
        ItemsOnloan = 0

    def GetBorrowerName(self):
        return(self.BorrwerName)

    def GetEmailAddress(self):
        return(self.EmailAddress)

    def GetBorrowerID(self):
        return(self.BorrowerID)

    def GetitemsOnLoan(self):
        return(self.ItemsOnloan)

    def UpdateitemsOnLoan(self,n):
        self.ItemsOnloan +=n

    def PrintDetails(self):
        print("Borrower     :", self.BorrowerName)
        print("EmailAddress :", self.EmailAddress)
        print("BorrowerID   :", self.BorrowerID)
        print("Items On loan:", self.ItemsOnloan)
        

def GetOption():
    print("1 - Add a new borrower")
    print("2 - Add a new book")
    print("3 - Add a new CD")
    print("4 - Borrow a book")
    print("5 - Return a book")
    print("6 - Borrow a CD")
    print("7 - Return a CD")
    print("8 - Request book")
    print("9 - Print al l details")
    print("99- Exit program")
    Option =int(input("Please Enter your choice:"))
    

        
x=LibraryItem("And Justice For All","Metallica","000414")
y=CD("Dark Side of the Moon","Pink Floyd","741026")
z=Book("Marshal is so handmsome","Everyone","01499")
Marshal= Borrower("Marshal", "Mars","000414",4)
    

