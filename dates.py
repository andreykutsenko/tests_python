import datetime
import pytz
from dateutil.relativedelta import relativedelta

timezone = pytz.timezone("Europe/Minsk")
now_with_tz = timezone.localize(datetime.datetime.now())
now_formatted = now_with_tz.strftime("%m.%d.%Y")

print(now_with_tz)

now_plus_month = now_with_tz + relativedelta(months=-1)
print(now_plus_month)