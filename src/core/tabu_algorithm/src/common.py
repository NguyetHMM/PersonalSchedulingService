import uuid
from datetime import datetime, timedelta
import calendar
import re
import math
from collections import Counter

WORD = re.compile(r"\w+")
MIN_DISTANCE = 15
MIN_COSINE_SIMILARITY = 0.8


def generate_uuid():
    return str(uuid.uuid4())


def string_to_datetime(datetime_string):
    return datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')


def sort_list_obj(list_obj, attr):
    return list_obj.sort(key=lambda x: x.attr)


def print_list_object(list_object):
    for item in list_object:
        print(item)


def weekday_count(start_date: datetime, end_date: datetime):
    week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }
    delta = end_date - start_date
    for i in range(delta.days + 1):
        day = calendar.day_name[(start_date + timedelta(days=i)).weekday()]
        week[day].append(start_date + timedelta(days=i))
    return week


def minutes_between_two_date(later_date, first_date):
    duration = later_date - first_date
    duration_in_s = duration.total_seconds()
    minutes = divmod(duration_in_s, 60)[0]
    return int(minutes)


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)
