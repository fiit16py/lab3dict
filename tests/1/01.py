n = int(input())
perms={}
for i in range(n):
	words = input().split()
	file = words[0]
	perms[file]=words[1:]
m = int (input())
print (perms)
opcode={'read': 'R', 'write':'W','execute':'X'}
for j in range(m):
	operation, filename = input().split()
	code=opcode[operation]
	if code in perms[filename]:
		print("OK")
	else:
		print("access denied")

