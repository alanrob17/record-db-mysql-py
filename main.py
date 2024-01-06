import artist_test as at
import record_test as rt

## ---- Artist calls ----

name = "Bob Dylan"
at.PrintArtist(name)

# at.PrintArtists()

# artistId = 114
# at.PrintArtistById(artistId)

# artistId = 114
# at.PrintBiography(artistId)

# at.CreateArtist()

# artistId = 836
# result = at.UpdateArtist(artistId)
# print(result)


# artistId = 836
# at.DeleteArtist(artistId)

# artistId = 114
# html = at.ArtistHtml(artistId)
# print(html)

# firstName = "Bob"
# lastName = "Dylan"
# at.GetArtistId(firstName, lastName)

# at.GetArtistsWithNoBio()

# at.GetNoBiographyCount()

## ---- Record calls ----

# rt.PrintArtistsAndRecords()

# rt.PrintFullRecords()

# rt.PrintRecords()

# rt.PrintSortedArtistRecords()

# year = 1975
# rt.PrintRecordsByYear(year)

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

# recordId = 2196
# rt.RecordHtml(recordId)
