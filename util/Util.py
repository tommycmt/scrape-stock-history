import pickle
from .model.Stock import Stock
from .model.Record import Record
import os
import csv

data_path = __file__.rsplit(os.sep,2)[0] + '\data\\'

stock_name_dict = dict()

def init_require_data():
    with open(data_path + "code.csv", "r", encoding="utf-8") as f:
        for line in f:
            code, name = line.strip().split(",",1)
            stock_name_dict[code] = name
    url = "http://www.quamnet.com/Quote.action"
    header = {"host": "www.quamnet.com",
              "Origin": "www.quamnet.com",
              "Content-Type": "application/x-www-form-urlencoded",
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",}
    payload = {"p":"0",
               "quoteSectionCode": "pastprices",
               "stockCode": "",
               "fromDate": "",
               "toDate": "",
               "searchDateRange": "R",
               "btnSubmit": "start"}
    method = "get"
    return url, header, payload, method
            
def get_stock_name(no):
    return stock_name_dict[no.zfill(4)]

def import_stock_from_file(stock_name, stock_no):
    file_name = stock_name + "-" + stock_no + ".txt"
    if os.path.exists(data_path + file_name):
        with open(data_path + file_name, "rb") as f:
            stock = pickle.load(f)
        return stock
    return Stock(stock_name, stock_no)

def export_stock_to_file(stock):
    file_name = stock.name + "-" + stock.no + ".txt"
    with open(data_path + file_name, "wb") as f:
        pickle.dump(stock, f)
    print("{} is saved.".format(file_name))

def export_stock_to_csv(stock):
    file_name = stock.name + "-" + stock.no + ".csv"
    with open(data_path + file_name, "w", newline='') as f:
        stock_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
        stock_writer.writerow(['date', 'opening', 'high', 'low', 'closing', 'total'])
        for date in stock.past_history:
            record = stock.past_history[date]
            stock_writer.writerow([record.date, record.opening, record.high, record.low, record.closing, record.total])
