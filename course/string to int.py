numbers_string = input('>>>') #1,2,3,4,5
numbers_string_list= numbers_string.split(',')
numbers = [int(number) for number in numbers_string_list]
print(numbers)

while number_string.isdigit() == False:
    number_string = input('Enter a number!')
print('Fine!', int(number_string))