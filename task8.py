def convert_decimal(minutes):
    hours = minutes // 60
    minutes%= 60
    if minutes==1 and hours==1:
        return"%d hour,%02d minute" % (hours, minutes)
    if hours==1 and minutes>1:
        return"%d hour,%02d minutes" % (hours, minutes)
    if minutes==1 and hours>1:
        return"%d hours,%02d minute" % (hours, minutes)
    else:
        return "%d hours,%02d minutes" % (hours, minutes)
print(convert_decimal(260))