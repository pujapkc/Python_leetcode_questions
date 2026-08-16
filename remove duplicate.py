
# #first method
nums=list(map(int,input("Enter space separated numbers").split()))
#
# res = list(set(nums))
#
# print(res)

#second method

# res = list(dict.fromkeys(nums))
#
# print(res)

#third method

res  = []

for i in nums:
    if i not in nums:
        res.append(i)

print(res)




