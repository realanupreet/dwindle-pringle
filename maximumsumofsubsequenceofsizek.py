# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

arr = [2, 1, 5, 1, 3, 2]
k = 3

wstart = 0  # window start
wsum = 0  # window sum
maxsum = 0

for wend in range(0, len(arr)):
    wsum += arr[wend]
    if wend >= k-1:
        maxsum = max(maxsum, wsum)
        print(wstart)
        wsum -= arr[wstart]
        wstart += 1
