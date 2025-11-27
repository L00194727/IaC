my_dictionary = {"FName":"Ed", "SName":"Connolly", "Occupation":"Rocket Scientist"}
print("Works as a " + my_dictionary["Occupation"])
print(my_dictionary)

# Add a key value pair
print()
my_dictionary["Salary"] = "Not Enough"
print(my_dictionary)

#Edit one value
print()
my_dictionary["Occupation"] = "Brain Surgeon"
print(my_dictionary)

print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())