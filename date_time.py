import datetime as dt

# Returns the weekday of the timestamp
def weekday(timestamp):
    return dt.date.fromtimestamp(timestamp).weekday()

# Return the hour of the timestamp
def hour_of_day(timestamp):
    return dt.datetime.fromtimestamp(timestamp).hour
