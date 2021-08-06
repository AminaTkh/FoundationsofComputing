import csv
import time
import calendar
"""
    Part D
"""

# Class Investment:
# Instance variables
#	start date
#	end date
#	data
# Functions
#	highest_price(data, start_date, end_date) -> float
#	lowest_price(data, start_date, end_date) -> float
#	max_volume(data, start_date, end_date) -> float
#	best_avg_price(data, start_date, end_date) -> float
#	moving_average(data, start_date, end_date) -> float


# date_str_to_epoch(date) -> int
# date : string in "dd/mm/yyyy" fromat
def date_str_to_epoch(date):
    timestamp = calendar.timegm(time.strptime(date, "%d/%m/%Y"))
    return timestamp


class Investment:
    def __init__(self, start_date, end_date, data):
        self.start_date = start_date
        self.end_date = end_date
        self.data = data

        # default_values(self, data, start_date, end_date)) -> data, start_date, end_date
        # data: the data from a csv file
        # start_date: string in "dd/mm/yyyy" format
        # end_date: string in "dd/mm/yyyy" format

    def default_values(self, data, start_date, end_date):
        if data == None:
            data = self.data
        if start_date == None:
            start_date = self.start_date
        if end_date == None:
            end_date = self.end_date
        return data, start_date, end_date
        
        # highest_price(data, start_date, end_date) -> float
        # data: the data from a csv file
        # start_date: string in "dd/mm/yyyy" format
        # start_date: string in "dd/mm/yyyy" format

    def highest_price(self, data, start_date, end_date):
        data, start_date, end_date = self.default_values(data, start_date, end_date)
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

    def lowest_price(self, data, start_date, end_date):
        data, start_date, end_date = self.default_values(data, start_date, end_date)
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
    def max_volume(self, data, start_date, end_date):
        data, start_date, end_date = self.default_values(data, start_date, end_date)
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
    def best_avg_price(self, data, start_date, end_date):
        data, start_date, end_date = self.default_values(data, start_date, end_date)
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

    def moving_average(self, data, start_date, end_date):
        data, start_date, end_date = self.default_values(data, start_date, end_date)
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

    pass

# lin_regression(dict_) -> y, m
# dict_: dictionary keys = days
# m: the gradient of a straight line
# y: prediction


def lin_regression(dict_):
    meanX = sum(dict_.keys()) / len(dict_.keys())
    meanY = sum(dict_.values()) / len(dict_.values())
    m_num = sum((xi - meanX)*(yi - meanY) for xi, yi in dict_.items())
    m_den = sum((xi - meanX)**2 for xi in dict_.keys())
    m = m_num/m_den
    b = meanY - m*meanX
    y = m * (list(dict_.keys())[-1] + 86400) + b
    return y, m


# predict_next_average(investment) -> float (predicted value)
# investment: Investment type
def predict_next_average(investment, line="volumeto"):
    start = date_str_to_epoch(investment.start_date)
    end = date_str_to_epoch(investment.end_date)
    dict_ = {}
    for i in range(len(investment.data)):
        x = data[i]
        if (int(x['time']) >= start and int(x['time']) <= end):
            if line == "volumeto":
                dict_[float(x['time'])] = float(
                    x['volumeto'])/float(x['volumefrom'])
            else:
                dict_[float(x['time'])] = float(x[line])
    y, grad = lin_regression(dict_)
    return y


# classify_trend(investment) -> str (increasing, decreasing, violate or other)
# investment: Investment type
def classify_trend(investment):
    start = date_str_to_epoch(investment.start_date)
    end = date_str_to_epoch(investment.end_date)
    high = {}
    low = {}
    for i in range(len(investment.data)):
        x = data[i]
        if (int(x['time']) >= start and int(x['time']) <= end):
            high[int(x['time'])] = (float(x['high']))
            low[int(x['time'])] = (float(x['low']))
    nexthigh, high_grad = lin_regression(high)
    nextlow, low_grad = lin_regression(low)

    if (high_grad > 0) and (low_grad > 0):
        str_res = "increasing"
    else:
        if (high_grad < 0) and (low_grad < 0):
            str_res = "decreasing"
        else:
            if (high_grad > 0) and (low_grad < 0):
                str_res = "violate"
            else:
                str_res = "other"
    return str_res


if __name__ == "__main__":
    data = []
    with open("cryptocompare_btc.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]

    inv1 = Investment("04/05/2015", "27/05/2015", data)
    inv2 = Investment("01/02/2016", "28/02/2016", data)
    inv3 = Investment("08/12/2016", "11/12/2016", data)
    dat1s = "01/01/2016"
    dat1e = "31/01/2016"
    dat2s = "01/02/2016"
    dat2e = "28/02/2016"
    dat3s = "01/12/2016"
    dat3e = "31/12/2016"

    print(predict_next_average(inv1))
    print(classify_trend(inv1))

    print(predict_next_average(inv2))
    print(classify_trend(inv2))

    print(predict_next_average(inv3))
    print(classify_trend(inv3))

    print(inv1.highest_price(data, dat1s, dat1e))
    print(inv1.highest_price(data, dat2s, dat2e))
    print(inv1.highest_price(data, dat3s, dat3e))

    print(inv1.lowest_price(data, dat1s, dat1e))
    print(inv1.lowest_price(data, dat2s, dat2e))
    print(inv1.lowest_price(data, dat3s, dat3e))

    print(inv1.max_volume(data, dat1s, dat1e))
    print(inv1.max_volume(data, dat2s, dat2e))
    print(inv1.max_volume(data, dat3s, dat3e))

    print(inv1.best_avg_price(data, dat1s, dat1e))
    print(inv1.best_avg_price(data, dat2s, dat2e))
    print(inv1.best_avg_price(data, dat3s, dat3e))

    print(inv1.moving_average(data, dat1s, dat1e))
    print(inv1.moving_average(data, dat2s, dat2e))
    print(inv1.moving_average(data, dat3s, dat3e))

