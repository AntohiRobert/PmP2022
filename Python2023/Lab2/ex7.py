def is_palindrome(n):
    digits=[]
    while n>0:
        digits.append(n%10)
        n=(n-n%10)/10
    l=len(digits)
    for i in range(0,l-1):
        if (digits[i]!=digits[l-i-1]):
            return False
    return True

def palindromes(list):
    bp=0
    np=0
    for elem in list:
        if is_palindrome(elem):
            np=np+1
            bp=max(bp,elem)
    ans=(np,bp)
    return ans


print(palindromes([123,1,12321,121]))