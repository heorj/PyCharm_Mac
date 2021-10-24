number_string = ''
while number_string.isdigit() == False:
    number_string = input('Enter a number!')
print('Fine!', int(number_string))