import artist_db as a
import artist_test as at
import artist_data as ad
import record_db as r
import record_data as rd


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

        print(
            f"{record_id}: {artist_id}: - {name} - {field} - {recorded} - {label} - {pressing} - {rating} - {discs} - {media} - {bought} - {cost}."
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

    if record:
        print(f"{recordId}, {artistId}, {name}, {recorded}, {media}, {bought}, {cost}")
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

        cost = round(cost, 2)

        year = bought.strftime("%Y")
        month = bought.strftime("%m")
        day = bought.strftime("%d")

        if year == "1900":
            dateStamp = ""
        else:
            dateStamp = f" - Bought: {day}-{month}-{year}"

        print(f"{recorded} - {name} ({media}){dateStamp} - Cost ${cost}")
