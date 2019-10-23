def get_second(var):
    return var[1]

l = [int(_) for _ in input().split()]
d = {}
for i in range(len(l)):
    if l[i] == 0:
        d[l[i]] = 1
        break
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1
d = list(d.items())
d.sort(key=get_second)
i = 1
c = d[0][1]
mx = d[0][0]
while True:
    if(i >= len(d)):
        break
    if d[i][1] != c:
        break
    if d[i][0] > mx:
        mx = d[i][0]
    i += 1
        
print(mx)