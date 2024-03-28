def insert_number(lst,number,index):
    lst.insert(index,number)
if __name__=="__main__":
    my_list=[10,20,30,50,60,70,80,90,100]
    number_to_insert=40
    insertion_index=3
    insert_number(my_list,number_to_insert,insertion_index)
    print("\nList after insertion = ",my_list)