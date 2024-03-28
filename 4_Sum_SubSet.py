def print_subsets(set,n,target,subset,subset_size,sum):
    if sum==target:
        print("{",end="")
        for i in range(subset_size):
            if subset[i]:
                print(set[i],end=" ")
        print("}")
        return
    if n==0 or sum > target:
        return
    subset[subset_size]=True
    print_subsets(set,n-1,target,subset,subset_size+1,sum+set[n-1])
    subset[subset_size]=False
    print_subsets(set,n-1,target,subset,subset_size,sum)
def subset_sum(set,target):
    subset=[False]*len(set)
    print_subsets(set,len(set),target,subset,0,0)
if __name__=="__main__":
    set=[12,23,34,45,56,67,78,89,90]
    target=34
    print(f"\nSubsets with sum equal to {target} are = ")
    subset_sum(set,target)