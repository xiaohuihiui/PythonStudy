from pymongo import MongoClient

client=MongoClient()
data=client['Chapter6']
collection=data['spider']
# par={'id':1,'name':'aa','age':20,'salary':9999,
#      'id':2,'name':'aa','age':20,'salary':9999,
#      'id':3,'name':'aa','age':20,'salary':9999,
#      'id':4,'name':'aa','age':20,'salary':9999}
# collection.insert_one(par)
# content=collection.find({'age':20})
# for re in content:
#     print(re)
# content=collection.find({'age':20},{'salary':9999})
# content=collection.find({'age':{'$eq':20}}).sort('id',1)
# for re in content:
#     print(re)
# content=collection.update_one({'id':12},{'$set':{'age':22}})
# collection.delete_one({'id':4})
content=collection.distinct('name')
print(content)