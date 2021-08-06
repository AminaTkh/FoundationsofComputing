import csv
import time
import calendar

"""
    Part A
"""


# date_str_to_epoch(date) -> int
# date : string in "dd/mm/yyyy" fromat
def date_str_to_epoch(date):
    timestamp = calendar.timegm(time.strptime(date, "%d/%m/%Y"))
    return timestamp

# highest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def highest_price(data, start_date, end_date):
    start = date_str_to_epoch(start_date)
    end = date_str_to_epoch(end_date)
    max_val = 0.0
    for i in range(len(data)):
        row = data[i]
        if (int(row['time']) >= start and int(row['time']) <= end):
            if (float(row['high']) > max_val):
                max_val = float(row['high'])

    return max_val


# lowest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def lowest_price(data, start_date, end_date):
    start = date_str_to_epoch(start_date)
    end = date_str_to_epoch(end_date)
    min_val = float("inf")
    for i in range(len(data)):
        row = data[i]
        if (int(row['time']) >= start and int(row['time']) <= end):
            if (float(row['low']) < min_val):
                min_val = float(row['low'])

    return min_val


# max_volume(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def max_volume(data, start_date, end_date):
    start = date_str_to_epoch(start_date)
    end = date_str_to_epoch(end_date)
    max_val = 0.0
    for i in range(len(data)):
        row = data[i]
        if (int(row['time']) >= start and int(row['time']) <= end):
            if (float(row['volumefrom']) > max_val):
                max_val = float(row['volumefrom'])

    return max_val


# best_avg_value(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def best_avg_price(data, start_date, end_date):
    start = date_str_to_epoch(start_date)
    end = date_str_to_epoch(end_date)
    max_val = 0.0
    for i in range(len(data)):
        row = data[i]
        if (int(row['time']) >= start and int(row['time']) <= end):
            avg = float(row['volumeto'])/float(row['volumefrom'])
            if (avg > max_val):
                max_val = avg

    return max_val


# moving_average(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_average(data, start_date, end_date):
    start = date_str_to_epoch(start_date)
    end = date_str_to_epoch(end_date)
    avg = 0.0
    days = 0
    for i in range(len(data)):
        row = data[i]
        if (int(row['time']) >= start and int(row['time']) <= end):
            days += 1
            avg = avg + float(row['volumeto'])/float(row['volumefrom'])

    return float("{:.2f}".format(avg/days))


if __name__ == "__main__":

    data = []
    with open("cryptocompare_btc.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]


    dat1s = "01/01/2016"
    dat1e = "31/01/2016"
    dat2s = "01/02/2016"
    dat2e = "28/02/2016"
    dat3s = "01/12/2016"
    dat3e = "31/12/2016"
    
    print(highest_price(data, dat1s, dat1e))
    print(highest_price(data, dat2s, dat2e))
    print(highest_price(data, dat3s, dat3e))

    print(lowest_price(data, dat1s, dat1e))
    print(lowest_price(data, dat2s, dat2e))
    print(lowest_price(data, dat3s, dat3e))

    print(max_volume(data, dat1s, dat1e))
    print(max_volume(data, dat2s, dat2e))
    print(max_volume(data, dat3s, dat3e))

    print(best_avg_price(data, dat1s, dat1e))
    print(best_avg_price(data, dat2s, dat2e))
    print(best_avg_price(data, dat3s, dat3e))

    print(moving_average(data, dat1s, dat1e))
    print(moving_average(data, dat2s, dat2e))
    print(moving_average(data, dat3s, dat3e))

    pass
