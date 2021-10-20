a = float(15)
b = float(14)
c = float(12)

x = (a + b + c) / 2

# calculating the area to two decimal 
area = (x*(x-a)*(x-b)*(x-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)