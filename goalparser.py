# command = "G()()()()(al)"
command = "(al)G(al)()()G"
res=""
for i in range(len(command)):
    # print(command[i:i+2])
    # print(command[i:i+4])
    if command[i] == "G":
        res+="G"
    elif command[i:i+2] == "()":
        res+="o"
    elif command[i:i+4] == "(al)":
        res+="al"