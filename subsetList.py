ipt = [4, 4, 4, 4, 2, 4]
opt = []
sol = []

mapp = {}


def solve(ip, op):
    # print("@========@\n")
    # print("ip is", ip)
    # print("op is", op)

    # print("len(ip)", len(ip))
    if len(ip) == 0:
        # print("ip is zero, op is", op)
        sol.append(op)
        return
    # ip1 = ip.copy()ooo
    op1 = op
    # print("op1 is", op1)
    op2 = [ip[0]] + op
    ip = ip[1:]
    # print("op2 is", op2)

    # print("\nip is", ip)

    solve(ip, op1)
    solve(ip, op2)


solve(ipt, opt)
print(sol)
for s in sol:
    if tuple(sorted(s)) not in mapp:
        mapp[tuple(sorted(s))] = 1
newsol = []
for k in mapp.keys():
    print(list(k))
    newsol.append(list(k))
print(newsol)
