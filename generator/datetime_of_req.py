from faker import Faker
from dateutil import tz
import random
import datetime

# `use_iso` determines if the output string should be in ISO-8601 format
# `fmt` is the format string that is used, if not using ISO format
#
# The default format string is the Apache default datetime format
def gen_datetime(test_mode=False, use_iso=False, fmt=None):
    fake = Faker()

    fake_tz = tz.gettz(fake.timezone())

    fake_time = fake.date_time(
        tzinfo=fake_tz,
        end_datetime=datetime.date.max)

    if use_iso:
        return fake_time.isoformat()
    else:
        return fake_time.strftime(
            '%d/%b/%Y:%H:%M:%S %z' if fmt is None else fmt)
