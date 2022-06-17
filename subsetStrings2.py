ipt = "abc"
opt = ""
sol = []


def solve(ip, op):
    # print("@========@\n")
    # print("ip is", ip)
    # print("op is", op)

    # print("len(ip)", len(ip))
    if len(ip) == 0:
        print("ip is zero, op is", (op))
        sol.append("".join(sorted(op)))
        return
    # ip1 = ip.copy()ooo
    op1 = op
    # print("op1 is", op1)
    op2 = ip[0] + op
    ip = ip[1:]
    # print("op2 is", op2)

    # print("\nip is", ip)

    solve(ip, op1)
    solve(ip, op2)


solve(ipt, opt)
sol.remove("")
print(sol)
s = ""
for a in sol:
    s += a+" "
print(s[:-1])


class Solution:
    def AllPossibleStrings(self, s):
        ip = s
        opt = ""
        sol = []

        def solve(ip, op):
            if len(ip) == 0:
                sol.append(op)
                return
            op1 = op
            op2 = ip[0] + op
            ip = ip[1:]
            solve(ip, op1)
            solve(ip, op2)

        solve(ip, opt)
        sol.remove("")
        return sorted(sol)

        # s = ""
        # for a in sol:
        #     s += a+" "
        # return s[:-1]
a = Solution()

print(a.AllPossibleStrings(23))
