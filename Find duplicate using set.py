def finddupli(s):
    seen=set()
    dups=set()

    for i in s:
        if i in seen:
            dups.add(i)

        seen.add(i)


    return list(dups)

s=list(map(int,input("enter the numbers ").split()))

res = finddupli(s)

if res:
    print("Duplicate numbers are :",res)

else:
    print("There are no duplicate numbers")