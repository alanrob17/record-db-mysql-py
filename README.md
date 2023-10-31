# Record DB using MySql and Python

This project uses Python with MySql on a version of my Record DB.

My database name is **RecordDB** and I have two related collections of data named ``artists`` and ``records``.

This an example of the ``artists`` JSON.

 ```json
    {
     "artistid": 114,
     "firstname": "Bob",
     "lastname": "Dylan",
     "name": "Bob Dylan",
     "biography": "<p>Bob Dylan's influence...</p>"
    }
 ```

This is an example of the ``records`` JSON.

```json
 {
  "recordid": 1172,
  "artistid": 114,
  "name": "Blonde On Blonde",
  "field": "Rock",
  "recorded": 1966,
  "label": "Columbia",
  "pressing": "American",
  "rating": "Indispensible",
  "discs": 1,
  "media": "CD-Audio",
  "bought": "17 Feb 1999",
  "cost": "$14.00",
  "review": "<p>If Highway 61 Revisited...</p>"
 }
```

These collections are related on ``artists.artistid`` = ``records.artistid``.

I am building a number of routines using Python to consume data from the database.

## dependencies

```bash
    python -m pip install mysql-connector-python
```
