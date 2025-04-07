import json

person = {
    'basic_info': {'name': 'hu',
                   'age': 24,
                   'sex': 'male',
                   'merry': False},

    'work_info': {'salary': 99999,
                  'position': 'engineer',
                  'department': None}
    }
#person_json=json.dumps(person)
person_json=json.dumps(person,indent=4)
print(type(person_json))
person_dick=json.loads(person_json)
print(type(person_dick))
print(person_dick['work_info']['salary'])



# book_list = [
#     {'name': 'san',
#      'price': 99.99},
#     {'name': 'xi',
#      'price': 100.0},
#     {'name': 'hong',
#      'price': 10.50},
#     {'name': 'shui',
#      'price': 20.22}
# ]
# book_json=json.dumps(book_list,indent=4)
# print(book_json)
