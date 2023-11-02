import artist_db as a
import artist_data as ad
import record_db as r
import record_data as rd

##---- Artist ----


def print_artists():
    artists = a.get_all_artists()

    for artist in artists:
        (
            artist_id,
            first_name,
            last_name,
            artist_name,
            biography,
        ) = artist  # Unpack the row
        print(f"Id: {artist_id}: {artist_name}")


def print_artist_by_id(artist_id):
    artist = a.get_artist_by_id(artist_id)

    if artist:
        (artist_id, first_name, last_name, artist_name, biography) = artist

        print(f"ArtistId: {artist_id}")
        print(f"Artist name: {artist_name}")
        print(f"First name: {first_name}")
        print(f"Last name: {last_name}")

        biography_to_print = (
            biography if len(biography) < 60 else biography[:60] + "..."
        )

        print(f"Biography: {biography_to_print}")
    else:
        print(f"Artist with id: '{artist_id}' not found.")


def print_Biography(artist_id):
    artist = a.get_artist_by_id(artist_id)

    if artist:
        (artist_id, first_name, last_name, artist_name, biography) = artist

        print(f"Biography: {biography}")
    else:
        print(f"Artist with id: '{artist_id}' not found.")


def print_artist(name):
    artist = a.get_artist(name)

    if artist:
        (
            artist_id,
            first_name,
            last_name,
            artist_name,
            biography,
        ) = artist  # Unpack the row

        print(f"ArtistId: {artist_id}")
        print(f"Artist name: {artist_name}")
        print(f"First name: {first_name}")
        print(f"Last name: {last_name}")

        biography_to_print = (
            biography if len(biography) < 60 else biography[:60] + "..."
        )

        print(f"Biography: {biography_to_print}")
    else:
        print(f"Artist '{artist_name}' not found in the 'Artist' table.")


def create_artist():
    firstname = "Charley"
    lastname = "Robson"
    name = ""
    biography = "Charley is a Country & Western singer."
    artist = (firstname, lastname, name, biography)

    artist_id = a.create_artist(artist)

    print(artist_id)


def update_artist(artist_id):
    artist = {
        "FirstName": "Charley",
        "LastName": "Robson",
        "Name": "",
        "Biography": "Charley is a Hip-Hop and Country & Western singer.",
    }

    result = a.update_artist(artist_id, artist)

    return result


def delete_artist(artist_id):
    result = a.delete_artist(artist_id)

    print(result)


def get_biography(artist_id):
    biography = a.get_biography(artist_id)

    print(biography)


def artist_html(artist_id):
    artist = a.get_artist_by_id(artist_id)

    if artist is None:
        return "Artist not found"
    else:
        (artist_id, first_name, last_name, name, biography) = artist
        html_code = f"<p><strong>Id:</strong> {artist_id}</p>\n<p><strong>Name:</strong> {first_name} {last_name}</p>\n<p><strong>Biography:</strong></p>\n<div>{biography}</p></div>"

    return html_code


def get_artist_id(first_name, last_name):
    artist_id = a.get_artist_id_by_name2(first_name, last_name)

    if artist_id is not None:
        print(f"Artist ID for {first_name} {last_name}: {artist_id}")
    else:
        print(f"No artist found for {first_name} {last_name}")


def get_artists_with_no_bio():
    artists = a.get_artists_with_no_bio()
    for artist in artists:
        (artist_id, name) = artist
        print(f"ArtistId: {artist_id} - {name}")


def get_no_biography_count():
    count = a.get_no_biography_count()
    print(f"There are {count} artists with no biography.")


##---- Record ----


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
        artist_id, artist, record_name, recorded, media = record

        print(f"{artist_id}: {artist} - {recorded} - {record_name} ({media})")


# ---- Artist calls ----

# name = "Bob Dylan"
# print_artist(name)

# print_artists()

# artist_id = 114
# print_artist_by_id(artist_id)

# artist_id = 114
# print_Biography(artist_id)

# create_artist()

# artist_id = 833
# result = update_artist(artist_id)
# print(result)


# artist_id = 833
# delete_artist(artist_id)

# artist_id = 114
# get_biography(artist_id)

# artist_id = 114
# html = artist_html(artist_id)
# print(html)

first_name = "Bob"
last_name = "Dylan"
get_artist_id(first_name, last_name)

# get_artists_with_no_bio()

# get_no_biography_count()

# ---- Record calls ----

# print_artists_and_records()

# print_full_records()

# print_records()

# print_sorted_artist_records()

# year = 1975
# print_records_by_year(year)


# GetAllRecords();
# CreateRecord(838);
# GetRecordById(133);
# UpdateRecord(5259);
# DeleteRecord(5260);
# GetRecordByName("Cutting Edge");
# GetRecordsByArtistId(114);
# GetArtistRecordsMultipleTables();
# GetRecordsByArtistIdMultipleTables(114);
# GetRecordsByArtistIdMultipleTablesSP(114);
# GetRecordsByYear(1974);
# GetTotalNumberOfCDs();
# GetTotalNumberOfDiscs();
# GetTotalNumberOfRecords();
# GetTotalNumberOfBlurays();
# GetRecordList();
# GetRecordListMultipleTables();
# CountDiscs(string.Empty);
# CountDiscs("DVD");
# CountDiscs("CD");
# CountDiscs("R");
# GetArtistRecordEntity(2196);
# GetArtistNumberOfRecords(114);
# GetRecordDetails(2196);
# GetArtistNameFromRecord(2196);
# GetDiscCountForYear(1974);
# GetBoughtDiscCountForYear("2000");
# GetNoRecordReview();
# GetNoReviewCount();
# GetTotalArtistCost();
# GetTotalArtistDiscs();
# RecordHtml(2196);
