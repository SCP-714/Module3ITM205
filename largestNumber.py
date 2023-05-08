number_List = [1,2,3,4,5,6,7,8,9,10]
largest_Number = number_List[0]

for number in number_List:
    if number > largest_Number:
        largest_Number = number

print(largest_Number)