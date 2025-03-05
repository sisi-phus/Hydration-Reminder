from datetime import datetime


def bind(var,min,max):
    if var > max:
        return max
    if var < min:
        return min
    return var

def get_time():
    cHour = datetime.now().hour

    hour = 3600
    minute = 60
    second = 1


    penaltymeasure = cHour - 6
    penaltymeasure = bind(penaltymeasure, 0, 6)
    penalty = 15*minute*penaltymeasure


    timer = 2*hour-penalty
    return timer
    