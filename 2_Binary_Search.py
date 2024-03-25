def binarysearch(a,x):
    l,r=0,len(a)-1    
    while l<=r:
        mid=l+(r-l)//2
        if a[mid]==x:
            return mid
        elif a[mid]<x:
            l=mid+1
        else:
            r=mid-1
        return -1
def main():
    a=list(map(int,input("\nEnter the elements in sorted order = ").split()))
    x=int(input("\nEnter the element to search = "))
    result=binarysearch(a,x)
    if result==-1:
        print("\nElement is not present in array")
    else:
        print(f"\nElement is present at {result}")
if __name__=="__main__":
    main()