from CryptoValueEntry import  CryptoValueEntry
import os
class CryptoValueWrite:

    def __init__(self,entry,filename,directory):
        self.directory = directory
        self.filename = filename
        self.information = entry

    def __checkAndCreateFile(self):
        filepath=os.path.join(self.directory,self.filename)
        if not os.path.isfile(filepath):
            f=open(filepath,"w+")
            f.write("Time/Date,BTC Value,Eth Value\n")
            f.close()
    def writeInformation(self):
        self.__checkAndCreateFile();
        filepath = os.path.join(self.directory, self.filename)
        f=open(filepath,"a")
        f.write(self.information.csvRep())

    @classmethod
    def fromOnlyEntry(cls,entry):
        obj=cls(entry,"CryptoValuesPython.csv",os.path.expanduser('~'))
        return obj