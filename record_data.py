def filter_records_by_artist(records, artist_id):
    filtered_records = [record for record in records if record[0] == artist_id]
    sorted_records = sorted(filtered_records, key=lambda record: record[1])

    return sorted_records
