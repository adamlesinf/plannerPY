import datetime


def sprawdz_date(data):

    try:
        datetime.datetime.strptime(data, "%Y-%m-%d")
        if len(data) != 10:
            return False
        return True

    except ValueError:
        return False


def sprawdz_czas(godzina):
    try:
        datetime.datetime.strptime(godzina, '%H:%M')
        if len(godzina) != 5:
            return False
        return True

    except ValueError:
        return False


def sprawdz_nazwe(nazwa):
    if nazwa == "":
        return False
    return True
