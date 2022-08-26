import bisect as bt
arr1 = [6345, 7477, 1769, 4061, 8519, 2784, 5887, 4743, 2865, 7339, 843, 3106, 5916, 5468, 9601, 5921, 9931, 2070, 4750, 2685, 6168, 7361,
        7499, 5902, 3222, 3527, 399, 4567, 2814, 5565, 28, 10342, 2945, 2088, 2943, 1436, 7, 4061, 5049, 4681, 1588, 141, 608, 9658, 10020]
arr2 = [1758, 7552, 9687, 2945, 690, 7949, 1642, 10229, 3218, 748, 4665, 4536]

# nmap = {}

# for a in arr1:
#     if a in nmap:
#         print("duplicate detected")
#         nmap[a] = 0
#     if a not in nmap:
#         nmap[a] = 0
#     print("============", a, "==============")
#     for b in sorted(arr2):
#         print("b", b, "<", a, "a")
#         if b <= a:
#             print("yes")
#             nmap[a] += 1
#             print("nmap ======>", nmap[a])
#         else:
#             break
# print(nmap[4061])
# aa = []
# for k in arr1:
#     aa.append(nmap[k])


# def bisect_right(A, x):
#     lo, hi = 0, len(A)-1
#     while lo <= hi:
#         mid = (lo+hi)//2
#         if A[mid] <= x:
#             lo = mid+1
#         else:
#             hi = mid-1
#     return hi+1

# aa = []
# arr2.sort()
# for v in arr1:
#     lo, hi = 0, len(arr2)-1
#     while lo <= hi:
#         mid = (lo+hi)//2
#         if arr2[mid] <= v:
#             lo = mid+1
#         else:
#             hi = mid-1
#     # print(hi+1)
#     aa.append(hi+1)


class Solution:
    def countEleLessThanOrEqual(self, arr1, n1, arr2, n2):
        arr2.sort()
        res = []
        for e in arr1:
            res.append(bt.bisect(arr2, e))

        return res
