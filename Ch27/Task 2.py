#End of chapter 27 questions
#Marshal from S3C3 Option1
class BankAccount:
    def __init__(self, i):
        self.__AccountHolderName = ''
        self.__IBAN = i

    def SetAccountHolderName(self, n):
        self.__AccountHolderName = n

    def GetAccountHolderName(self):
        return(self.__AccountHolderName)

    def GetIBAN(self):
        return(self.__IBAN)
