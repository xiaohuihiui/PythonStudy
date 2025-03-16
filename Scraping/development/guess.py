import random

history={}

def try_to_guess(name,answer):
 guess_times=0
 while guess_times<10:
    guess_num=int(input('guess number'))
    if guess_num<answer:
         print('too mmall')
    elif guess_num==answer:
     print('correct')
     history[name].append('correcct')
     break
    else:  
     print('too big') 
     guess_times+=1
 else:
   print('lost many times')
   history[name].append('faild')



def showHistoy():
  for name,record in history.items():
    print('name:{},recode:{}'.format(name,record))

def start():
  name=input('input you name')
  if name=='exit':
    return
  if name not in history:
   history[name]=[]
   answer=random.randint(0,1024)
   print(answer)
   try_to_guess(name,answer)


def default():
 pass

if __name__ =='__main__':
    select_num={'1':showHistoy,'2':start,'3':exit}
    while True:
      select=input('1.history Record\n2.start\n3.exit\nplease input num：')
      select_num.get(select,default)()