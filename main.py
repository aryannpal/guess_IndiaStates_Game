import turtle
import pandas as pd
screen=turtle.Screen()
screen.title('INDIA STATES')
image="India_Outline_Map.gif"
screen.setup(width=1000,height=790)
screen.addshape(image)
turtle.shape(image)
# turtle.shapesize(stretch_len=0.5,stretch_wid=0.5)

data=pd.read_csv('states_corr.csv')
all_states=data.states
list_all_states=all_states.to_list()

guessed_states=[]
while len(guessed_states)<28:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/28 Score",
                                  prompt="Enter The State Name").title()
    missing_states=[]
    if answer_state=='Exit':
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("Needs_to_learn")
        break

    if answer_state in list_all_states and answer_state is not guessed_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        row=data[data.states==answer_state]
        t.goto(row.x.item(),row.y.item())
        t.write(answer_state)



