"""
This module provide functions to deal with navigation in json file
"""
import json


def read_from_json_file(file_name: str) -> dict:
    """
    Read data from json file
    """
    with open(file_name, "r", encoding="utf-8") as file:
        decoded_file = json.load(file)
    return decoded_file


def navigation(file_name: str):
    """
    This is a main function of this project, it navigates in json file
    Cause the json object is very similar to filesystem ierarchy, our
    navigation behave the same way. This function have 4 operating modes:
    1)'b' - Break, that is end of program
    2)'w' - Write, return the object, in which we are right now
    3)'u' - move Up, we are returning to the previous object
    4)'d' - move Down, we are moving to the one key(or index) of object(if it is
    possible)
    """
    json_file = read_from_json_file(file_name)
    obj = json_file
    route = []
    print('Our program have 4 operating modes to navigate in json file')
    print('You need to enter appropriate letter to run mode')
    print('1)b - stop program')
    print('2)w - show contents of object in which you are right now')
    print('3)u - move to the previous object(which is "above")')
    print('4)d - you choose object to which we will move')
    while True:
        if isinstance(obj, list):
            print('Object, on which you are right now,is list. It have {} indices'.format(len(obj)))
            print('You can activate all operating modes')
        elif isinstance(obj, dict):
            print('Object, on which you are right now, is dict')
            print('You can activate all operating modes')
            print('If you activate "d"-mode, you will choose from following keys:')
            print(obj.keys())
        else:
            print('Object, on which you are right now, is {}'.format(type(obj)))
            print('You can activate all modes, except "d"-mode.')
        mode = input('Please, enter mode with which you want to work:')
        if mode == "b":
            break
        elif mode == "w":
            print(obj)
        elif mode == "u":
            obj = route[-1][1]
            route.pop()
        elif mode == "d":
            pointer = input("Please, enter key/index of object, in which you want to go:")
            if isinstance(obj, list):
                pointer = int(pointer)
            route.append((pointer, obj))
            obj = obj[pointer]
        else:
            print("You entered incorrect mode. Please try again")


if __name__ == "__main__":
    file_name = input("Please, enter a file_name:")
    navigation(file_name)
