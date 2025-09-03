import os
print(os.getcwd())
with open(r"demo/message.txt","w") as f:
    # print(f.readline())
    pass
print(os.path.abspath("demo/message.txt"))