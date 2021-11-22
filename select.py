import psycopg2
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://alexander:123456@localhost:5432/music_website_db')
connection = engine.connect()

# название и год выхода альбомов, вышедших в 2018 году
connection.execute("""
SELECT name, year_release FROM albums_list
WHERE year_release = 2018;
"""
).fetchall()

# название и продолжительность самого длительного трека
connection.execute("""
SELECT name, duration FROM track_list
ORDER BY duration DESC;
""").fetchmany(1)

# название треков, продолжительность которых не менее 3,5 минуты
connection.execute("""
SELECT name FROM track_list
WHERE duration > 210;
""").fetchall()

# названия сборников, вышедших в период с 2018 по 2020 год включительно
connection.execute("""
SELECT name, year FROM collections
WHERE year BETWEEN 2018 AND 2020;
""").fetchall()

# исполнители, чье имя состоит из 1 слова
connection.execute("""
SELECT name FROM musicians
WHERE name NOT LIKE '%% %%';
""").fetchall()

# название треков, которые содержат слово "мой"/"my"
connection.execute("""
SELECT name FROM track_list
WHERE name ILIKE '%%my%%';
""").fetchall()
