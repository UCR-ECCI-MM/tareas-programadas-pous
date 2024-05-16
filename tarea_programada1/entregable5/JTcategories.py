import pandas as pd

class Categories():
    def __init__(self):
        self.values = []
        
    def add_value(self, value):
        self.values.append(value)
        
    def create_series(self):
        self.categories = pd.Series(self.values)
        return self.categories
        
    def save_csv(self):
        self.categories.to_csv('categories.csv', index=False)