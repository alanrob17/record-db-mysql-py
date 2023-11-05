import artist_db as a
import artist_test as at
import artist_data as ad
import record_db as r
import record_data as rd
import utilities as u


def print_records_by_year(year):
    records = r.get_records_by_year(year)

    if len(records) == 0:
        print(f"No records found for {year}.")
        exit()

    artists = a.get_all_artists()

    artist_ids_list = ad.get_artist_ids(records)

    artists = [artist for artist in artists if artist[0] in artist_ids_list]

    def print_records(artists, records):
        print(f"\nAlbums recorded in {year}:")

        for artist in artists:
            artist_id, first_name, last_name, name, biography = artist

            print(f"\n{name}\n")

            filtered_records = rd.filter_records_by_artist(records, artist_id)

            for record in filtered_records:
                artist_id, name, recorded, media = record

                print(f"\t{name} ({media})")

        print()

    print_records(artists, records)


def print_sorted_artist_records():
    artists = a.get_all_artists()

    records = r.get_records()

    artist_records = ad.organize_records_by_artist(records)

    for artist in artists:
        artist_id, first_name, last_name, artist_name, biography = artist

        if artist_id in artist_records:
            print(f"\n{artist_name}\n")

            for recorded, name, media in artist_records[artist_id]:
                print(f"\t{recorded} - {name} ({media})")

    print()


def print_records():
    records = r.get_records()

    for record in records:
        artist_id, name, recorded, media = record

        print(f"{artist_id}: {recorded} - {name} ({media})")


def print_full_records():
    records = r.get_full_records()

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


def print_artists_and_records():
    artists_records = r.get_artists_and_records()

    for record in artists_records:
        (artist_id, artist, record_name, recorded, media) = record

        print(f"{artist_id}: {artist} - {recorded} - {record_name} ({media})")


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
    artist = a.get_artist_by_id(artistId)

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
