import requests
Payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get', params=Payload)
print(response.text)