# initiate - merchant process a detailed post request to payweb
# Response payrequestid and checksum
import json
#initiate and get response as payrequest id
import requests

url = "https://secure.paygate.co.za/payweb3/initiate.trans"
 
payload = {
    "PAYGATE_ID": "10011072130",  
    "REFERENCE": "",
    "AMOUNT": "3299",
    "CURRENCY": "IND",
    "RETURN_URL": "https://www.bigcommerce.com/",
    "TRANSACTION_DATE": "2021-06-30 09:30:10",
    "LOCALE": "hi",
    "COUNTRY": "IND",
    "EMAIL": "fazilneopraxis@gmail.com",
    "PAY_METHOD":"CC",
    "PAY_METHOD_DETAIL": "",
    "VAULT": 1,
    "CHECKSUM": "cb6314787044dfc1869658b5abb608ab "
}


headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

response = requests.request("POST", url, json=payload, headers=headers)
print(response.text)
