# from itertools import count

str = input("Enter a string")

count={}

for char in str:
    count[char] = count.get(char,0)+1

for char in str:
    if count[char]==1:
        print("first unique char",char)
        break
else:

    print("no unique char")