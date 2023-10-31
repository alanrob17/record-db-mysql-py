import mysql.connector
import configuration as c


db_user, db_password, db_database = c.connect()


def get_all_artists():
    db = mysql.connector.connect(
        host="localhost", user=db_user, password=db_password, database=db_database
    )

    cursor = db.cursor()

    sql = "SELECT ArtistId, FirstName, LastName, Name, Biography FROM Artist ORDER BY LastName, FirstName;"

    cursor.execute(sql)

    artists = cursor.fetchall()

    cursor.close()
    db.close()

    return artists


def get_artist(artist_name):
    db = mysql.connector.connect(
        host="localhost", user=db_user, password=db_password, database=db_database
    )

    cursor = db.cursor()

    sql = f"SELECT ArtistId, Name, FirstName, LastName, Biography FROM Artist WHERE Name = '{artist_name}';"

    cursor.execute(sql)

    artist = cursor.fetchone()

    cursor.close()
    db.close()

    return artist


def get_artist_by_id(artist_id):
    db = mysql.connector.connect(
        host="localhost", user=db_user, password=db_password, database=db_database
    )

    cursor = db.cursor()

    sql = f"SELECT ArtistId, Name, FirstName, LastName, Biography FROM Artist WHERE ArtistId = '{artist_id}';"

    cursor.execute(sql)

    artist = cursor.fetchone()

    cursor.close()
    db.close()

    return artist
