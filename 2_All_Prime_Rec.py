def is_prime(n,divisor=2):
    if n<=2:
        return n==2
    if n%divisor==0:
        return False
    if divisor*divisor>n:
        return True
    return is_prime(n,divisor+1)
def prime(n,current=2):
    if current>n:
        return []
    if is_prime(current):
        return [current]+prime(n,current+1)
    return prime(n,current+1)
limit=int(input("\nEnter the limit to generate prime numbers = "))
print("\nPrime numbers up to",limit,"are = ",prime(limit))