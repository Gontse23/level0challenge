time = float(120)
hour=time//60
time%=60
minutes = time//60 
time%=60
print("h:m->%d:%d"%(hour,minutes))