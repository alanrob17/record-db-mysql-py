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

searchName = "blonde on blonde"
rt.GetRecordByName(searchName)

# rt.GetRecordsByArtistId(114);
# rt.GetArtistRecordsMultipleTables();
# rt.GetRecordsByArtistIdMultipleTables(114);
# rt.GetRecordsByArtistIdMultipleTablesSP(114);
# rt.GetRecordsByYear(1974);
# rt.GetTotalNumberOfCDs();
# rt.GetTotalNumberOfDiscs();
# rt.GetTotalNumberOfRecords();
# rt.GetTotalNumberOfBlurays();
# rt.GetRecordList();
# rt.GetRecordListMultipleTables();
# rt.CountDiscs(string.Empty);
# rt.CountDiscs("DVD");
# rt.CountDiscs("CD");
# rt.CountDiscs("R");
# rt.GetArtistRecordEntity(2196);
# rt.GetArtistNumberOfRecords(114);
# rt.GetRecordDetails(2196);
# rt.GetArtistNameFromRecord(2196);
# rt.GetDiscCountForYear(1974);
# rt.GetBoughtDiscCountForYear("2000");
# rt.GetNoRecordReview();
# rt.GetNoReviewCount();
# rt.GetTotalArtistCost();
# rt.GetTotalArtistDiscs();
# rt.RecordHtml(2196);
