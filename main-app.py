from CryptoValueEntry import CryptoValueEntry
from CryptoValueRequest import  CryptoValueRequest
from CryptoValueWrite import CryptoValueWrite
if __name__ == '__main__':
    request=CryptoValueRequest()
    entry=request.create_entry()
    writer = CryptoValueWrite.fromOnlyEntry(entry)
    writer.writeInformation()
else:
    print("import lib")
