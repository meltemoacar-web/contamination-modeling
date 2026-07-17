#Calculations used to find FWHM in the voigt_profile.py file. 
import numpy as np

def find_max(x,y):

    y_max = y.max()

    ymax_indices = []

    for index, i in enumerate(y):

        if abs(i - y_max) <= 0.0001:
            ymax_indices.append(index)

    x_max=[]
    for i in  ymax_indices:
        x_max.append(x[i])


    print(f"x_max {x_max} y_max {y_max}")    
    return x_max[0],y_max

#####################################################

def find_half(x,y,y_max):

    '''
    Given x, y, x_max,y_max returns the half values of max
    These are to calculate the full width half maximum, when you run the program it will give you some points. Thats what this is. This is only calculating the points on the voigt profile graph though.

    '''

    y_max_half = y_max/2

    half_indices = []

    for index, yy in enumerate(y):
        #print(f" delta:{abs(yy - y_max_half)}")
        if abs(yy - y_max_half) <= 0.001:
            half_indices.append(index)

    x_max_half=[]
    for i in  half_indices:
        x_max_half.append(x[i])
       
    print(f"x_max_half:{x_max_half} y_max_half:{y_max_half}")

    return x_max_half, y_max_half

