def find_even_num(number_list: list)->bool:
    for iterate_number in number_list:
        if iterate_number % 2 == 0:
            return True
        else:
            pass
    else:
        return False

result = find_even_num([1,2,3,4,5,6,7,8])
print(result)



volume = lambda r, h: 3.14 * r**2 * h

# Example usage
print(volume(3, 5))   # radius = 2, height = 5
