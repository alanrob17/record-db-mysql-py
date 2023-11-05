from datetime import datetime


def roundOff(cost: float) -> float:
    if cost == None:
        cost = 0.0000

    return round(cost, 2)


def dateString(date: datetime) -> str:
    dateStamp = ""

    if date:
        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")

        if year == "1900" or year == None:
            dateStamp = ""
        else:
            dateStamp = f"{day}-{month}-{year}"

    return dateStamp
