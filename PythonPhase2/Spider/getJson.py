# 第 4 章 //xld.py
import requests
import json
import xlwt

URL = "http://www.csrc.gov.cn/pub/zjhapp/wz_1/wz_1_1/next_7797_1.json"
headers = {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G977N Build/LMY48Z)"
}

s = requests.request("get", URL, headers = headers)
dic = json.loads(s.text)
list = dic["list_datas"]

i = 0
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('onesheet')

for lis in list:
    worksheet.write(i, 0, lis["title"]) # 向第 0 列 第 i 行 添
    worksheet.write(i, 1, lis["URL"])    # 向第 1 列 第 i 行 添
    i = i + 1

workbook.save('infol.xlsx')