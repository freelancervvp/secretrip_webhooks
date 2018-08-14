print("Hook['params'] is populated with request parameters")
print(Hook['params'])
print("Hook['req'] is the http request")
print(Hook['req']['url'])
import requests
url = "https://api.sendinblue.com/v3/smtp/email"
a = 'Владимир'.encode('utf-8','surrogatepass')
payload = "{\"sender\":{\"name\":\"Secret Trip\",\"email\":\"hello@secretrip.ru\"},\"to\":[{\"email\":\"freelancervvp@gmail.com\",\"name\":\"VLADIMIR\"}],\"htmlContent\":\"\",\"subject\":\"\",\"replyTo\":{\"email\":\"hello@secretrip.ru\",\"name\":\"Secret Trip\"},\"templateId\":5,\"params\":{\"NAME\":\"%s\"}}" % Hook['params']['name']
response = requests.request("POST", url, data=payload, headers={'api-key': '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','content-type': 'application/json'})
print(response.text)
