my_list = [1,2,3,4,"A"]
a = len(my_list)
print(a)
slice_l = my_list[1:3:1]
print(slice_l)
my_character = my_list[-1]
print(my_character)


print()
my_list_1 = [1,2,3,4,"A"]
my_list_2 = ["S", "T", "Fish",9,10]
concatenated_list = my_list_1 + my_list_2
print(concatenated_list)



print()
my_list_1 = [1,2,3,4,"A"]
my_list_2 = ["S", "T", "Fish",9,10]
concatenated_list = (my_list_1,my_list_2)
print(concatenated_list)

print()
my_list_1 = [1,2,3,4,"A"]
print(my_list_1)
my_list_1[2] = "Chips"
print(my_list_1)


print()
my_list = ["One", "Two", "Three"]
print(my_list)
my_list.append("Four")

print()
my_string = "12/9/22, 14:30, System Start, UB2204-Server"
list_of_values = my_string.split(",")
print(list_of_values)