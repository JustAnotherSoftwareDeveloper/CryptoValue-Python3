import requests
import json
from CryptoValueEntry import CryptoValueEntry
'Class for handling requests'
class CryptoValueRequest:
    requestID = 0

    def __init__(self):
        CryptoValueRequest.requestID+=1

    def __request_value(self,ValueType):
        requestURL="https://coinmarketcap-nexuist.rhcloud.com/api/"+ValueType+"/price"
        request=requests.get(requestURL)
        request.raise_for_status();
        #Parse Json
        j=request.json()
        value=j["usd"]
        return value

    def create_entry(self):
        ethValue=self.__request_value("eth")
        btcValue=self.__request_value("btc")
        cryptoValue=CryptoValueEntry(btcValue,ethValue)
        return cryptoValue
