import pandas as pd

class Questions():
    def __init__(self):
        self.category = []
        self.air_date = []
        self.question = []
        self.value = []
        self.answer = []
        self.round = []
        self.show_number = []
        self.questions_data = {"Category": self.category,
                "Air Date": self.air_date,
                "Question": self.question,
                "Value": self.value,
                "Answer": self.answer,
                "Round": self.round,
                "Show Number": self.show_number,}
        
    def add_category(self, category):
        self.category.append(category)
        
    def add_air_date(self, air_date):
        self.air_date.append(air_date)

    def add_question(self, question):
        self.question.append(question)

    def add_value(self, value):
        self.value.append(value)

    def add_answer(self, answer):
        self.answer.append(answer)

    def add_round(self, round):
        self.round.append(round)
        
    def add_show_number(self, show_number):
        self.show_number.append(show_number)
        
    def create_dataframe(self):
        self.questions = pd.DataFrame(self.questions_data)
        
    def save_csv(self):
        # self.questions.to_excel("questions.xlsx", sheet_name="Sheet1")
        self.questions.to_csv('questions.csv', index=False)
