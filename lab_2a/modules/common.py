import datetime
import sys


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

def filter (filter):
    num=range(0,101)
    if filter=="True":
        m = "even numbers: " 
    elif filter=="False":
        m = "odd numbers: "

    for index in num:
        if (filter == "True") & (num[index]%2 == 0):
            m += str(num[index]) + " "
        elif (filter == "False") & (num[index]%2 != 0):
            m += str(num[index]) + " "
    return m


