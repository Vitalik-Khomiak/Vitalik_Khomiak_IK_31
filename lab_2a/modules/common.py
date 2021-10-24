import datetime
import sys
import logging
import numpy
import random

def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def filter(filter):
    numbers=range(0,101)
    if filter=="True":
    	msg = "paired elements: " 
    elif filter=="False":
    	msg = "odd elements: "
    
    for index in range(0, len(numbers)):
    	if (filter == "True") & (numbers[index]%2 == 0):
    	    msg += str(numbers[index]) + " "
    	elif (filter == "False") & (numbers[index]%2 != 0):
    	    msg += str(numbers[index]) + " "
    return msg

def s_arr():
    y = 200
    z = 11
    x=[random.randint(1, y)
       for i in range(z)]      
    print("arrray X[]:", x)
    index = int(input("Press element num: "))
    try:
    	print(f"X[{index}] = {x[index]}")
    	print('------------------------------------')
    except IndexError:
        logging.error("Num must be in range 0-%s", z-1)
    else:
    	logging.info("\nNice \n-_- -_- -_-")
