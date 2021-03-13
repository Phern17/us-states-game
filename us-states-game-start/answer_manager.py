import pandas
from turtle import Turtle


class AnswerManager(Turtle):
    def __init__(self):
        super(AnswerManager, self).__init__()
        self.hideturtle()
        self.penup()
        self.data = pandas.read_csv('50_states.csv')
        self.all_states = self.data['state'].to_list()

    def check_states(self, user_ans):
        return user_ans in self.all_states

    def plot_answer(self, destination):
        des_info = self.data[self.data['state'] == destination]
        self.goto(int(des_info.x), int(des_info.y))
        self.write(arg=f'{destination}', align='left')
