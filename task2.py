digits = input().split()
repeat = {}
for i in digits:
    if i in repeat.keys():
        repeat[i] += 1
    else:
        repeat[i] = 1
mn = 0
mn_key = ''
for i in repeat.keys():
    if mn == 0:
        mn = repeat[i]
        mn_key = i
    if repeat[i] < mn:
        mn_key = i
        mn = repeat[i]
print(mn_key)
