DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY, 
    album_name VARCHAR(255),
    artist_id INT NOT NULL REFERENCES artists(id) ON DELETE CASCADE
);

INSERT INTO artists (name)
VALUES ('Olly Murs');

INSERT INTO albums (album_name, artist_id)
VALUES ('Marry Me', 1);




