"""The function move(my_history, their_history) must return "r", "p", or "s".
my_history and their_history are strings of the same length, perhaps length zero.
"""
import random
strategy_name = "RP Random S"




def random_move():
    pick = random.choice(["r", "p", "s"])
    return str(random)

def move(my_history, their_history):
    my_move = "r"
    if len(my_history) % 4 == 0:
        my_move = "r"
    elif len(my_history) % 4 == 1:
        my_move = "p"

    elif len(my_history) % 4 == 2:
        my_move = random_move()

    elif len(my_history) % 4 == 3:
        my_move = "s"



    return my_move


