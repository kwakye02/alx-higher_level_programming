#!/usr/bin/python3

def print_list_integer(my_list=[]):
	""" Prints integers from a list"""
    for i in range (len(my_list)):
        print("{:d}".format(my_list[i]))
