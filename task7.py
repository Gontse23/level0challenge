#Celcius to Fahrenheit function
def temp_celcius(temp):
    cel = (temp*1.8)+32
    print("Temp in Fahrenheit = {:.2f}" .format(cel))

#Fahrenheit to Celcius function
def temp_far(temp):
    fahren = (temp*1.8)+32
    print("Temp in Celcius = {:.2f}" .format(fahren))
temp_far(17)