def get_second(var):
    return var[1]

d = {}
while True:
    n = int(input())
    if n == 0:
        break
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
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