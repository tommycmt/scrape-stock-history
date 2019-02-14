from .Record import Record

class Stock():
    def __init__(self, name, no):
        self.name = name
        self.no = no
        self.past_history = dict()
        
    def add_record(self, date, record_list):
        record = Record(date, record_list)
        self.past_history[date] = record

    def show_past_history(self):
        print("Date      \tOpening\tHigh\tLow\tClosing\tTotal")
        for date in self.past_history:
            print(self.past_history[date])
