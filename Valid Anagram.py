s=input("Enter the first string")

t=input("enter the second string")

if len(s)!=len(t):
    print("Strings are not anagram")

elif sorted(s)== sorted (t):
    print("Both Strings are anagrams")

else:
    print("Strings are not anagram")