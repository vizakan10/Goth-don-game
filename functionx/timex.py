import random
from datetime import datetime


def time(output):
    current_datetime = datetime.now()
    year = str(current_datetime.year)
    month = str(current_datetime.month).zfill(2)
    day = str(current_datetime.day).zfill(2)
    hour = str(current_datetime.hour).zfill(2)
    minute = str(current_datetime.minute).zfill(2)
    second = str(current_datetime.second).zfill(2)

    random_number = random.randint(0, 9999)
    random_number_str = str(random_number).zfill(4)

    name = year + "_" + month + "_" + day + "_" + hour + "_" + minute + "_" + second + "_" + random_number_str + ".txt"
    return name,output