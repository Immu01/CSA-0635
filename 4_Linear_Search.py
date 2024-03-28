def linear_search(a,find):
    for i in range(len(a)):
        if a[i]==find:
            return i
    return -1
a=[12,23,34,45,56,67,78,89]
find=56
index=linear_search(a,find)
if index!=-1:
    print(f"{find} is at index {index}")
else:
    print(f"{find} is not found")