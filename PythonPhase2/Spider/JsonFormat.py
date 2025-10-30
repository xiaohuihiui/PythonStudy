import json

dic={"user":"jack","password":"123","age":"12"}
jsonStr = json.dumps(dic)
print(type(jsonStr))

data = json.loads(jsonStr)
print(type(data))
print(data['user'])
print(data['password'])
print(data['age'])


