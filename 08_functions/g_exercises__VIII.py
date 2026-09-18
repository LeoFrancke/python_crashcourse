# 8.8 User Albums

def make_album(artist, album):
    """Return a dictionary containing information about an album."""
    album_info = {
        'artist': artist.title(),
        'album': album.title(),
    }

    return album_info


while True:
    print("Please, provide information about an album:\nEnter 'q' to quit.\n")
    artist = input("Artist name: ")
    if artist == 'q':
        break

    album = input("Album name: ")
    if album == 'q':
        break

    album_dictionary = make_album(artist, album)
    print(album_dictionary, end='\n\n')

