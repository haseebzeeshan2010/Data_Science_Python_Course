import requests
url = 'https://www.ibm.com'
r = requests.get(url)
print(r.status_code) # return request status
print(r.request.headers) # return request headers
print(r.request.body) # return body
print(r.headers) # return dictionary of http response headers
print(r.headers['date']) # returning the data of the request