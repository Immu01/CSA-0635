def find_factors(n,divisor=1,factors=[]):
    if divisor>n:
        return factors
    if n%divisor==0:
        factors.append(divisor)
    return find_factors(n,divisor+1,factors)
if __name__=="__main__":
    n=int(input("\nEnter a number = "))
    factors=find_factors(n)
    print("\nFactors of ",n," are = ",factors)