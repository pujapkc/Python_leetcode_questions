


def findcommonprefix(lst):
    if not lst:
        return ""


    prefix= lst[0]

    for s in lst[1:]:
        while not s.startswith(prefix):
            prefix=prefix[:-1]

            if not prefix:
                return ""

    return prefix



lst = input("Enter words to check longest common prefix ").split()

res=findcommonprefix(lst)

if res:
    print("Longest common prefix ",res)

else:
    print("No common prefix")