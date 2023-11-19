-- lists all genres of the show using the database `hbtn_0d_tvshows`
-- show Dexter genres 

    SELECT tv_genres.name AS name
      FROM tv_genres
INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
        ON tv_shows.id = tv_show_genres.show_id
     WHERE tv_shows.id = 8
  ORDER BY name ASC;
