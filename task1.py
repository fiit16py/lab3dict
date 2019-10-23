print("input path:")
path = input()
f = open(path)
n = int(f.readline().split('\n')[0])
rules = {}
for i in range(n):
    s = f.readline().split('\n')[0]
    s = s.split()
    rules[s[0]] = {}
    for r in range(len(s) - 1):
        rules[s[0]][s[r + 1].lower()] = 0

#print(rules)        

n = int(f.readline().split('\n')[0])
for i in range(n):
    s = f.readline().split('\n')[0]
    s = s.split()
    #print(s)
    if s[0] == 'read':
        s[0] = 'r'
    if s[0] == 'execute':
        s[0] = 'x'
    if s[0] == 'write':
        s[0] = 'w'
    if s[1] in rules:
        if s[0] in rules[s[1]]:
            print('OK')
        else:
            print('Access denied')
    else:
        print('Access denied')