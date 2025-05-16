#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for idx in range(list_length):
        try:
            if idx >= len(my_list_1) or idx >= len(my_list_2):
                raise IndexError
            if (not isinstance(my_list_1[idx], (int, float)) or
                    not isinstance(my_list_2[idx], (int, float))):
                raise TypeError
            division = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            result.append(division)
    return result
