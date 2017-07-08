from datetime import  datetime
'Class That stores data to write to CSV'
class CryptoValueEntry:

    def __init__(self,BTCValue,ETHValue):
        self.btcValue=BTCValue
        self.ethValue=ETHValue
        self.dateEntry=datetime.now()

    def csvRepresentation(self):
        csv=str(self.dateEntry)+","+str(self.btcValue)+","+str(self.ethValue)+",\n"
        return csv
