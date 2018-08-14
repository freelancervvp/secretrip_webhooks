print("Hook['params'] is populated with request parameters")
print(Hook['params'])
print("Hook['req'] is the http request")
print(Hook['req']['url'])
import requests
name = Hook['params']['name'].encode('utf-8','surrogateescape').decode('utf-8')
email = Hook['params']['email']
api_key = Hook['env']['sendinblue_api_key']
url = "https://api.sendinblue.com/v3/smtp/email"
payload = "{\"sender\":{\"name\":\"Secret Trip\",\"email\":\"hello@secretrip.ru\"},\"to\":[{\"email\":\"%s\",\"name\":\"%s\"}],\"htmlContent\":\"\",\"subject\":\"\",\"replyTo\":{\"email\":\"hello@secretrip.ru\",\"name\":\"Secret Trip\"},\"templateId\":5,\"params\":{\"NAME\":\"%s\"}}" % (email,name,name)
response = requests.request("POST", url, data=payload.encode("utf-8"), headers={'api-key': api_key,'content-type': 'application/json'})
print(response.text)
