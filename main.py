import pandas
data=pandas.read_csv("50_states.csv") 
all_states=data.state.to_list()
import turtle
screen =turtle.Screen()
screen.title("U.S.States Game")

image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess=[]
while len(guess)<50:
    answer=screen.textinput(title=f"{len(guess)}/50",prompt="whats another state name").title()
    if answer == "Exit":
        missing_states=[state for state in all_states if state not in guess]
        # for state in all_states:
        #     if state not in guess:
        #         missing_states.append(state)
        #         #print(missing_states)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("missing.csv")
        break
    if answer in all_states:
        guess.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer)


