import random
n_1 = random.randint(0,300)
n_2 = random.randint(0,300)

result = input(str(n_1)+ '+' +str(n_2)+ '=')
if str(n_1 + n_2) == result:
    print('Correct')
else:
    print ('Incorrect')
