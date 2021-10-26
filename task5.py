def tri_area(a,b,c):
    
    s = (a + b + c) / 2

    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return  round(area,2)

a = float(15)
b = float(22)
c = float(32)
tri_area(a,b,c)