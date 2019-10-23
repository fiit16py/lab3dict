#1
perms={}

n=int(input())
for i in range(n):
	perm=input().split()
	file=perm[0]
	perms[file] =perm[1:] 




m=int(input())
opcode={'read': 'R',
		'write':'W',
		'execute':'X'}
for i in range(m):
	operation,file=input().split()
	code = opcode[operation]
	if code in perms[file]:
		print("OK")
	else:
		print("Access denied")