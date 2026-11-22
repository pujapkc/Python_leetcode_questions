from collections import Counter


def wordappear(s):
    words = s.lower().split()
    return dict(Counter(words))


s=input("enter a string ")

res=wordappear(s)

print(res)
