import pandas as pd
import datetime
from mongo_db import*

class Df:
    def __init__(self) -> None:
        self.data = {
                    "Id": [1, 2, 3, 4, 5, 6, 7],
                    "Name": ["Alex", "Justin", "Set", "Carlos", "Gareth", "John", "Bob"],
                    "Surname": ["Smur", "Forman", "Carey", "Carey", "Chapman", "James", "James"],
                    "Age": [21, 25, 35, 40, 19, 27, 25],
                    "Job": ["Python Developer", "Java Developer", "Project Manager", "Enterprise architect", "Python Developer", "IOS Developer", "Python Developer"],
                    "Datetime": [datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now(), datetime.datetime.now()]
                    }

    def make_dataframe(self):
        df = pd.DataFrame(self.data)

        return df 

    def insert_2_db(self):
        result = get_database(self.data)                   

if __name__ == "__main__":
    df = Df()

    df.make_dataframe() # Датафреим жасау
    df.insert_2_db() # Mongo db

