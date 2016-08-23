import requests
import json
url = 'http://challenge.code2040.org/api/reverse'
payload = {'token': '6947ddc0354913e7928f75ce2f42e5ed',
	    'github': 'https://github.com/tyreest19/code2040_api',
           'string': 'cupcake'}
post = requests.post(url,json = payload)
print(post.content)
returned_string = str(post.content)[:-1]
for i in range(2):
    returned_string =returned_string[1:]
print(returned_string)
url = 'http://challenge.code2040.org/api/reverse/validate'
payload['string'] = returned_string[::-1]
post = requests.post(url,json = payload)
print(payload['string'])
print(post.content)

