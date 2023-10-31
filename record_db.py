import mysql.connector
import configuration as c

db_user, db_password, db_database = c.connect()


def get_records_by_id(artist_id):
    db = mysql.connector.connect(
        host="localhost", user=db_user, password=db_password, database=db_database
    )

    cursor = db.cursor()

    sql = f"SELECT Name, Recorded, Media FROM Record WHERE ArtistId = {artist_id} ORDER BY Recorded DESC;"

    cursor.execute(sql)

    records = cursor.fetchall()

    cursor.close()
    db.close()

    return records


def get_artists_and_records():
    db = mysql.connector.connect(
        host="localhost", user=db_user, password=db_password, database=db_database
    )

    cursor = db.cursor()

    sql = "SELECT a.ArtistId, a.Name AS Artist, r.Name AS Record, r.Recorded, r.Media \
        FROM Artist a INNER JOIN Record r \
        ON a.ArtistId = r.ArtistId \
        ORDER BY a.LastName, a.FirstName, r.Recorded DESC;"

    cursor.execute(sql)

    artist_record = cursor.fetchall()

    cursor.close()
    db.close()

    return artist_record


def get_full_records():
    db = mysql.connector.connect(
        host="localhost", user=db_user, password=db_password, database=db_database
    )

    cursor = db.cursor()

    sql = "SELECT RecordId, ArtistId, Name, Field, Recorded, Label, Pressing, \
            Rating, Discs, Media, Bought, Cost, Review \
            FROM Record ORDER BY ArtistId, Recorded DESC;"

    cursor.execute(sql)

    records = cursor.fetchall()

    cursor.close()
    db.close()

    return records


def get_records():
    db = mysql.connector.connect(
        host="localhost", user=db_user, password=db_password, database=db_database
    )

    cursor = db.cursor()

    sql = "SELECT ArtistId, Name, Recorded, Media FROM Record ORDER BY ArtistId, Recorded DESC;"

    cursor.execute(sql)

    records = cursor.fetchall()

    cursor.close()
    db.close()

    return records


def get_records_by_year(year):
    db = mysql.connector.connect(
        host="localhost", user=db_user, password=db_password, database=db_database
    )

    cursor = db.cursor()

    sql = f"SELECT ArtistId, Name, Recorded, Media FROM Record WHERE Recorded = {year} ORDER BY ArtistId, Recorded DESC;"

    cursor.execute(sql)

    records = cursor.fetchall()

    cursor.close()
    db.close()

    return records


def get_artist_ids_by_year(year):
    db = mysql.connector.connect(
        host="localhost", user=db_user, password=db_password, database=db_database
    )

    cursor = db.cursor()

    sql = f"SELECT DISTINCT ArtistId FROM Record WHERE Recorded = {year} ORDER BY ArtistId;"

    cursor.execute(sql)

    artist_ids = cursor.fetchall()

    cursor.close()
    db.close()

    return artist_ids
