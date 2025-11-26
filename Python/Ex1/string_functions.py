a = "Good Morning Ed, Would you like brekkie"
print(len(a))

my_string = "Almost finished now folks!"
my_upper = my_string.upper()
my_lower = my_string.lower()
print(f"Original: {my_string}")
print(f"Upper: {my_upper}")
print(f"Lower: {my_lower}")

text_with_spaces = "   Ed Connolly   "
text_without_spaces = text_with_spaces.strip()
print(text_without_spaces)


text_with_brackets = "(((Ed Connolly)))"
text_without_brackets = text_with_brackets.strip("(")
text_without_brackets = text_without_brackets.strip(")")
print(text_without_brackets)