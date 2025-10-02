import itertools
list=[[1,2],[3,4],[5,6],[7,8]]
def qtlb(list):
 for aa in list:
   for bb in aa:
     yield  bb
for x in qtlb(list):
    print(x)
