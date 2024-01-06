import mysql.connector
import configuration as c


db_user, db_password, db_database, db_host, db_port = c.connect()


def GetAllArtists():
    artists = None

    try:
        with mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_database,
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                "GetAllArtists",
            )

        for result in cursor.stored_results():
            artists = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return artists


def GetArtist(artistName):
    artist = None

    try:
        with mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_database,
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetArtistByName", (artistName,))

            for result in cursor.stored_results():
                row = result.fetchone()
                if row:
                    artist = row

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return artist


def GetArtistById(artistId):
    artist = None

    try:
        with mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_database,
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetArtistById", (artistId,))

            for result in cursor.stored_results():
                row = result.fetchone()
                if row:
                    artist = row

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return artist


def CreateArtist(artist):
    artistId = None

    try:
        with mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_database,
        ) as db, db.cursor() as cursor:
            (firstName, lastName, biography) = artist

            cursor.callproc("CreateArtist", (firstName, lastName, biography))

            for result in cursor.stored_results():
                row = result.fetchone()
                if row:
                    artistId = row[0]

            db.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return artistId


def UpdateArtist(artistId, updatedArtist):
    (firstName, lastName, biography) = updatedArtist

    try:
        with mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_database,
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                "UpdateArtistById",
                (artistId, firstName, lastName, biography),
            )

            result = f"{cursor.rowcount} record(s) affected"

            db.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return result


def DeleteArtist(artistId):
    try:
        with mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_database,
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetArtistById", (artistId,))

            for result in cursor.stored_results():
                row = result.fetchone()
                if row:
                    artist = row

            if artist is None:
                return "Artist not found"

            cursor.callproc("DeleteArtistById", (artistId,))
            db.commit()

            affectedRows = cursor.rowcount
            if affectedRows > 0:
                return f"{affectedRows} artist(s) deleted"
            else:
                return "No artists deleted"

    except mysql.connector.Error as err:
        return f"Error: {err}"


def GetArtistIdByName(firstName, lastName):
    artistId = None

    try:
        with mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_database,
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetArtistIdByNames", (firstName, lastName))

            for result in cursor.stored_results():
                row = result.fetchone()
                if row:
                    artistId = row[0]

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return artistId


def GetArtistsWithNoBio():
    artists = None

    try:
        with mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_database,
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                "GetArtistsWithNoBio",
            )

        for result in cursor.stored_results():
            artists = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return artists


def GetNoBiographyCount():
    count = None

    try:
        with mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_database,
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                "GetNoBiographyCount",
            )

            for result in cursor.stored_results():
                row = result.fetchone()
                if row:
                    count = row[0]

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return count
