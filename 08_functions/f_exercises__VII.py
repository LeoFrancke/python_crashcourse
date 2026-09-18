# 8.7 Album

def make_album(artist, album, number_of_songs=None):
    """Return a dictionary containing information about an album."""
    album_info = {
        'artist': artist.title(),
        'album': album.title(),
    }

    if number_of_songs:
        album_info['number_of_songs'] = number_of_songs

    return album_info


album_1 = make_album('stratovarius', 'episode', 12)
album_2 = make_album('stratovarius', 'elements')
album_3 = make_album('stratovarius', 'polaris', 11)
album_4 = make_album('symphony x', 'the odyssey')
print(album_1)
print(album_2)
print(album_3)
print(album_4)

