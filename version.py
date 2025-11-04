import datetime


def get_version_with_date(version_number):
    """Function returns version with date and time"""
    today_date = datetime.datetime.now().strftime("%y%m%d%H%M")
    version_with_date = f"{today_date}_{version_number}"
    return version_with_date


version_number = "1.0.0"
version = get_version_with_date(version_number)
print(version + ".zip")
