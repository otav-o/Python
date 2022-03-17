from datetime import date, time, datetime, timedelta


# .strftime(); .strptime
def discovering_date():
    actual_date = date.today()
    print(actual_date)
    print(actual_date.strftime('%w'))
    print(actual_date.strftime('%W'))
    print(actual_date.strftime('%D'))
    print(actual_date.strftime('%d > %m | %Y'))
    print(actual_date.strftime('%A %B %y'))


def discovering_time():
    my_time = time(hour=15, minute=18, second=30)
    time_str = my_time.strftime('%h:%m:%s')
    print(time_str)


def working_with_datetime():
    actual_date = datetime.now()
    print(actual_date)
    print(actual_date.strftime('%d/%m/%Y %H:%M:%S'))
    print(actual_date.strftime('%c'))
    print(actual_date.minute)
    print(actual_date.weekday())
    print(actual_date.second)

    created_date = datetime(2035, 12, 31, 11, 35, 0)
    print(created_date.strftime("%c"))

    string_date = "03/05/2027"  # you can add time
    converted_date = datetime.strptime(string_date, '%d/%m/%Y')
    print(converted_date.year)

    new_date = converted_date - timedelta(days=365, hours=2, minutes=12)
    print(new_date.strftime('%c'))


if __name__ == '__main__':
    # discovering_date()
    working_with_datetime()

# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

