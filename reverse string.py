
str = input("Enter a string")

# print(str[::-1])

#second method without builtin

res = ""

for char in str:
    res = char+res

print(res)