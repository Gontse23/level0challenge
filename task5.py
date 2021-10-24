def tri_area(a,b,c):
    
	s = (a + b + c) / 2

	area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
	print('Triangle area is %0.2f' %area)

a = float(15)
b = float(14)
c = float(12)
tri_area(a,b,c)
