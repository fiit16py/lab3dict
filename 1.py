# Задание 1: права доступа
perms = []

n = int(input())
for i in range(n):
	perm = input().split()
	try:
		perm[perm.index('X')] = 'execute'
	except:
		continue
	try:	
		perm[perm.index('R')] = 'read'
	except:
		continue
	try:
		perm[perm.index('W')] = 'write'
	except:
		continue

m = int(input())
for j in range(m):
	operation, filename = input().split()
	try:
		perm.index(operation)
		perms.append("OK")
	except:
		perms.append("Access denied")
for k in perms:
	print(k)
