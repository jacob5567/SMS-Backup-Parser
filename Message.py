class Message():
    def __init__(self, body, name, date, readable_date):
        self.body = body
        self.name = name
        self.date = date
        self.readable_date = readable_date

    def __str__(self):
        return "{}: {}".format(self.name, self.body)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.date < other.date

    def __le__(self, other):
        return self.date <= other.date

    def __gt__(self, other):
        return self.date > other.date

    def __ge__(self, other):
        return self.date >= other.date

    def __eq__(self, other):
        return self.date == other.date

    def __ne__(self, other):
        return self.date != other.date
