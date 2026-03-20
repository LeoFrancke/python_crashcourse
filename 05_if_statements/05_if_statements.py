# When you understand conditional tests, you can start using if statements.

if True:
    # do something that is inside this indented code block
    pass

else:
    # do this other code block ONLY if the first condition is false
    # 'Else' is not mandatory.
    pass


# elif => else, if...
#         it creates another condition.
bitcoin = 70_000_000
if bitcoin < 60_000_000:
    buy()
elif bitcoin >= 60_000_000 and bitcoin < 65_000_000:
    pass
elif bitcoin >= 66_000_000 and bitcoin < 72_000_000:
    print('Uncertain move. Wait before taking a decision.')
    pass
elif bitcoin > 100_000_000:
    pass
else:
    print('in case every test fails, this line will be executed.')

