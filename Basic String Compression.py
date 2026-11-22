def compressionstring(s):

    count = 1
    result = ""

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count+=1

        else:
            result+=s[i-1]+str(count)
            count=1

    if len(s)>0:
        result+=s[-1]+str(count)

    return result



s=input("Enter the string")

print(compressionstring(s))