import turtle
import pandas

image = "blank_states_img.gif"
csv_file = "50_states.csv"

screen = turtle.Screen()

screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv(csv_file)
data_state = data["state"].tolist()
game_on = True
turtle = turtle.Turtle()
turtle.pu()
turtle.hideturtle()
score = 0
screen.title(f"U.S. State game")
guess_states = []
while game_on:
    states_guess = screen.textinput(title=f"Guess the state's ({score}/50)",
                                    prompt="What's state's name?").capitalize()
    screen.update()


    for state in data_state:
        if states_guess == state:
            coordinate_coloum = data[data["state"] == state]
            guess_states.append(state)
            turtle.color("black")
            x_coordinate = int(coordinate_coloum["x"])
            y_coordinate = int(coordinate_coloum["y"])
            turtle.goto(x_coordinate, y_coordinate)
            turtle.write(state, align="center", font=("Arial", 8, "normal"))
            score += 1

    if score == 50 or states_guess == "Exit":
        for state in data_state:
            for state_guess in guess_states:
                if state != state_guess:
                    coordinate_coloum = data[data["state"] == state]
                    x_coordinate = int(coordinate_coloum["x"])
                    y_coordinate = int(coordinate_coloum["y"])
                    turtle.color("red")
                    turtle.goto(x_coordinate, y_coordinate)
                    turtle.write(state, align="center", font=("Arial", 8, "normal"))
        turtle.goto(0, 250)
        turtle.write(f"You guessed {score} state's correct", align="center", font=("Arial", 24, "normal"))

        game_on = False

screen.exitonclick()
