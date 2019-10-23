perms = {}
m = int(input())
for i in range(m):
    perm = input().split()
    file = perm[0]
    perms[file] = perm[1:]
n = int(input())
for j in range(n):
    opcode ={"read": "R","write":"W","execute": "X"}
    operation, filename = input().split()
    code = opcode[operation]
    if code in perms[file]:
       print("OK")
    else:
       print("Access denied")
