def square_numbers(numbers):
    square_list=[]
    for num in numbers:
        squared_list=[]
    return squared_list

def get_numbers_from_user():
    num_list=[]
    n=int(input("enter number of element in the list="))

    for i in range(n):
        element=float(input("enter element{}=".format(i+1)))
        num_list.append(element) 

    return num_list

numbers=get_numbers_from_user()
for i in range(len(numbers)):
    squared_number=numbers[i]**2
    print(f"{numbers[i]} \t \t {squared_number}")      
          
