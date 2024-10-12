# MAZE CODE AAAA JUSKO HIRAP SANA ETO NA YON
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

trial = 25
def game():
    while not at_goal():
        global trial
        if trial == 0:
            break
        else:
            if right_is_clear():
                turn_right()
                move()
                trial -= 1
            elif front_is_clear():
                move()
            else:
                turn_left()
game()
if front_is_clear():
    move()
else:
    turn_left()
trial += 25
game()
'''

# MORE OPTIMIZED SOLUTION
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

trial = 25
while not at_goal():
    if trial == 0:
        if front_is_clear():
            move()
        else:
            turn_left()
        trial += 25
    else:
        if right_is_clear():
            turn_right()
            move()
            trial -= 1
        elif front_is_clear():
            move()
        else:
            turn_left()
'''
 # MORE OPTIMIZEDDDD
'''
 def turn_right():
    turn_left()
    turn_left()
    turn_left()

trial = 25
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        trial -= 1
        if trial == 0:
            if front_is_clear():
                move()
            else:
                turn_left()
            trial += 25
    elif front_is_clear():
        move()
    else:
        turn_left()
'''