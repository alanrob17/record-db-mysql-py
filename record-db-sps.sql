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
    IN _coverName VARCHAR(255),
    IN _review TEXT,
	IN _freeDbId INT
	
)
BEGIN
    UPDATE Record
    SET artistId = _artistId, name = _name, field = _field, recorded = _recorded,
        label = _label, pressing = _pressing, rating = _rating,
        discs = _discs, media = _media, bought = _bought,
        cost = _cost, coverName = null, review = _review, freeDbId = null
    WHERE
        recordId = _recordId;
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


CALL GetRecordByName('Cutting Edge');
