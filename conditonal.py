shape = input('Enter shape: ')
area = 0


if shape == 'circle':
    radius = int(input('Please enter the radius '))
    area = ((radius+radius)*(radius+radius))*3.14
elif shape == 'triangle':
    side = int(input('Enter side of your equilateral triangle ')) ##h = а² - (а/2)²
    h= side*side -((side/2)*(side/2))
    area = h*side/2
elif shape == "square":
    side= int(input("Enter side of your sqaure " ))
    area= side*side



if area >= 100:
 print("It's BIG ", shape)    #S = a*h/2

else: print("It's not BIG ",shape)




