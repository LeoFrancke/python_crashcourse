def get_character_record(name, server, level, rank):
    return {
            'name': name,
            'server': server,
            'level': level,
            'rank': rank,
            'id': f"{name}#{server}",
            }

print('initializing server...')
character = get_character_record('leofrancke', 'brazil_sp', 27, 'apprentice')

print(character)
print('shutting down server...')


