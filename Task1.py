N=int(input())
d = {}
for i in range(N):
    str = input().split(' ')
    for j in range(len(str)):
        if str[j]=='W':
            str[j]='write'
        elif str[j]=='R':
            str[j]='read'
        elif str[j]=='X':
            str[j]='execute'
    d[str[0]] = str[1:]

M=int(input())
d2 = {}
for i in range(M):
    str = input().split(' ')
    d2[str[1]] = str[0]
    if d2[str[1]] in d[str[1]]:
        print('Ok')
    else:
        print('Access denied')

