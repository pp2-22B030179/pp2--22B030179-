string = input()

modified_string = ""
for char in string:
    if char.isalnum():
        modified_string += char
    else:
        modified_string += "-"
print(modified_string)
