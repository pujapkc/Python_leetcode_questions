
def palin(s):
    s=s.lower()

    return s == s[::-1]



s=input("Enter a string ")

res=palin(s)

if res:
    print("String is palindrome")

else:
    print("string is not palindrome")
