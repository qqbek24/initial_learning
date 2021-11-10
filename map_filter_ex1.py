# ****_map filter examples
# ****_Autor: Jakub Koziorowski

input_data = [i for i in range(10)]
print(input_data)

x = [i for i in range(20)]

def is_even(number):
    if number % 2:
        return True
    else:
        return False


filter_data = filter(is_even, x)
print(list(filter_data))