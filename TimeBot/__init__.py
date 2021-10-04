from datetime import datetime
import pytz

time_str = """
**TIME** :- `{}`

**DATE** :- `{}`

**DAY** :- `{}`

**UTC** :- `{}`

**UNIX TIME** :- `{}`

**TIME ZONE** :- `{}`
"""


class TimeTeller:
    @staticmethod
    def india():
        present = datetime.now(tz=pytz.timezone("Asia/Kolkata"))
        time = present.strftime("%I:%M:%S %p")
        date = present.strftime("%d-%B-%Y")
        day = present.strftime("%A")
        utc = present.strftime("%z")
        unixtime = int(datetime.utcnow().timestamp())
        indian_time = time_str.format(time, date, day, utc, unixtime, "Asia/Kolkata")
        return indian_time

    @staticmethod
    def gmt():
        present = datetime.now(tz=pytz.timezone('GMT'))
        time = present.strftime("%I:%M:%S %p")
        date = present.strftime("%d-%B-%Y")
        day = present.strftime("%A")
        utc = present.strftime("%z")
        unixtime = int(datetime.utcnow().timestamp())
        gmt_time = time_str.format(time, date, day, utc, unixtime, "GMT")
        return gmt_time

    @staticmethod
    def particular(time_zone):
        try:
            present = datetime.now(tz=pytz.timezone(time_zone))
            time = present.strftime("%I:%M:%S, %p")
            date = present.strftime("%d-%B-%Y")
            day = present.strftime("%A")
            utc = present.strftime("%z")
            unixtime = int(datetime.utcnow().timestamp())
            particular_time = time_str.format(time, date, day, utc, unixtime, time_zone)
        except pytz.exceptions.UnknownTimeZoneError:
            particular_time = f"**Unknown Time Zone ** : '`{time_zone}`' is not a valid timezone. \n\n" \
                              "1) Send /timezones to check all timezones. \n" \
                              "2) Use '/search country/city' to search for  particular timezone."
        return particular_time
