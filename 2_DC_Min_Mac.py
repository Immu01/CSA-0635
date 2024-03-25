def find_max_min(a,low,high):
    if low==high:
        return a[low],a[low]
    if high==low+1:
        return (a[low],a[high]) if a[low]<a[high] else (a[high],a[low])
    mid=(low+high)//2
    left_max,left_min=find_max_min(a,low,mid)
    right_max,right_min=find_max_min(a,mid+1,high)
    return max(left_max,right_max),min(left_min,right_min)
n=int(input("\nEnter the number of elements = "))
a=[]
print("\nEnter the elements = ")
for i in range(n):
    a.append(int(input()))
max_val,min_val=find_max_min(a,0,len(a)-1)
print("\nMaximum element = ",max_val)
print("\nMinimum element = ",min_val)