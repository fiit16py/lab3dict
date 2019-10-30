file_count = int(input())
files = []
for i in range(file_count):
    file_parse = input().split()
    file_info = {"filename":file_parse[0],"permissions":[]}
    file_info["permissions"] = file_parse[1:]
    files.append(file_info)
    pass
cmd_count = int(input() )

def check_perm(op, file):
    for i in range(file_count):
        if files[i]["filename"] == file:
            if op in files[i]["permissions"]:
                return 'OK'
        pass
    return 'Access denied'

for i in range(cmd_count):
    conv = {'write':'W', 'read':'R', 'execute':'X'} 
    cmd_parse = input().split()
    print(check_perm(conv[cmd_parse[0]], cmd_parse[1]))
    pass
