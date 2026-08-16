
str = input("enter a string").split()

print(str)

res = ""

for s in str:
    res=s+" "+res

print(res)