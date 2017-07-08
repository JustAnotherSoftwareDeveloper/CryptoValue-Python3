from CryptoValueEntry import CryptoValueEntry
from CryptoValueRequest import  CryptoValueRequest
if __name__ == '__main__':
    request=CryptoValueRequest()
    entry=request.create_entry();
    print(entry.csvRepresentation())
else:
    print("import lib")
