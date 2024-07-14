import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#def mouse_click_coordinate(x, y):
#    print(x, y)


#turtle.onscreenclick(mouse_click_coordinate)
#turtle.mainloop()

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer = turtle.textinput(title=f"{len(guessed_states)}/50 states correct",
                              prompt="What's the state name?", ).title()

    if answer == "Exit":
        missing_states = []
        for i in states:
            if i not in guessed_states:
                missing_states.append(i)
        df = pd.DataFrame(missing_states, columns=["Missing States"])
        df.to_csv('missing_states.csv', index=False)
        break
    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())
