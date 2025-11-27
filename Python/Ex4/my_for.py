iterable_variable = [1,2,3,4,5,6]

for item in iterable_variable:
    # For each item, execute this code block
    print(item)



print()
iterable_variable = [1,2,3,4,5,6]

for item in iterable_variable:
    if item % 2 != 0:
        print(item)

print()
iterable_variable = [1,2,3,4,5,6]
total = 0

for item in iterable_variable:
    total = total + item

print(total)
