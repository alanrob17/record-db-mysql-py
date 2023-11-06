import mysql.connector
import configuration as c

db_user, db_password, db_database = c.connect()


def GetRecordsById(artistId):
    records = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetRecordsById", (artistId))

        for result in cursor.stored_results():
            records = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return records


def GetArtistsAndRecords():
    records = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                "GetArtistRecordsByRecordId",
            )

        for result in cursor.stored_results():
            records = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return records


def GetFullRecords():
    records = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                "GetFullRecords",
            )

        for result in cursor.stored_results():
            records = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return records


def GetRecords():
    records = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                "GetRecords",
            )

        for result in cursor.stored_results():
            records = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return records


def GetRecordsByYear(year):
    records = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetRecordsByYear", (year,))

        for result in cursor.stored_results():
            records = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return records


def GetArtistIdsByYear(year):
    artistIds = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetArtistIdsByYear", (year,))

            for result in cursor.stored_results():
                artistIds = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return artistIds


def CreateRecord(record):
    record_id = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            (
                artistId,
                name,
                field,
                recorded,
                label,
                pressing,
                rating,
                discs,
                media,
                bought,
                cost,
                review,
            ) = record
            cursor.callproc(
                "CreateRecord",
                (
                    artistId,
                    name,
                    field,
                    recorded,
                    label,
                    pressing,
                    rating,
                    discs,
                    media,
                    bought,
                    cost,
                    review,
                ),
            )

            for result in cursor.stored_results():
                row = result.fetchone()
                if row:
                    artist_id = row[0]

            db.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return artist_id


def GetRecordById(recordId):
    record = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetRecordById", (recordId,))

            for result in cursor.stored_results():
                row = result.fetchone()
                if row:
                    record = row

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return record


def UpdateRecord(recordId, updatedRecord):
    (
        artistId,
        name,
        field,
        recorded,
        label,
        pressing,
        rating,
        discs,
        media,
        bought,
        cost,
        review,
    ) = updatedRecord

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                "UpdateRecordById",
                (
                    recordId,
                    artistId,
                    name,
                    field,
                    recorded,
                    label,
                    pressing,
                    rating,
                    discs,
                    media,
                    bought,
                    cost,
                    review,
                ),
            )

            result = f"{cursor.rowcount} record(s) affected"

            db.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return result


def DeleteRecord(recordId):
    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetRecordById", (recordId,))

            for result in cursor.stored_results():
                row = result.fetchone()
                if row:
                    record = row

            if record is None:
                return "Record not found"

            cursor.callproc("DeleteRecordById", (recordId,))
            db.commit()

            affected_rows = cursor.rowcount
            if affected_rows > 0:
                return f"{affected_rows} record(s) deleted"
            else:
                return "No records deleted"

    except mysql.connector.Error as err:
        return f"Error: {err}"


def GetRecordByName(searchName):
    records = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetRecordByName", (searchName,))

            for result in cursor.stored_results():
                records = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return records


def GetRecordsByArtistId(artistId):
    records = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetRecordsByArtistId", (artistId,))

            for result in cursor.stored_results():
                records = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return records


def GetTotalNumberOfCDs(sproc):
    Total = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                sproc,
            )

            for result in cursor.stored_results():
                result = result.fetchone()
                if result:
                    total = result[0]

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return total


def GetTotalNumberOfDiscs(sproc):
    Total = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                sproc,
            )

            for result in cursor.stored_results():
                result = result.fetchone()
                if result:
                    total = result[0]

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return total


def GetArtistNumberOfRecords(artistId):
    Total = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetArtistNumberOfRecords", (artistId,))

            for result in cursor.stored_results():
                result = result.fetchone()
                if result:
                    total = result[0]

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return total


def GetArtistRecordEntity(recordId: int) -> tuple:
    record = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetArtistRecordByRecordId", (recordId,))

            for result in cursor.stored_results():
                record = result.fetchone()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return record


def GetSingleRecord(recordId: int) -> tuple:
    record = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetSingleRecord", (recordId,))

            for result in cursor.stored_results():
                record = result.fetchone()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return record


def GetArtistNameByRecordId(recordId: int) -> str:
    name = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetArtistNameByRecordId", (recordId,))

            for result in cursor.stored_results():
                row = result.fetchone()
                if row:
                    name = row[0]

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return name


def GetDiscCountForYear(year: int) -> int:
    Total = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetRecordedYearNumber", (year,))

            for result in cursor.stored_results():
                result = result.fetchone()
                if result:
                    total = result[0]

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return total


def GetBoughtDiscCountForYear(year: str) -> int:
    Total = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc("GetBoughtDiscCountForYear", (year,))

            for result in cursor.stored_results():
                result = result.fetchone()
                if result:
                    total = result[0]

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return total


def MissingRecordReviews():
    records = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                "MissingRecordReview",
            )

            for result in cursor.stored_results():
                records = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return records


def GetTotalsForEachArtist():
    records = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                "GetTotalsForEachArtist",
            )

            for result in cursor.stored_results():
                records = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return records


def GetTotalCostForEachArtist():
    records = None

    try:
        with mysql.connector.connect(
            host="localhost", user=db_user, password=db_password, database=db_database
        ) as db, db.cursor() as cursor:
            cursor.callproc(
                "GetTotalCostForEachArtist",
            )

            for result in cursor.stored_results():
                records = result.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return records
