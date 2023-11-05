import artist_test as at
import record_test as rt

## ---- Artist calls ----

# name = "Bob Dylan"
# at.print_artist(name)

# at.print_artists()

# artist_id = 114
# at.print_artist_by_id(artist_id)

# artist_id = 114
# at.print_Biography(artist_id)

# at.create_artist()

# artist_id = 833
# result = at.update_artist(artist_id)
# print(result)


# artist_id = 833
# at.delete_artist(artist_id)

# artist_id = 114
# at.get_biography(artist_id)

# artist_id = 114
# html = at.artist_html(artist_id)
# print(html)

# firstName = "Bob"
# lastName = "Dylan"
# at.GetArtistId(firstName, lastName)

# at.get_artists_with_no_bio()

# at.get_no_biography_count()

## ---- Record calls ----

# rt.print_artists_and_records()

# rt.print_full_records()

# rt.print_records()

# rt.print_sorted_artist_records()

# year = 1975
# rt.print_records_by_year(year)

# artistId = 827
# rt.CreateRecord(artistId)

# recordId = 83
# rt.GetRecordById(recordId)

# recordId = 5256
# rt.UpdateRecord(recordId)

# recordId = 5251
# rt.DeleteRecord(recordId)

# searchName = "Blonde On Blonde"
# rt.GetRecordByName(searchName)

# artistId = 114
# rt.GetRecordsByArtistId(artistId)

# sproc = "GetTotalCDCount"
# total = rt.GetTotalNumberOfDiscs(sproc)
# print(f"Total number of Records, CD's: {total}.")

# sproc = "GetTotalNumberOfAllRecords"
# total = rt.GetTotalNumberOfDiscs(sproc)
# print(f"Total number of Records, CD's, DVD's and Blu-rays: {total}.")

# sproc = "GetTotalNumberOfRecords"
# total = rt.GetTotalNumberOfDiscs(sproc)
# print(f"Total number of Vinyl Records: {total}.")

# sproc = "GetTotalNumberOfAllBlurays"
# total = rt.GetTotalNumberOfDiscs(sproc)
# print(f"Total number of Blu-rays: {total}.")

# recordId = 2196
# rt.GetArtistRecordEntity(recordId)

# artistId = 114
# rt.GetArtistNumberOfRecords(artistId)

# recordId = 2196
# rt.GetRecordDetails(recordId)

# recordId = 2196
# rt.GetArtistNameFromRecord(recordId)

# year = 1973
# rt.GetDiscCountForYear(year)

# year = "2000"
# rt.GetBoughtDiscCountForYear(year)

# sproc = "GetNoRecordReviewCount"
# total = rt.GetTotalNumberOfDiscs(sproc)
# print(f"Number of records with no Reviews : {total}.")

# rt.MissingRecordReviews()

# rt.GetTotalArtistTotals()

# rt.GetTotalCostForEachArtist()

recordId = 2196
rt.RecordHtml(recordId)
