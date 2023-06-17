import requests
url = 'https://www.ibm.com'
r = requests.get(url)
print(r.request.body)