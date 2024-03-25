def copy_str(source,destination,index=0):
    if index==len(source):
        return destination
    destination+=source[index]
    return copy_str(source,destination,index+1)
source_str="Hello world"
destination_str=""
copied_str=copy_str(source_str,destination_str)
print("\nCopied string = ",copied_str)