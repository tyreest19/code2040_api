import requests
import json
url = 'http://challenge.code2040.org/api/prefix'
payload = {'token': '6947ddc0354913e7928f75ce2f42e5ed',
	    'github': 'https://github.com/tyreest19/code2040_api',
           'array': [1,2,34,4]}
post = requests.post(url,json = payload)
prefix = str(post.content).split(':')
prefix = prefix[1].split(',')
prefix = prefix[0]
prefix = prefix[:-1]
prefix = prefix[1:]
print(prefix)
array = str(post.content).split('[')
array = array[1]
for i in range(3):
    array = array[:-1]
array = array.split(',')
answer = list()
for i in array:
    i = i[:-1]
    i = i[1:]
    if i.startswith(prefix) != True:
        answer.append(i)
print()       
print(answer)
payload['array'] = answer
url = 'http://challenge.code2040.org/api/prefix/validate'
post = requests.post(url,json = payload)
print(post.content)
