from CryptoValueEntry import CryptoValueEntry
if __name__ == '__main__':
    newEntry=CryptoValueEntry(500.0,5.0)
    print(newEntry.csvRepresentation())
else:
    print("import lib")
