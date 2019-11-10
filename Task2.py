d={}
str=[]
num=input().split(' ')
num.remove('0')
s=0
for i in range(len(num)):
    if num[i] in d:
        d[num[i]]=d[num[i]]+1
    else:
        d[num[i]]=1
        str.insert(s,num[i])
        s=s+1
min=int(d[num[0]])
for i in range(s):
    if min>d[str[i]]:
        min=d[str[i]]
        max=int(str[i])
for i in range(s):
    if min==d[str[i]]:
        if max<int(str[i]):
            max=int(str[i])
print(max)
    
