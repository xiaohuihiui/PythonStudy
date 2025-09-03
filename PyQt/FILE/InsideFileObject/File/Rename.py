import os
if os.path.exists("test3.txt"):
    pass
os.rename("test3.txt", "test4.txt")
