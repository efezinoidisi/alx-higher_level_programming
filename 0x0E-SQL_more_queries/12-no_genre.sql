-- lists all shows contained im hbtn_0d_tvshow without a genre linked

SELECT shows.title, genres.genre_id FROM tv_shows AS shows
       LEFT JOIN tv_show_genres AS genres ON shows.id = genres.show_id
       WHERE genres.genre_id IS NULL
       ORDER BY shows.title, genres.genre_id;
