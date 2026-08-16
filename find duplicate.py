
def findduplicate(nums):
    n=len(nums)

    duplicates = []

    for i in range(n):
        for j in range(i+1,n):
            if nums[i]==nums[j] and nums[i] not in duplicates:
                duplicates.append(nums[i])
    return duplicates



nums=list(map(int,input("enter the numbers").split()))

result = findduplicate(nums)

if result:
    print("duplicate number",result)

else:
    print("There is no duplicate numbers")

