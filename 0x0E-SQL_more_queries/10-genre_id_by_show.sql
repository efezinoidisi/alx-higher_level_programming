-- lists all shows contained im hbtn_0d_tvshow that have at least one genre linked

SELECT shows.title, genres.genre_id FROM tv_shows AS shows
JOIN tv_shows_genres AS genres ON shows.id = genres.show_id
ORDER BY shows.title ASC, genres.genre_id ASC;
