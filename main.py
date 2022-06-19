from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# We're off to the races! Turtle lineup is set.
all_turtles = []
for turtle_index in range(0, 6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.color(colours[turtle_index])
	new_turtle.penup()
	new_turtle.speed(7)
	new_turtle.goto(x=-230, y=y_positions[turtle_index])
	all_turtles.append(new_turtle)

# The bet is in!
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour:").lower()
is_race_on = True

# Ready, set, go!
while is_race_on:
	for turtle in all_turtles:
		random_distance = random.randint(0, 10)
		turtle.forward(random_distance)
		if turtle.xcor() > 230:
			is_race_on = False
			winning_colour = turtle.pencolor()
			if winning_colour == user_bet:
				print(f"You've won! The {winning_colour} turtle is the winner!")
			else:
				print(f"You bet on the wrong turtle... The {winning_colour} turtle is the winner!")


screen.exitonclick()
