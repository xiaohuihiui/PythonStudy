import csv

# file_path2 = r"D:\studybook\PC\python\第3章\program\new.csv" 
# with open(file_path2,encoding='utf-8') as f2:
#     content=csv.DictReader(f2)
#     for row in content:
#         username=row['username']
#         cont=row['content']
#         replaytime=row['reply_time']
#         print('username:{},cont:{},reply_time{}'.format(username,cont,replaytime))


# file_path2 = r"D:\studybook\PC\python\第3章\program\new.csv" 
# with open(file_path2,encoding='utf-8') as f2:
#     content=[x for x in csv.DictReader(f2)]
#     for row in content:
#         username=row['username']
#         cont=row['content']
#         replaytime=row['reply_time']
#         print('username:{},cont:{},reply_time{}'.format(username,cont,replaytime))

file_path2 = r"D:\studybook\PC\python\第3章\program\new.csv" 
data=[{'name':'a','age':'4'},
      {'name':'b','age':'5'},
      {'name':'c','age':'6'}]
with open(file_path2,'w',encoding='utf-8') as f2:
    f2=csv.DictWriter(f2,fieldnames=['name','age'])
    f2.writeheader()
    f2.writerows(data)
    f2.writerow({'name':'d','age':'7'})