numbers = [1,2,2,3,4,5,5,6,7,8,8]
number_list = []

for number in numbers:
    if number not in number_list:
        number_list.append(number)
print(number_list)