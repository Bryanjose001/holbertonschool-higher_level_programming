-- File: SQL_more_queries/13-count_shows_by_genre.sql
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
    INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY
    genre
ORDER BY number_of_shows DESC;