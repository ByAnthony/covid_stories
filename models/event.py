import datetime

class Event():
    
    def __init__(self, name, description, charity, fee, date, id=None):
        self.name = name
        self.description = description
        self.charity = charity
        self.fee = fee
        self.date = date
        self.guests = []
        self.id = id

    def convert_date(self):
        date = self.date
        date = datetime.datetime.strptime(str(date), "%Y-%m-%d")
        date = date.strftime("%d/%m/%Y")
        return date

    def check_in_guests(self, guest):
        self.guests.append(guest)
    
    def check_out_guests(self, guest):
        self.guests.remove(guest)