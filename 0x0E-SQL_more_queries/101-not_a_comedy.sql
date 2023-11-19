-- lists all shows of without Comedy in the database `hbtn_0d_tvshows`
-- no show Comedy 

	SELECT tv_shows.title AS title
	  FROM tv_shows
	 WHERE tv_shows.title NOT IN (
	SELECT tv_shows.title
	  FROM tv_shows
    INNER JOIN tv_show_genres
            ON tv_shows.id = tv_show_genres.show_id
    INNER JOIN tv_genres
	    ON tv_genres.id = tv_show_genres.genre_id
	 WHERE tv_show_genres.genre_id = 5)
      ORDER BY title ASC;
