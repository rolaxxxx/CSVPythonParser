import datetime

def IsDateFormatValid(dateString) -> bool:
    if len(dateString) <= 0:
        return False
    if dateString[0] == '0':
        return False
    if IsDateInvalid(dateString[0]):
        return False
    return True


def IsDateInvalid(date_text):
    try:
        datetime.datetime.strptime(date_text, "%m/%d/%Y")
        return False
    except ValueError:
        return True