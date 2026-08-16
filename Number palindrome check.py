def palindrome(x):
    if x<0:
        return False

    temp=x

    rev = 0

    while x>0:
        digit = x%10
        rev = rev*10+digit
        x=x//10

    return temp == rev

x=int(input("Enter a number"))

res = palindrome(x)

if res:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
