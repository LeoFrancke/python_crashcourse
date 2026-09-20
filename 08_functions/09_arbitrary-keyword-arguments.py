# The double asterisk cause Python to create a dictionary named user_info,
# containing all the name-value pairs the function receives.

def build_profile(first, last, **user_info):
    """Build a dictionary for a user profile."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user)




