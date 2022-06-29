import requests
url = "https://secure.paygate.co.za/payweb3/query.trans"

payload = {
  "PAYGATE_ID":"10011072130",
  "PAY_REQUEST_ID":"9jCWQt6oQuvschkFUZ4-9hECwpzcoZo4hNfig2g3sx8F5E81LKovzw==",
  "REFERENCE":"pgtest_123456789",
  "CHECKSUM":"12ef5d8bf7434fb291dde99340677576"
}

headers = {
      "Content-Type":"application/x-www-form-urlencoded"
}

response = requests.request("POST",url,json=payload,headers=headers)

print(response.text)