# 8.13 User profile

def build_profile(first, last, **user_info):
    """Build a dictionary for a user profile."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user = build_profile('leo', 'francke', location='campinas', favorite_lang='c++')
print(user)

