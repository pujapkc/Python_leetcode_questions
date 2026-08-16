
def runningSum(nums):
    sum=0
    res = []


    for i in nums:
        sum=sum+i
        res.append(sum)

    return res





nums = list(map(int,input("enter the elements").split()))

result = runningSum(nums)

print(result)