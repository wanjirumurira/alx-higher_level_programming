#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    sum = 0
    y_total = 0
    for x, y in my_list:
        sum += (x*y)
        y_total += y
    return (sum/y_total)
