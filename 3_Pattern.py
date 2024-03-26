def pattern(n):
    if n==0:
        return
    pattern(n-1)
    for i in range(1,n+1):
        print(i,end=" ")
    print()
def main():
    n=int(input("\nEnter the number of rows ="))
    pattern(n)
if __name__=="__main__":
    main()