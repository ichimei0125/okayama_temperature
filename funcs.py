import xlrd


def return_value(file_path, xl_date, value):
    book = xlrd.open_workbook(file_path)
    mode = book.datemode

    year, month, day, hour, minute, second = xlrd.xldate_as_tuple(xl_date, mode)

    if value == "month":
        return month
    if value == "day":
        return day
    if value == "year":
        return year


def month_to_str(month):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    return months[month-1]
