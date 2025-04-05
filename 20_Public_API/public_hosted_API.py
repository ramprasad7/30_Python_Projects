import requests

requests = requests.get("https://ramprasad.pythonanywhere.com/")

data = requests.json()

print(data)