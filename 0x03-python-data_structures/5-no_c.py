#!/usr/bin/python3
def no_c(my_string):
    copy = [j for j in my_string if j != 'c' and j != 'C']
    return ("".join(copy))
