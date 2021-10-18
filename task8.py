time = float(input("time in minutes:"))
hour=time//60
time%=60
minutes = time//60 
time%=60
print("h:m->%d:%d"%(hour,minutes))