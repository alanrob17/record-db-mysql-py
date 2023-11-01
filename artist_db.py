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


def create_artist(artist):
    firstname, lastname, name, biography = artist

    db = mysql.connector.connect(
        host="localhost", user=db_user, password=db_password, database=db_database
    )

    cursor = db.cursor()

    if not firstname:
        name = f"{lastname}"
    else:
        name = f"{firstname} {lastname}"

    sql = "INSERT INTO Artist (FirstName, LastName, Name, Biography) VALUES (%s, %s, %s, %s);"
    values = (firstname, lastname, name, biography)

    cursor.execute(sql, values)

    id = cursor.lastrowid

    db.commit()

    cursor.close()
    db.close()

    return id


def update_artist(artist_id, new_artist):
    db = mysql.connector.connect(
        host="localhost", user=db_user, password=db_password, database=db_database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM Artist WHERE ArtistId = %s", (artist_id,))
    existing_artist = cursor.fetchone()

    if existing_artist is None:
        cursor.close()
        db.close()
        return "Artist not found"

    sql = """
    UPDATE Artist
    SET FirstName = %s, LastName = %s, Name = %s, Biography = %s
    WHERE ArtistId = %s
    """

    new_name = f"{new_artist['FirstName']} {new_artist['LastName']}"
    update_data = (
        new_artist["FirstName"],
        new_artist["LastName"],
        new_name,
        new_artist["Biography"],
        artist_id,
    )

    cursor.execute(sql, update_data)
    db.commit()

    cursor.close()
    db.close()

    return "Artist updated successfully"


def delete_artist(artist_id):
    db = mysql.connector.connect(
        host="localhost", user=db_user, password=db_password, database=db_database
    )

    cursor = db.cursor()

    cursor.execute("SELECT ArtistId FROM Artist WHERE ArtistId = %s", (artist_id,))
    existing_artist = cursor.fetchone()

    if existing_artist is None:
        cursor.close()
        db.close()
        return "Artist not found"

    sql = "DELETE FROM Artist WHERE ArtistId = %s"
    cursor.execute(sql, (artist_id,))
    db.commit()

    cursor.close()
    db.close()

    return f"Artist with ArtistId {artist_id} has been deleted"
