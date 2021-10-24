n_1 = float(input("Enter the first number " ))
n_2 = float(input("Enter the second number "))
operation = input('Select operation whitch might be one of following: + - * / ')

result= None
error = None

if operation == '+':
 result = n_1+n_2

elif '-' == operation:
    result = n_1-n_2

elif operation == '*':
    result = n_1*n_2

elif operation == "/":
    if n_2 != 0:
        result = n_1 / n_2

    else: error = 'we cant divide on ZERO'

if error != None:
    print(error)

else: print(int(result))

