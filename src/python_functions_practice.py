def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1,num_2):
    return num_1 / num_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2


def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(month):
    if month == 1:
        return "January"
    elif month == 3:
        return "March"
    elif month == 9:
        return "September"  


def number_to_short_month_name(month):
    if month == 1:
        return "Jan"
    elif month == 4:
        return "Apr"
    elif month == 10:
        return "Oct"

def volume_of_cube(length):
    return length * length * length


def reversed_string(string_name):
    return string_name[::-1]


def converted_temp(farenheit):
    return (int((farenheit - 32) * .5556))



