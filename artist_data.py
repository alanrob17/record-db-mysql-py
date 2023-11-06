def GetArtistIds(records):
    # Create a set to store distinct artist_ids
    artist_ids = set()

    for record in records:
        (artist_id, name, recorded, media) = record
        artist_ids.add(artist_id)

    # Convert the set to a list if needed
    artist_ids_list = list(artist_ids)

    return artist_ids_list


def OrganizeRecordsByArtist(records):
    artist_records = {}

    for record in records:
        (artist_id, name, recorded, media) = record

        if artist_id not in artist_records:
            artist_records[artist_id] = []

        artist_records[artist_id].append((recorded, name, media))

    return artist_records
