import requests
resp = requests.get("http://www.example.com")
print(resp.status_code)
print(len(resp.text))
print(resp.url)