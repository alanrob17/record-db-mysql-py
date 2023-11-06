import artist_db as a
import artist_data as ad


def PrintArtists():
    artists = a.GetAllArtists()

    for artist in artists:
        (
            artistId,
            firstName,
            lastName,
            artistName,
            biography,
        ) = artist
        print(f"Id: {artistId}: {artistName}")


def PrintArtistById(artistId):
    artist = a.GetArtistById(artistId)

    if artist:
        (artistId, firstName, lastName, artistName, biography) = artist

        print(f"ArtistId: {artistId}")
        print(f"Artist name: {artistName}")
        print(f"First name: {firstName}")
        print(f"Last name: {lastName}")

        biographyToPrint = biography if len(biography) < 60 else biography[:60] + "..."

        print(f"Biography: {biographyToPrint}")
    else:
        print(f"Artist with id: '{artistId}' not found.")


def PrintBiography(artistId):
    artist = a.GetArtistById(artistId)

    if artist:
        (artistId, firstName, lastName, artistName, biography) = artist

        print(f"Biography: {biography}")
    else:
        print(f"Artist with id: '{artistId}' not found.")


def PrintArtist(name):
    artist = None
    artist = a.GetArtist(name)

    if artist:
        (
            artistId,
            firstName,
            lastName,
            artistName,
            biography,
        ) = artist

        print(f"ArtistId: {artistId}")
        print(f"Artist name: {artistName}")
        print(f"First name: {firstName}")
        print(f"Last name: {lastName}")

        biographyToPrint = biography if len(biography) < 60 else biography[:60] + "..."

        print(f"Biography: {biographyToPrint}")
    else:
        print(f"Artist '{name}' not found in the 'Artist' table.")


def CreateArtist():
    firstName = "Ethan"
    lastName = "Robson"
    biography = "Ethan is a Soul singer."
    artist = (firstName, lastName, biography)

    artistId = a.CreateArtist(artist)

    print(artistId)


def UpdateArtist(artistId):
    artist = (
        "Ethan James",
        "Robson",
        "Ethan is a Hip-Hop and Country & Western singer.",
    )

    result = a.UpdateArtist(artistId, artist)

    return result


def DeleteArtist(artistId):
    result = a.DeleteArtist(artistId)

    print(result)


def ArtistHtml(artistId):
    artist = a.GetArtistById(artistId)

    if artist is None:
        return "Artist not found"
    else:
        (artistId, firstName, lastName, name, biography) = artist
        htmlCode = f"<p><strong>Id:</strong> {artistId}</p>\n<p><strong>Name:</strong> {firstName} {lastName}</p>\n<p><strong>Biography:</strong></p>\n<div>{biography}</p></div>"

    return htmlCode


def GetArtistId(firstName, lastName):
    artistId = a.GetArtistIdByName(firstName, lastName)

    if artistId is not None:
        print(f"Artist ID for {firstName} {lastName}: {artistId}")
    else:
        print(f"No artistId found for {firstName} {lastName}")


def GetArtistsWithNoBio():
    artists = a.GetArtistsWithNoBio()
    for artist in artists:
        (artistId, name) = artist
        print(f"ArtistId: {artistId} - {name}")


def GetNoBiographyCount():
    count = a.GetNoBiographyCount()
    print(f"There are {count} artists with no biography.")
