from bs4 import BeautifulSoup

def scrape_stock(stock, html):
    hv_new = False
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.select(".quote_text")
    for i in range(0, len(tags), 6):
        date = tags[i].text.strip()
        if (date not in stock.past_history):
            stock.add_record(date, [tags[i+ii].text.strip() for ii in range(1,6)])
            hv_new = True
    return stock, hv_new

def check_reach_end(stock, fromdate):
    for k in stock.past_history.keys():
        if k <= fromdate:
            return True
    return False
