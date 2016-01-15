import requests
url = "https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address/"
resp = requests.get(url)
print(resp.text.count("Applause"))
caseless = resp.text.lower()
print(caseless.count("applause"))
print(resp.text.count("<p>"))