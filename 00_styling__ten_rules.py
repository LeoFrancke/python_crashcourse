""" Convention for styling python code:
[https://peps.python.org/pep-0008/]

    The 10 Most Important Style Rules (PEP 8)
"""

# se estiver com pressa, isso vale mais que as 10 regras juntas:
# if u'r in a hurry, this is worth more than the 10 rules combined:
print('READABILITY COUNTS.')
print("Don’t follow style rules blindly if doing so hurts readability.")

# Rule 1. indentation: 4 spaces
# Rule 2. variables and functions: snake_case

""" Rule 3. spaces around operators + - * / = >= <= etc

    If operators with different priorities are used, consider adding whitespace 
    around the operators with the lowest priority(ies). Use your own judgment; 
    however, never use more than one space, and always have the same amount 
    of whitespace on both sides of a binary operator:
    """
# Correct:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)


# Rule 4. Limit lines to ~88 chars
# Rule 5. Import order matters. One per line. Wildcards make code harder to understand; avoid
# Correct:
import os
import sys
# Not recommended:
from math import *

# Rule 6. Use meaningful variable names

# Rule 7. Don't use None with ==
# Use 'is not' operator rather than 'not ... is':
# Correct:
if player is None:
if foo is not None:
# Wrong:
if player == None:
if not foo is None:


# Rule 8. Use Truthiness Properly
# Correct:
if greeting:
# Wrong:
if greeting == True:

# Also:
if players:
# Not:
if len(players) > 0:

# And:
if not players:
# Not:
if len(players) == 0:


# Rule 9. Small Functions: more readability and testability.
# Bad:
def process_game():
    # 200 lines of logic

#Better:
def process_game():
    update_players()
    process_combat()
    update_world()


# Rule 10. Function Parameters
# Add 4 spaces (an extra level of indentation) to distinguish parameters.
def function_name(
        parameter1, parameter2,
        parameter3, parameter4
        ):
    print('function code block')
    return None




### BONUS ###
# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)


# Use ''.startswith() and ''.endswith() instead of string slicing to check for prefixes or suffixes.
# startswith() and endswith() are cleaner and less error prone:
# Correct:
if foo.startswith('bar'):
# Wrong:
if foo[:3] == 'bar':


