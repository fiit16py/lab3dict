# Задание 1: права доступа
perms = {}

n = int(input())
for i in range(n):
	words = input().split()
	file = words[0]
	perms[file] = words[1: ]
print(perms)

m = int(input())
opcode = {'read': 'R',
		  'write': 'W',
		  'execute': 'X'}
for i in range(m):
	operation, file = input().split()
	code = opcode[operation]
	if code in perms[file]:
		print("OK")
	else:
		print("Access denied")