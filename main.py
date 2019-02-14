import datetime, time, logging, traceback
from util.RequestTemp import RequestTemp
from util.Scraper import scrape_stock, check_reach_end
from util.model.Stock import Stock
from util.Util import *

def request_scrape_stocks(url, header, payload, method):
    name = get_stock_name(payload["stockCode"])
    stock = import_stock_from_file(name, payload["stockCode"])
    while (True):
        print("Scraping {} P.{}".format(name+"-"+payload["stockCode"], payload["p"].zfill(4)))
        aReq = RequestTemp(url, header, payload, method)
        aReq.send()
        stock, hv_new = scrape_stock(stock, aReq.res.content)
        end = check_reach_end(stock, payload["fromDate"])
        if (end or not hv_new):
            export_stock_to_file(stock)
            return stock
        payload["p"] = str(int(payload["p"]) + 1)
        time.sleep(10)
        
url, header, payload, method = init_require_data()

stock_list = ["0823","1716"]
try:
    for stock in stock_list:
        payload["stockCode"] = stock.zfill(4)
        payload["fromDate"] = "1990-01-01"
        payload["toDate"] = datetime.date.today().strftime("%Y-%m-%d")
        stock_obj = request_scrape_stocks(url, header, payload, method)
        export_stock_to_csv(stock_obj)
        time.sleep(5)
except Exception as e:
    logging.error(traceback.format_exc())
