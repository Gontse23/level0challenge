#Celcius to Fahrenheit function
temp= 35
def temp_celcius(temp):
    cel = (temp*1.8)+32
    return ("Temp in Fahrenheit = {:.2f}" .format(cel))

#Fahrenheit to Celcius function
def temp_far(temp):
    fahren = (temp-32)/1.8
    return ("Temp in Celcius = {:.2f}" .format(fahren))
temp_celcius(temp)