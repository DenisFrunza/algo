def solution(nums):
    if nums == []:
        return 0
    if len(nums) == 1:
        return nums[0]

    res = [0] * len(nums)
    res[0] = nums[0]
    res[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        res[i] = max(res[i-1], res[i-2]+ nums[i])
    return res[-1]


print(solution(nums=[ 1, 3, 4, 4, 3, 3, 7, 2, 3, 4, 5, 1 ]))
