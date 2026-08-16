
def twosum(nums,target):
    n=len(nums)

    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]

    return []





nums = list(map(int,input("enter the numbers separated by space").split()))

target = int(input("Enter the target number"))

result=twosum(nums,target)

if result:
    print("indices are",result)
else:
    print("there is no pair")

