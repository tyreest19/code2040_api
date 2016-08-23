import requests
import json
url = 'http://challenge.code2040.org/api/prefix'
payload = {'token': '6947ddc0354913e7928f75ce2f42e5ed',
	    'github': 'https://github.com/tyreest19/code2040_api',
           'array': [1,2,34,4]}
post = requests.post(url,json = payload)
prefix = str(post.content).split(':')
prefix = prefix[1].split(',') # Grabs prefix
prefix = prefix[0]
prefix = prefix[:-1] # delete the last string
prefix = prefix[1:]  # delete last string
array = str(post.content).split('[') # spilts the array out of brackets
array = array[1] # grabs the strings in the array
for i in range(3):
    array = array[:-1] # deltes last 3 chars of the array
array = array.split(',') # creates a list with the string
answer = list() # answers will be stored here
for i in array:
    i = i[:-1] # last quoute in the array
    i = i[1:]  # deltes last quote in the array
    if i.startswith(prefix) != True: # checks for strings without the input
        answer.append(i) # appends to answers list
payload['array'] = answer # makes answer the value for the array key
url = 'http://challenge.code2040.org/api/prefix/validate'
post = requests.post(url,json = payload)
print(post.content)
