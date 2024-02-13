MOD=10**9+7
def maxNiceDivisors(primeFactors):
    if primeFactors<=3:
        return primeFactors
    if primeFactors%3==0:
        return pow(3,primeFactors//3,MOD)
    elif primeFactors%3==1:
        return(pow(3,(primeFactors-4)//3,MOD)*4)%MOD
    else:
        return(pow(3,(primeFactors-2)//3,MOD)*2)%MOD
primeFactors=5
print("\nNumber of nice divisors = ",maxNiceDivisors(primeFactors))