class Record():
    def __init__(self, date, record_list):
        opening, high, low, closing, total = record_list
        self.date = date
        self.opening = opening
        self.high = high
        self.low = low
        self.closing = closing
        self.total = total

    def __str__(self):
        return "{}\t{}\t{}\t{}\t{}\t{}".format(self.date, self.opening, self.high, self.low, self.closing, self.total)
