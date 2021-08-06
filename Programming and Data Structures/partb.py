import csv
import time
import calendar
"""
    Part B
"""


class MyException(Exception):

 # Exception message set by value
    def __init__(self, value):
        self.parameter = value

 # Exception message to be printed
    def __str__(self):
        return self.parameter


# date_str_to_epoch(date) -> int
# date : string in "dd/mm/yyyy" fromat
def date_str_to_epoch(date):
    try:
    	timestamp = calendar.timegm(time.strptime(date, "%d/%m/%Y"))
    except Exception as ex:
        raise MyException("invalid date value")
    return timestamp


# check_date(data, start_date, end_date) -> int
# data: the data from a csv file
# start_date: date in epoch format
# end_date: date in epoch format
def check_date(data, start_date, end_date):
    row = data[0]
    first = int(row["time"])
    row = data[-1]
    last = int(row["time"])
    if ((start_date < first) or (end_date > last)):
        raise MyException("date value is out of range")
    if (start_date > end_date):
        raise MyException("end date must be larger than start date")
    return True


# highest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# end_date: string in "dd/mm/yyyy" format

def highest_price(data, start_date, end_date):
    start = date_str_to_epoch(start_date)
    end = date_str_to_epoch(end_date)
    check_date(data, start, end)
    max_val = 0.0
    try:
    	for i in range(len(data)):
    		row = data[i]
    		if (int(row['time']) >= start and int(row['time']) <= end):
    			if (float(row['high']) > max_val):
    				max_val = float(row['high'])
    except Exception as ex:
    	raise MyException("requested column is missing from dataset")
    return max_val


# lowest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def lowest_price(data, start_date, end_date):
    start = date_str_to_epoch(start_date)
    end = date_str_to_epoch(end_date)
    check_date(data, start, end)
    min_val = float("inf")
    try:
        for i in range(len(data)):
            row = data[i]
            if (int(row['time']) >= start and int(row['time']) <= end):
                if (float(row['low']) < min_val):
                    min_val = float(row['low'])
    except Exception as ex:
        raise MyException("requested column is missing from dataset")
    return min_val


# max_volume(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def max_volume(data, start_date, end_date):
    start = date_str_to_epoch(start_date)
    end = date_str_to_epoch(end_date)
    check_date(data, start, end)
    max_val = 0.0
    try:
        for i in range(len(data)):
            row = data[i]
            if (int(row['time']) >= start and int(row['time']) <= end):
                if (float(row['volumefrom']) > max_val):
                    max_val = float(row['volumefrom'])
    except Exception as ex:
        raise MyException("requested column is missing from dataset")
    return max_val


# best_avg_value(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def best_avg_price(data, start_date, end_date):
    start = date_str_to_epoch(start_date)
    end = date_str_to_epoch(end_date)
    check_date(data, start, end)
    max_val = 0.0
    try:
    	for i in range(len(data)):
    		row = data[i]
    		if (int(row['time']) >= start and int(row['time']) <= end):
    			avg = float(row['volumeto'])/float(row['volumefrom'])
    			if (avg > max_val):
    				max_val = avg
    except Exception as ex:
    	raise MyException("requested column is missing from dataset")
    return max_val


# moving_average(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_average(data, start_date, end_date):
    start = date_str_to_epoch(start_date)
    end = date_str_to_epoch(end_date)
    check_date(data, start, end)
    avg = 0.0
    days = 0
    try:
        for i in range(len(data)):
            row = data[i]
            if (int(row['time']) >= start and int(row['time']) <= end):
                days += 1
                avg = avg + float(row['volumeto'])/float(row['volumefrom'])
    except Exception as ex:
        raise MyException("requested column is missing from dataset")
    return float("{:.2f}".format(avg/days))


if __name__ == "__main__":

    try:
    	data = []
    	try:
    		with open("cryptocompare_btc.csv", "r") as f:
    			reader = csv.DictReader(f)
    			data = [r for r in reader]
    	#commands here 
    		#print(moving_average(data, "29/08/2020", "29/09/2020"))	
    		
    			
    	except IOError as e:
    		raise MyException("dataset not found")
    	

    except MyException as e:
        print("Error: " + str(e))

