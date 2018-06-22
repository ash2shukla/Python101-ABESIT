from datetime import date, datetime


def dates():
    date_now = date.today()
    print(date_now)

    dob = date(1996, 8, 8)

    # Lets try to see how many days have i lived
    diff = date_now - dob
    print(diff)
    print(diff.days)

    print(dob.strftime("%m-%d-%y. %d %b %Y was a %A on the %d day of %B."))


def datetimes():
    datetime_now = datetime.now()
    dob = datetime(1996, 8, 8)
    diff = datetime_now - dob
    # diff is a timedelta object which has attribute total_seconds
    print(diff.total_seconds())
    print(datetime_now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.And the time is %I:%M:%S %p in 12 hours or %H:%M in 24 hours"))


if __name__ == "__main__":
    dates()
    datetimes()
