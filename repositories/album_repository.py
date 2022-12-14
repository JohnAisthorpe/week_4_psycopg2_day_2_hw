from db.run_sql import run_sql
from models.album import Album

def save(album):
    sql = "INSERT INTO albums (album_name, artist_id) VALUES (%s, %s) RETURNING *"
    values = [album.album_name, album.artist.id]

    results = run_sql(sql, values)

    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        album_data = results[0]
        album = Album(album_data['album_name'], album_data['artist'])

        return album

    