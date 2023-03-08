import requests

response = requests.get("https://cisco.com")
print(response.status_code)