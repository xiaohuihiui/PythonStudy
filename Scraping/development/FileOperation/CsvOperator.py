import csv

file_path2 = r"D:\studybook\PC\python\第3章\program\new.csv" 
with open(file_path2,encoding='utf-8') as f2:
    content=csv.DictReader(f2)
    for row in content:
        print(row)