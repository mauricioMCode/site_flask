import requests

data = {"info":"salario", "value":5000}
response = requests.post("http://127.0.0.1:5000/informations", data=data)

if response.status_code == 200:
    message = response.json()
    print(message['empregados'])
else:
    print(response.status_code)





