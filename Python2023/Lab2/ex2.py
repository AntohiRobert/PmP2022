def is_prime(n):
    if n==1:
        return False
    ok=True
    i=2
    while i*i<=n:
        if n%i==0:
            ok=False
        i=i+1
    return ok

def get_primes(list):
    ans=[]
    for i in list:
        if (is_prime(i)):
            ans.append(i)
    return ans


print(get_primes([1,2,3,4,5,6,7,8,9,10]))