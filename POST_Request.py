import requests
url_post = 'https://httpbin.org/post'
payload = {"name":"Joseph","ID":123}
r_post = requests.post(url_post,data = payload)

print(r_post.url)
print(r_post.json())
print(r_post.json()['form'])