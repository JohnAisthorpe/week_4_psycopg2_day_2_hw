# Use this file to test your repository functions 
import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository



#instances of album class

album_1 = Album("Midnights", "Taylor Swift")

album_repository.save(album_1)

# album_repository.delete_all()

print(album_repository.select(5).__dict__)

artist_1 = Artist("Michael Buble")

artist_repository.save(artist_1)

# artist_repository.delete_all()

print(artist_repository.select(4).__dict__)




