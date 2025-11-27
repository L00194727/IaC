my_list = ["one", "two", "three"]
my_tuple = ("one", "two", "three")
print(type(my_list))
print(type(my_tuple))

print()
my_tuple = ("one", "two", "three", "one")
# How many times does "one" occur in tupple
print(my_tuple.count("one"))
# At what posiion is first occurance of "one"
print(my_tuple.index("one"))