#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for number in range(x):
            print(my_list[number], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
