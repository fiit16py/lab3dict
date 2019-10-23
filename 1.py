# Задание 1: права доступа
perms = {}
output = []

n = int(input())
for i in range(n):
	perm = input().split()
	file = perm[0]
	for i in range(1, len(perm)):
		perms[file] = perm[i]

m = int(input())
opcode = {'read': 'R', 'write': 'W', 'execute': 'X'}
for j in range(m):
	operation, filename = input().split()
	code = opcode[operation]
	if code in perms[file]:
		output.append("OK")
	else:
		output.append("Access denied")
for k in output:
	print(k)
