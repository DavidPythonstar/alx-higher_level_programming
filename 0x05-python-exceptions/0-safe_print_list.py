#!/usr/bin/python3

def safe_print_list(my_list=None, x=0):
    """Function that prints elements in a list up to a certain index.
    Args:
    my_list: list to be printed
    x: the index up to which the list elements will be printed
    """
    lst = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}",end="")
            lst += 1
        except IndexError:
            break
    return lst 

