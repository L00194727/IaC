def find_even_nm(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number % 2 == 0:
            return True
        else:
            pass
    else:
        return False

result = find_even_num([1,2,3,4,5,6,7,8], 9)
print(result)