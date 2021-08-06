import csv
import time
import calendar
"""
    Part C
"""



# date_str_to_epoch(date) -> int
# date : string in "dd/mm/yyyy" fromat
def date_str_to_epoch(date):
    try:
    	timestamp = calendar.timegm(time.strptime(date, "%d/%m/%Y"))
    except Exception as ex:
        raise MyException("invalid date value")
    return timestamp

# moving_average(data, index, leng) -> float
# data: the data from csv file
# index: current row of the data
# leng: how many days needed to be taken into account 
def moving_average(data, index, leng):
    avg = 0.0
    try:
        for i in range(index - leng + 1, index+1):
            row = data[i]
            avg = avg + float(row['volumeto'])/float(row['volumefrom'])
    except Exception as ex:
        raise MyException("requested column is missing from dataset")

    return float((avg/leng))


# moving_avg_short(data, start_date, end_date) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  moving_avg_short(data, start_date, end_date):
    avg_short_dict = {}
    for i in range(len(data)):
        x = data[i]
        if (int(x['time']) >= start_date and int(x['time']) <= end_date):
            if (i >= 2):
                avg_short_dict[x['time']] = moving_average(data, i, 3)
            else:
                avg_short_dict[x['time']] = moving_average(data, i, i+1)
    return avg_short_dict



# moving_avg_long(data, start_date, end_date) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  moving_avg_long(data, start_date, end_date):
    avg_long_dict = {}
    for i in range(len(data)):
        x = data[i]
        if (int(x['time']) >= start_date and int(x['time']) <= end_date):
            if (i >= 9):
                avg_long_dict[x['time']] = moving_average(data, i, 10)

            else:
                avg_long_dict[x['time']] = moving_average(data, i, i+1)

    return avg_long_dict



# find_buy_list(short_avg_dict, long_avg_dict) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  find_buy_list(short_avg_dict, long_avg_dict):
    buy_list = {}
    keys = list(short_avg_dict.keys())
    prev = keys[0]
    for k in keys:
        if (short_avg_dict[k] > long_avg_dict[k] and short_avg_dict[prev] <= long_avg_dict[prev]):
            buy_list[k] = 1
        else:
            buy_list[k] = 0
        prev = k
    return buy_list



# find_sell_list(short_avg_dict, long_avg_dict) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  find_sell_list(short_avg_dict, long_avg_dict):
    sell_list = {}
    keys = list(short_avg_dict.keys())
    prev = keys[0]
    for k in keys:
        if (short_avg_dict[k] < long_avg_dict[k] and short_avg_dict[prev] >= long_avg_dict[prev]):
            sell_list[k] = 1
        else:
            sell_list[k] = 0
        prev = k
    return sell_list



# crossover_method(data, start_date, end_date) -> [buy_list, sell_list]
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def  crossover_method(data, start_date, end_date):
    start = date_str_to_epoch(start_date)
    end = date_str_to_epoch(end_date)
    short_avg_dict = moving_avg_short(data, start, end)
    long_avg_dict = moving_avg_long(data, start, end)
    buy_list_dict = find_buy_list(short_avg_dict, long_avg_dict)
    sell_list_dict = find_sell_list(short_avg_dict, long_avg_dict)

    buy_list = [time.strftime("%d/%m/%Y",  time.gmtime(int(x)))
                for x, v in buy_list_dict.items() if v == 1]
    sell_list = [time.strftime("%d/%m/%Y",  time.gmtime(int(x)))
                 for x, v in sell_list_dict.items() if v == 1]

    return buy_list, sell_list

if __name__ == "__main__":
    
    data = []
    with open("cryptocompare_btc.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]
    
    buy, sell = crossover_method(data, "01/05/2017", "12/06/2017")
    print(buy)
    print(sell)
    buy, sell = crossover_method(data, "05/09/2018", "27/09/2018")
    print(buy)
    print(sell)
    buy, sell = crossover_method(data, "03/11/2019", "14/11/2019")
    print(buy)
    print(sell)
    
    pass

