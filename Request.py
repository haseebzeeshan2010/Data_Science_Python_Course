import requests
url = 'https://www.ibm.com'
r = requests.get(url)
print(r.status_code) # return request status