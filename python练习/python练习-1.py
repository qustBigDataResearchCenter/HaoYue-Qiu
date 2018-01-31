
# coding: utf-8

# In[1]:


x=5
if x<10:
    print('smaller')
if x>20:
    print('bigger')

print ('finis')


# 

# In[3]:


x=42
if x>1:
    print('morer than one')
    if x<10:
        print('less than 100')
print('all done')


# In[4]:


x=4
if x>2:
    print('bigger')
else:
    print('smaller')
    
print('all down')


# In[5]:


astr='hello bob'
istr=int(astr)
print('first',istr)
astr='123'
istr=int(astr)
print('second',istr)


# In[6]:


astr='bob'
try:
    istr=int(astr)
except:
    istr=-1
    
print('first',istr)

astr='123'
try:
    istr=int(astr)
except:
    istr=-1
    
print('second',istr)


# In[7]:


astr='bob'
try:
    print('hello')
    istr=int(astr)
    print('there')
except:
    istr=-1
    
print('done',istr)


# In[8]:


astr='bob'
print('hello')
istr=int(astr)
print('there')

print('done',istr)


# In[10]:


r=input('enter a number:')
try:
    i=int(r)
except:
    i=-1
if i>0:
    print('nice work')
else:
    print('not a number')


# In[12]:


hour=input('enter houur:')
rate=input('enter rate:')
try:
    hours=int(hour)
    rates=int(rate)
    pay=hours*rates
except:
    print('please input another number!')
    
print('pay=',pay)


# In[20]:


hour=input('enter houur:')
rate=input('enter rate:')
try:
    hours=int(hour)
    rates=int(rate)
except:
    print('please input another number!')
    quit()

pay=hours*rates
print('pay=',pay)


# In[ ]:


hour=input()
rate=input()
try:
    h=int(hour)
    r=int(rate)
except:
    print('error')
    quit()
    
print('pay=',h*r)


# In[ ]:


sh=input()
sr=input()
try:
    fh=float(sh)
    fr=float(sr)
except:
    print('error')
    quit()
    
print(fh,fr)
if fh>40:
    reg=fr*fh
    otp=(fh-40.0)*(fr*0.5)
    xp=reg+otp
else:
    xp=fh*fr
print('pay',xp)


# In[9]:


a=input()
b=input()
try:
    aa=float(a)
    bb=float(b)
    c=aa*bb
    print(c)
except:
    print('error')


# In[10]:


sh=input()
sr=input()
try:
    fh=float(sh)
    fr=float(sr)
except:
    print('error')
    quit()
    
print(fh,fr)
if fh>40:
    reg=fr*fh
    otp=(fh-40.0)*(fr*0.5)
    xp=reg+otp
else:
    xp=fh*fr
print('pay',xp)


# In[1]:


type(123)


# In[2]:


type('123')


# In[1]:


def thing():
    print('hello')
    print('fun')


# In[2]:


thing()
print('zip')
thing()


# In[3]:


max('Nasxsiducn')


# In[4]:


max('Abcd')


# In[5]:


max('bcda')


# In[8]:


big=max('hello world')
print(big)
tiny=min('hello world')   
print(tiny)   #for some reason space is the smallest thing.


# In[7]:


min('helloworld')


# In[9]:


min('hello world')


# In[11]:


min('hello world')
max('hello world')


# In[13]:


print (99/100)
print (float(99)/100)


# In[16]:


m=input()
try:
    n=int(m)
except:
    print('error')


# In[2]:


x=5
print('hello')
def print_lyrics():
    print('I am a lumberjack, and I am okay.')
    print('I sleep all night and I work all day.')
    
print('yo')
print_lyrics()
x=x+2
print(x)


# In[3]:


def greet(lang):
    if lang=='es':
        print('hola')
    elif lang=='fr':
        print('Bongour')
    else:
        print('hello')


# In[4]:


greet('en')


# In[5]:


greet('es')


# In[6]:


greet('fr')


# In[12]:


def greet():
    return('hello')
    
print(greet(),'Glenn')
print(greet(),'Sally')


# In[11]:


greet()


# In[13]:


greet()


# In[14]:


def greet():
    print('hello')
    
print(greet(),'Glenn')
print(greet(),'Sally')


# In[15]:


