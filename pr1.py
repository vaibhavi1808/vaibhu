def sum_of_list(numbers):
    total=0
    for num in numbers:
        total+=num
    return total
    
def get_numbers_from_user():
    num_list=[]
    n=int(input("enter number of elements in the list="))

    for i in range(n):
        element=int(input("enter the element{}: ".format(i+1)))
        num_list.append(element)

    return num_list
        
numbers=get_numbers_from_user()
print("sum of the list is=",sum_of_list(numbers))
