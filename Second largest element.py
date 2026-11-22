def secondlarge(nums):
    largest = nums[0]
    secondlargest = float('-inf')

    for i in range(len(nums)):
        if nums[i]>largest:

            secondlargest = largest
            largest=nums[i]

        elif nums[i]<largest and nums[i]>secondlargest:
            secondlargest = nums[i]

    if secondlargest == float('-inf'):
        return -1

    return secondlargest



s=list(map(int,input("Enter a list of numbers ").split()))

res = secondlarge(s)

print("Second largest",res)