import artist_db as a
import artist_test as at
import artist_data as ad
import record_db as r
import record_data as rd
import utilities as u


def PrintRecordsByYear(year):
    records = r.GetRecordsByYear(year)

    if len(records) == 0:
        print(f"No records found for {year}.")
        exit()

    artists = a.GetAllArtists()

    artistIdsList = ad.GetArtistIds(records)

    artists = [artist for artist in artists if artist[0] in artistIdsList]

    def print_records(artists, records):
        print(f"\nAlbums recorded in {year}:")

        for artist in artists:
            (artistId, firstName, lastName, name, biography) = artist

            print(f"\n{name}\n")

            filteredRecords = rd.FilterRecordsByArtist(records, artistId)

            for record in filteredRecords:
                artistId, name, recorded, media = record

                print(f"\t{name} ({media})")

        print()

    print_records(artists, records)


def PrintSortedArtistRecords():
    artists = a.GetAllArtists()

    records = r.GetRecords()

    artistRecords = ad.OrganizeRecordsByArtist(records)

    for artist in artists:
        (artistId, firstName, lastName, artistName, biography) = artist

        if artistId in artistRecords:
            print(f"\n{artistName}\n")

            for recorded, name, media in artistRecords[artistId]:
                print(f"\t{recorded} - {name} ({media})")

    print()


def PrintRecords():
    records = r.GetRecords()

    for record in records:
        artist_id, name, recorded, media = record

        print(f"{artist_id}: {recorded} - {name} ({media})")


def PrintFullRecords():
    records = r.GetFullRecords()

    for record in records:
        (
            record_id,
            artist_id,
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

        dateStamp = u.dateString(bought)
        dateStamp = f" - Bought: {dateStamp}" if dateStamp else ""

        print(
            f"{record_id}: {artist_id}: - {name} - {field} - {recorded} - {label} - {pressing} - {rating} - {discs} - {media} - {dateStamp} - ${u.roundOff(cost)}."
        )


def PrintArtistsAndRecords():
    artists_records = r.GetArtistsAndRecords()

    for record in artists_records:
        (artistId, artist, recordName, recorded, media) = record

        print(f"{artistId}: {artist} - {recorded} - {recordName} ({media})")


def CreateRecord(artistId):
    disc = (
        artistId,
        "Bongo Zongo",
        "Rock",
        1979,
        "Bop Squat",
        "USA",
        "***",
        1,
        "CD",
        "2023-09-27 12:00:00",
        21.99,
        "Pretty good,  even if I do say so myself!",
    )

    artistId = r.CreateRecord(disc)

    if artistId:
        print(f"Record with the Id: {artistId} created.")
    else:
        print("No record created!")


def GetRecordById(recordId):
    record = r.GetRecordById(recordId)

    if record:
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
        ) = record

    dateStamp = u.dateString(bought)
    dateStamp = f" - Bought: {dateStamp}" if dateStamp else ""

    if record:
        print(
            f"{recordId}, {artistId}, {name}, {recorded}, {media}, {dateStamp}, ${u.roundOff(cost)}"
        )
    else:
        print("Record not found!")


def UpdateRecord(recordId):
    newRecord = (
        827,
        "Bango Wango",
        "Jazz",
        1990,
        "Diddly Squat",
        "AU",
        "****",
        2,
        "CD",
        "2023-10-27 12:00:00",
        24.50,
        "Pretty amazing, even if I do say so myself!",
    )

    result = r.UpdateRecord(recordId, newRecord)

    if result:
        print(result)
    else:
        print("Record not updated!")


def DeleteRecord(recordId):
    result = r.DeleteRecord(recordId)

    print(result)


def GetRecordByName(searchName):
    records = r.GetRecordByName(searchName)
    for record in records:
        (name, recorded, media, bought, cost) = record

        dateStamp = u.dateString(bought)
        dateStamp = f" - Bought: {dateStamp}" if dateStamp else ""

        print(f"{recorded} - {name} ({media}){dateStamp} - Cost ${u.roundOff(cost)}")


def GetRecordsByArtistId(artistId):
    records = r.GetRecordsByArtistId(artistId)

    if records:
        for record in records:
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
            ) = record

            dateStamp = u.dateString(bought)
            dateStamp = f" - Bought: {dateStamp}" if dateStamp else ""

            print(
                f"{recordId}, {artistId}, {name}, {recorded}, {media}, {dateStamp}, ${u.roundOff(cost)}"
            )
    else:
        print(f"Records not found for ArtistId: {artistId}!")


