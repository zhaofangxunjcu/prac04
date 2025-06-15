"""
CP1404/CP5632 Practical
List comprehensions
"""
names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]
# TODO: list comprehension to create a list of all the full_names in lowercase format
# lowercase_full_names =
lowercase_full_names = [name.lower() for name in full_names]
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# TODO: list comprehension to create a list of integers from the above list of strings
# numbers =
numbers = [int(s) for s in almost_numbers]
# TODO: list comprehension to create a list of only the numbers that are
# greater than 9 from the numbers (not strings) you just created
greater_than_nine = [n for n in numbers if n > 9]
# TODO: (more advanced) use a list comprehension and the join string method
# to create a string (not list) of the last names for those full names longer than 11 characters
# the result should be: 'Harlem, Hendrix, Lovelace'
long_last_names = ", ".join(name.split()[1] for name in full_names if len(name) > 11)