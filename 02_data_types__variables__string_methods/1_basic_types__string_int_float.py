### DATA TYPES ###

# prefer to explicitly show the data Type
# > it improves readability and creates good habits for low level languages.

# Strings: text, surrounded by quotes
string_1: str = "this is a string"
string_2: str = 'also a string'

# Numbers: integers and "rational numbers"...
#   numbers with decimals are called Float numbers.
integer: int = 27
float_number: int = 3.1415

# Boolean: can be only True or False.
bool_1: bool = True
bool_2: bool = False

# NoneType: Not all variables have a value.
#  We can make an "empty" variable by setting it to None.
#  None is a special value in Python that represents the absence of a value.
#  It is not the same as zero, False, or an empty string.
empty_variable: str | None = None
age_empty: int | None = None

""" So when would you use it? One use case is to represent that a value hasn't been 
                                                                        determined yet. 
    E.g., an uncaptured input. Maybe your program is waiting for a user to enter 
                                                                            their name. 
    You might start with a variable: username = None
"""