def GetTotalNumberOfDiscs(sproc):
    total = None

    total = r.GetTotalNumberOfDiscs(sproc)

    return total


def GetArtistRecordEntity(recordId):
    record = r.GetArtistRecordEntity(recordId)

    if record:
        (
            artistId,
            firstName,
            lastName,
            artistName,
            recordId,
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
        ) = record

        dateStamp = u.dateString(bought)
        dateStamp = f" - Bought: {dateStamp}" if dateStamp else ""

        print(
            f"{recordId}, {artistId}, {artistName} - {name}, {recorded}, {media}, {dateStamp}, ${u.roundOff(cost)}"
        )
    else:
        print(f"Records not found for ArtistId: {artistId}!")


def GetArtistNumberOfRecords(artistId):
    total = None
    artist = a.GetArtistById(artistId)

    if artist:
        (artistId, firstName, lastName, name, biography) = artist

        total = r.GetArtistNumberOfRecords(artistId)

        if total:
            print(f"{name} has {total} records.")
        else:
            print(f"{name} has no records.")
    else:
        print(f"{artistId} not found!")


def GetRecordDetails(recordId):
    record = r.GetSingleRecord(recordId)

    if record:
        (
            recordId,
            name,
            recorded,
            media,
        ) = record

        print(
            f"Record Id: {recordId}, Name: {name}, Recorded: {recorded}, Media: {media}"
        )
    else:
        print(f"Record not found for RecordId: {recordId}!")


def GetArtistNameFromRecord(recordId: int):
    name = None

    name = r.GetArtistNameByRecordId(recordId)

    if name:
        print(f"Artist name: {name}.")
    else:
        print(f"Artist name not found for RecordId: {recordId}!")


def GetDiscCountForYear(year: int):
    total = None
    total = r.GetDiscCountForYear(year)

    if total:
        print(f"Total number of discs for {year} is {total}.")
    else:
        print(f"{year} has no discs.")


def GetBoughtDiscCountForYear(year: str):
    total = None
    total = r.GetBoughtDiscCountForYear(year)

    if total:
        print(f"Total number of discs bought in {year} is {total}.")
    else:
        print(f"No discs were bought in {year}.")


def MissingRecordReviews():
    records = r.MissingRecordReviews()

    if records:
        for record in records:
            (artistId, artist, recordId, name, recorded, discs, rating, media) = record

            print(
                f"{artist} - Id: {recordId} - {recorded} - {name} ({media}) - {discs} - {rating}"
            )
    else:
        print(f"No Records found!")


def GetTotalArtistTotals():
    records = r.GetTotalsForEachArtist()

    if records:
        for record in records:
            (artistId, name, totalDisc, totalCost) = record

            print(
                f"{artistId}: {name.strip()} - {totalDisc} - ${u.roundOff(totalCost)}"
            )
    else:
        print(f"No Records found!")


def GetTotalCostForEachArtist():
    records = r.GetTotalCostForEachArtist()

    if records:
        for record in records:
            (artistId, name, totalCost) = record

            print(f"{artistId}: {name.strip()} - ${u.roundOff(totalCost)}")
    else:
        print(f"No Records found!")


def RecordHtml(recordId):
    record = r.GetArtistRecordEntity(recordId)

    if record:
        (
            artistId,
            firstName,
            lastName,
            artistName,
            recordId,
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
        ) = record

        dateStamp = u.dateString(bought)
        dateStamp = f"Bought: {dateStamp}" if dateStamp else ""

        print(
            f"<p><strong>ArtistId:</strong> {artistId}</p>\n<p><strong>Artist:</strong> \
{artistName}</p>\n<p><strong>RecordId:</strong> {recordId}</p>\n<p><strong>Recorded:</strong> \
{recorded}</p>\n<p><strong>Name:</strong> {name}</p>\n<p><strong>Rating:</strong> \
{rating}</p>\n<p><strong>Media:</strong> {media}</p>\n \
<p><strong>Bought:</strong> {dateStamp}</p>\n<p><strong>Cost:</strong> ${u.roundOff(cost)}</p>\n"
        )
    else:
        print(f"Records not found for ArtistId: {artistId}!")
