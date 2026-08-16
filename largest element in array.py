def findmax(nums):
    if not nums:
        return ""

    res = nums[0]

    for i in nums:
        if i>res:
            res = i

    return res


nums = list(map(int,input("Enter the nums").split()))

result = findmax(nums)

print("largest number",result)