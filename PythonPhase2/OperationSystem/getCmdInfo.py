import os
commend="java"
r=os.popen(commend)
info=r.readlines()
for i in info:
    line=i.strip("\r\n")
    print(line)