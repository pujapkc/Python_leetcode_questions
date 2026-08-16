
def group_anagrams(words):
    groups={}

    for word in words:
        key="".join(sorted(word))

        if key in groups:
           groups[key].append(word)

        else:
            groups[key] = [word]

    return list(groups.values())





n=int(input("enter the number of inputs"))

words = []

for i in range(n):
    words.append(input("enter word"))

print(group_anagrams(words))