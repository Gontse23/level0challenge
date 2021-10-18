a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

x = (a + b + c) / 2

# calculating the area to two decimal 
area = (x*(x-a)*(x-b)*(x-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)