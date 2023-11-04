import artist_db as a
import artist_data as ad


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
    firstname = "James"
    lastname = "Robson"
    biography = "James is a heavy metal bass player."
    artist = (firstname, lastname, biography)

    artist_id = a.create_artist2(artist)

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


def GetArtistId(first_name, last_name):
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
