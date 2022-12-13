DROP TABLE IF EXISTS albums;

CREATE TABLE albums (
    id SERIAL PRIMARY KEY, 
    album_name VARCHAR(255),
    artist_name VARCHAR(255)
);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255)
);

INSERT INTO albums (album_name, artist_name)
VALUES ('Marry Me', 'Olly Murs');

INSERT INTO artists (name)
VALUES ('Olly Murs');



