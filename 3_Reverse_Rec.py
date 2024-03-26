def r_num(n,reversed_num=0):
    if n==0:
        return reversed_num
    else:
        return r_num(n//10,reversed_num*10+n%10)
def main():
    num=int(input("\nEnter a number = "))
    rev_num=r_num(num)
    print("\nReversed number = ",rev_num)
if __name__=="__main__":
    main()