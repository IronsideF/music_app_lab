import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Elton John')
artist_2 = Artist('Adele')
artist_repository.save(artist_1)
artist_repository.save(artist_2)
album_1 = Album('Goodbye Yellow Brick Road', 'Pop', artist_1,)
album_2 = Album('21', 'Pop', artist_2)
album_3 = Album('25', 'Pop', artist_2)
album_4 = Album('30', 'Pop', artist_2)
album_5 = Album('Madman Across the Water', 'Pop', artist_1)
album_6 = Album('The Lockdown Sessions', 'Pop', artist_1)
album_repository.save(album_1)
album_repository.save(album_2)
album_repository.save(album_3)
album_repository.save(album_4)
album_repository.save(album_5)
album_repository.save(album_6)

results = album_repository.artist_albums(artist_1)

for album in results:
    print(album.__dict__)

# Elton = artist_repository.select(artist_1.id)
# _21 = album_repository.select(album_2.id)

# print(Elton.__dict__)
# print(_21.__dict__, _21.artist.__dict__)

# all_artists = artist_repository.select_all()
# all_albums = album_repository.select_all()
# for artist in all_artists:
#     print(artist.__dict__)
# for album in all_albums:
#     print(album.__dict__)