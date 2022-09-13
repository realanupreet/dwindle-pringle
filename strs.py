goal = "codeit"
targets = "code it nice"
ntargets = targets.split(" ")
for n in ntargets:
    print(n)
    if n == goal[:len(n)]:
        for i in ntargets:
            print("", i)
            if i == goal[len(n):]:
                # return 1
                print("woo")
# return 0
