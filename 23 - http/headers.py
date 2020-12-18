import requests

url = "https://icanhazdadjoke.com/"

#plainResponse = requests.get(url, headers={"Accept": "text/plain"})
jsonResponse = requests.get(url, headers={"Accept": "application/json"})

#print(plainResponse.text)
#print(jsonResponse.text)
#print(jsonResponse.json())

data = jsonResponse.json()

print(data["joke"])
