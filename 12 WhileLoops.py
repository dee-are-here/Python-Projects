# This is a while loop. It will continue to run as long as the condition is true.
# While something is true, do something


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


number_of_hurdles = 6
while number_of_hurdles > 0:
    at_goal(False)
    jump()
    number_of_hurdles -= 1
    # This will print the number of hurdles left after
    print(number_of_hurdles)
    # each jump


while at_goal() == False:  # or while not at_goal(), will work, too
    jump()  # This will continue to run until at_goal() returns True


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()  # This will continue to run until at_goal() returns True,
        # but it will also check if there is a wall in front of the robot.
        # If there is a wall, it will jump. If there is no wall,
        # it will move forward.


# This is my program. It will continue to run until the robot reaches the goal.
# It will check if there is a wall in front of the robot.
# If there is a wall, it will jump. If there is no wall, it will move forward.

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
