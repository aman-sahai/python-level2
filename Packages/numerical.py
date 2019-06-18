# Prime Numbers
def Prime(n):
    c=0
    if n == 2:
        return True
    for i in range(2,n//2 + 1):
        if n % i == 0:
            c=1
            return False
    if c == 0:
        return True
Prime(71)

# Number of Prime factors
def PrimeFactors(N):
    if Prime(N):
        return 1
    c=0
    for i in range(2,N//2+1):
        if N % i == 0 and Prime(i):
            c+=1
    return c
PrimeFactors(10) # 2,5

