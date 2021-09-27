import datetime

class Memory():
    
    def __init__(self, title, contributor, story, date, charity, id=None):
        self.title = title
        self.contributor = contributor
        self.story = story
        self.date = date
        self.charity = charity
        self.id = id

    def convert_date(self):
        date = self.date
        date = datetime.datetime.strptime(str(date), "%Y-%m-%d")
        date = date.strftime("%d/%m/%Y")
        return date