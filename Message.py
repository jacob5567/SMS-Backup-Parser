class Message():
    def __init__(self, name, date, readable_date):
        self.name = name
        self.date = date
        self.readable_date = readable_date

    def __str__(self):
        return "**{}**: {}".format(self.name, "Blank Message")

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

class SMSMessage(Message):
    def __init__(self, name, date, readable_date, body):
        super().__init__(name, date, readable_date)
        self.body = body

    def __str__(self):
        return "**{}**: {}".format(self.name, self.body)

class MMSMessage(Message):
    def __init__(self, name, date, readable_date, parts):
        super().__init__(name, date, readable_date)
        self.parts = parts

    def __str__(self):
        return "**{}**:  \n{}".format(self.name, str(self.parts[0]))

class MMSPart():
    def __init__(self, ct, data, date):
        self.ct = ct
        self.data = data
        self.date = date

    def __str__(self):
        return "![Type: {}; Data: {}](img/{}_{})".format(self.ct, self.data, self.date, self.data) if self.ct != "text/plain" else self.data

    def __repr__(self):
        return self.__str__()
