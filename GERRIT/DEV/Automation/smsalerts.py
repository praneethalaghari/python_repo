
import requests

url = "https://www.fast2sms.com/dev/bulk"

payload = "sender_id=FSTSMS&message=Good morning , this is prasad  sending from python.&language=english&route=p&numbers=9573340942"

headers = {

'authorization': "nJIpT3WNiYuhjcDvt5FSz89VHPyZxfwR4mqG7lbkOBXMsL1QeaKW7TPusowIaRHvl10yezU4gLxX26Fm",

'Content-Type': "application/x-www-form-urlencoded",

'Cache-Control': "no-cache",

}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

