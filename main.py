from AStar import AStar
from UCS import UCS
from hill_climbing import HillClimbing
from state import State
from solo import UserPlayer
from DFS import DFS
from BFS import BFS
from recursive_DFS import RecursiveDFS
from levels import Levels

lev = Levels.level14
st = State(lev)

print("Logic steps Games")
print("Choose the way to solve the problem")
meth = input("Enter 1 to play the game lonely\n"
             "Enter 2 to solve the problem using BFS algo\n"
             "Enter 3 to solve the problem using DFS algo\n"
             "Enter 4 to solve the problem using DFS Recursively algo\n"
             "Enter 5 to solve the problem using UCS algo\n"
             "Enter 6 to solve the problem using HillClimbing algo\n"
             "Enter 7 to solve the problem using AStar\n")
match meth:
    case "1":
        print("Start play the Game by your self")
        user_player = UserPlayer()
        user_player.play()
    case "2":
        print("Solve the game by the Algorithms BFS")
        algo = BFS()
        algo.play()

    case "3":
        print("Solve the game by the  Algorithms DFS")
        algo = DFS()
        algo.play()

    case "4":
        print("Solve the game by the  Algorithms Recursive DFS")
        algo = RecursiveDFS()
        algo.play(st)

    case "5":
        print("Solve the game by the  Algorithms UCS")
        algo = UCS()
        algo.play()

    case "6":
        print("Solve the game by the  Algorithms HillClimbing")
        algo = HillClimbing()
        algo.play()

    case "7":
        print("Solve the game by the  Algorithms AStar")
        algo = AStar()
        algo.play()
    case _:
        print("Wrong Entered Sorry")

