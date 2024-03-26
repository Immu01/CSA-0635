def is_perfect(n):
    sum_divisors=0
    for i in range(1,n):
        if n%i==0:
            sum_divisors+=i
    return sum_divisors==n
def main():
    num=int(input("\nEnter a number = "))
    if is_perfect(num):
        print("The number ",num," is perfect")
    else:
        print("The number ",num," is not perfect")
if __name__=="__main__":
    main()