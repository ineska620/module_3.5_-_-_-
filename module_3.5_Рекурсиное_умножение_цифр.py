def get_multiplied_digits(number):
    str_number = str(number) #
    if len(str_number) > 1: # если длина  больше 1
        first = int(str_number[0]) # берем 1 значение, только уже цифру
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)
result = get_multiplied_digits(40203)
print(result)
#get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3
