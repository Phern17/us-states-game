import turtle
from answer_manager import AnswerManager


screen = turtle.Screen()
screen.title("50 States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
answer_manager = AnswerManager()
correct_counter = 0

while correct_counter < 50:
    user_input = screen.textinput(title=f"{correct_counter}/50 States Correct",
                                  prompt="What's the next state's name?").title()

    if user_input == "Exit":
        answer_manager.export_csv()
        break

    if answer_manager.check_states(user_input):

        answer_manager.plot_answer(user_input)
        correct_counter += 1


