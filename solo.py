import levels as lev
import state as stat

import numpy as np


class UserPlayer:

    def play(self):
        state = stat.State(lev.Levels.level14)
        check = False
        # state.next_state()
        while True:
            print("The current Grid is:\n", state)
            print("The player in:", state.players)
            if len(state.players) > 1:
                user_index = int(input("Choose player: \n"))
                x, y = state.players[user_index] \
                    if 0 <= user_index < len(state.players) \
                    else state.players[-1]
            else:
                x, y = state.players[0]
            print("Your destination is : ", state.to_win)
            character = input("Enter the direction of move you want:\n"
                              "R for Right\n"
                              "D for Down\n"
                              "L for Left \n"
                              "U for UP\n"
                              "Q to quit the game\n")
            match character:
                case "R":
                    state.move(x, y, character)
                    check = state.isfinish()
                case "L":
                    state.move(x, y, character)
                    check = state.isfinish()
                case "U":
                    state.move(x, y, character)
                    check = state.isfinish()
                case "D":
                    state.move(x, y, character)
                    check = state.isfinish()
                case "q":
                    return
                case _:
                    print("Invalid Enter change the character")
            if check:
                print("You win the level Congrats")
                return
