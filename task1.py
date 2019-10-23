f = open("04")
file_count = int(f.readline())
files = []
for i in range(file_count):
    file = f.readline()
    file_parse = file.split()
    file_info = {"filename":file_parse[0],"permissions":[]}
    file_info["permissions"] = file_parse[1:]
    files.append(file_info)
    pass
cmd_count = int(f.readline())

def check_perm(op, file):
    for i in range(file_count):
        if files[i]["filename"] == file:
            if op in files[i]["permissions"]:
                return 'OK'
        pass
    return 'Access denied'

for i in range(cmd_count):
    cmd = f.readline()
    cmd_parse = cmd.split()
    if cmd_parse[0] == 'read':
        print(check_perm("R", cmd_parse[1]))
    elif cmd_parse[0] == 'write':
        print(check_perm("W", cmd_parse[1]))
    elif cmd_parse[0] == 'execute':
        print(check_perm("X", cmd_parse[1]))
    pass