def greet(lang):
    if lang=='es':
        return 'hola'
    elif lang=='fr':
        return 'bonjour'
    else:
        return 'hello'
    
print(greet('en'),'G')
print(greet('es'),'S')
print(greet('fr'),'M')


# In[16]:


def addtwo(a,b):
    added=a+b
    return added

x=addtwo(3,5)
print(x)


# In[17]:


def H():
    print('sdc')

    
def B():
    return 'eewrh'

H()
B()


# In[1]:


n=5
while n>0:
    print(n)
    n=n-1
print('Blastoff!')
print(n)


# In[1]:


while True:
    line=input('>')
    if line=='done':
        break
    print(line)
print('Done')


# In[5]:


while True:
    line=input('>')
    if line[0]=='#':
        continue       #直接进入下次循环（跳到开头）
    if line=='done':
        break          #结束循环（跳到结尾）
    print(line)
print('Done')


# In[1]:


for i in [5,4,3,2,1]:     #遍历列表里的元素
    print(i)
print('blastoff')


# In[4]:


friends=['joseph','glenn','sally']
for friend in friends:
    print('happy new year：',friend)
print('Done')


# In[6]:


largest_so_far=-1
print('before',largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num>largest_so_far:
        largest_so_far=the_num
    print(largest_so_far,the_num)
    
print('after',largest_so_far)


# In[7]:


zork=0
print('before',zork)
for thing in [9,41,12,3,74,15]:
    zork=zork+1
    print(zork,thing)
print('after',zork)


# In[8]:


zork=0
print('before',zork)
for thing in [9,41,12,3,74,15]:
    zork=zork+thing
    print(zork,thing)
print('after',zork)


# In[10]:


count=0
sum=0
print('before',count,sum)
for value in [9,41,12,3,74,15]:
    count=count+1
    sum=sum+value
    print(count,value,sum)
print('after',count,sum,sum//count)


# In[11]:


count=0
sum=0
print('before',count,sum)
for value in [9,41,12,3,74,15]:
    count=count+1
    sum=sum+value
    print(count,value,sum)
print('after',count,sum,sum/count)


# In[12]:


print('before')
for value in [9,41,12,3,74,15]:
    if value>20:
        print('larger number',value)
print('after')


# In[13]:


found=False
print('before',found)
for value in [9,41,12,3,74,15]:      #当用来验证3是否在列表里时for循环部分可以不用打印
    if value==3:
        found=True
    print(found,value)
print('after',found)


# In[14]:


found=False          #验证3是否在列表里
print('before',found)
for value in [9,41,12,3,74,15]:      
    if value==3:
        found=True
print('after',found)


# In[16]:


found=False          #验证3是否在列表里,但不能说明有几个3（至少有一个3在列表里）
print('before',found)
for value in [9,41,3,12,3,74,3,15]:      
    if value==3:
        found=True
print('after',found)


# In[17]:


count=0        #列表里3的个数
found=False 
print('before',found,count)
for value in [9,41,3,12,3,74,3,15]:      
    if value==3:
        found=True
        count=count+1
print('after',found,count)


# In[18]:


smallest=None
print('before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(smallest,value)
print('after',smallest)


# In[23]:


num=0
tot=0.0
while True:
    sval=input('enter a number: ')
    if sval=='done':
        break
    fval=float(sval)
    #print(fval)
    num=num+1
    tot=tot+fval
    
#print('all done')
print(tot,num,tot/num)


# In[24]:


num=0
tot=0.0
while True:
    sval=input('enter a number: ')
    if sval=='done':
        break
    fval=float(sval)
    #print(fval)
    num=num+1
    tot=tot+fval
    
#print('all done')
print(tot,num,tot/num)


# In[26]:


num=0
tot=0.0
while True:
    sval=input('enter a number: ')
    if sval=='done':
        break
    try:
        fval=float(sval)
    except:
        print('invalid input')
    #print(fval)
    num=num+1
    tot=tot+fval
#print('all done')
print(tot,num,tot/num)


# In[27]:


num=0
tot=0.0
while True:
    sval=input('enter a number: ')
    if sval=='done':
        break
    try:
        fval=float(sval)
    except:
        print('invalid input')
        continue      #continue影响计数项，如果输入的不是数字则计数项不发生变化
    #print(fval)
    num=num+1
    tot=tot+fval
#print('all done')
print(tot,num,tot/num)


# In[ ]:




