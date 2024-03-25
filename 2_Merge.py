def merge_sort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    l_half=a[:mid]
    r_half=a[mid:]
    l_half=merge_sort(l_half)
    r_half=merge_sort(r_half)
    return merge(l_half,r_half)
def merge(l,r):
    result=[]
    l_index = 0
    r_index = 0
    while l_index<len(l) and r_index<len(r):
        if l[l_index]<r[r_index]:
            result.append(l[l_index])
            l_index+=1
        else:
            result.append(r[r_index])
            r_index+=1
    result.extend(l[l_index:])
    result.extend(r[r_index:])    
    return result
try:
    n=int(input("\nEnter the number of elements in the array = "))
    arr=[]
    for i in range(n):
        element=int(input(f"\nEnter element {i + 1} = "))
        arr.append(element)   
    print("\nOriginal array = ",arr)
    sorted_a=merge_sort(arr)
    print("\nSorted array = ",sorted_a)
except ValueError:
    print("\nError")