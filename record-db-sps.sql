DELIMITER $

CREATE PROCEDURE CreateArtist(
    IN _firstName VARCHAR(255),
    IN _lastName VARCHAR(255),
    IN _biography TEXT
)
BEGIN
    DECLARE _artistName VARCHAR(255);

    IF _firstName IS NULL OR _firstName = '' THEN
        SET _artistName = _lastName;
    ELSE
        SET _artistName = CONCAT(_firstName, ' ', _lastName);
    END IF;

    INSERT INTO Artist (FirstName, LastName, Name, Biography)
    VALUES (_firstName, _lastName, _artistName, _biography);

    SELECT LAST_INSERT_ID() AS ArtistId;
END $

DELIMITER ;

DELIMITER $

CREATE PROCEDURE CreateRecord(
_artistId int,
_name varchar(100),
_field varchar(50),
_recorded int,
_label varchar(50),
_pressing varchar(50),
_rating varchar(4),
_discs int,
_media varchar(50),
_bought datetime,
_cost decimal(10,4),
_review longtext
)
BEGIN
    INSERT INTO Record (artistId, name, field, recorded, label, pressing, rating, discs, media, bought, cost, review)
    VALUES (_artistId, _name, _field, _recorded, _label, _pressing, _rating, _discs, _media, _bought, _cost, _review);

    SELECT LAST_INSERT_ID() AS RecordId;
END $

DELIMITER ;

DELIMITER $

CREATE PROCEDURE UpdateRecordById(
    IN _recordId INT,
	IN _artistId INT,
    IN _name VARCHAR(255),
    IN _field VARCHAR(255),
    IN _recorded INT,
    IN _label VARCHAR(255),
    IN _pressing VARCHAR(255),
    IN _rating VARCHAR(255),
    IN _discs INT,
    IN _media VARCHAR(255),
    IN _bought VARCHAR(255),
    IN _cost VARCHAR(255),
    IN _review TEXT
)
BEGIN
    UPDATE Record
    SET artistId = _artistId, name = _name, field = _field, recorded = _recorded,
        label = _label, pressing = _pressing, rating = _rating,
        discs = _discs, media = _media, bought = _bought,
        cost = _cost, review = _review
    WHERE
        RecordId = _recordId;
END $

DELIMITER ;



DELIMITER $
 
 CREATE PROCEDURE DeleteRecordById(
    IN _recordId INT
)
BEGIN
	DELETE FROM Record WHERE RecordId = _recordId;
END $

DELIMITER ;


DELIMITER $

CREATE PROCEDURE GetRecordByName(
    IN _name VARCHAR(255)
)
BEGIN
    SELECT name, recorded, media, bought, cost FROM Record WHERE Name LIKE CONCAT('%', _name, '%');
END $

DELIMITER ;


DELIMITER $

CREATE PROCEDURE GetArtistIdByNames(
IN _firstName VARCHAR(255), 
IN _lastName VARCHAR(255)
)
BEGIN
    SELECT ArtistId FROM Artist WHERE FirstName = _firstName AND LastName = _lastName;
END $

DELIMITER ;


DELIMITER $

CREATE PROCEDURE GetRecordById(
    IN _recordId INT
)
BEGIN
    SELECT recordId, artistId, name, field, recorded, label, pressing, rating, discs, media, bought, cost, review
    FROM Record
    WHERE recordId = _recordId;
END $

DELIMITER ;