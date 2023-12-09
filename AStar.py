from abc import ABC
from Algo import Algo
from state import State
from levels import Levels


class AStar(Algo, ABC):
    lev = Levels.level42
    st = State(lev)
    visited = {}

    def __init__(self):
        self.parent_key = ""
        self.pQueue = []
        self.path = []

    def print_path(self, current_state):
        temp_state = current_state
        while temp_state.parent != "":
            self.path.append(temp_state)  # win state -> root
            temp_state = self.visited[temp_state.parent]
        for node in self.path[::-1]:
            print(node)
            print("---------------------------------------")

    def sorting(self):
        sorting_list = []
        m = len(self.pQueue)
        while len(sorting_list) != m:
            first_state = self.pQueue[0]
            f_first_state = first_state.cost + first_state.heuristic
            # for to get the smallest cost
            for state in self.pQueue:
                f_state = state.cost + state.heuristic
                if f_state < f_first_state:
                    first_state = state
            sorting_list.append(first_state)
            self.pQueue.remove(first_state)
        return sorting_list

    def play(self):
        self.pQueue.append(self.st)
        self.visited[str(self.st)] = self.st
        self.parent_key = str(self.st)
        counter = 0
        while self.pQueue:
            counter += 1
            current_state = self.pQueue.pop(0)
            print("Cost & Heuristic = ", current_state.cost + current_state.heuristic)
            print("The current_state is:\n", str(current_state))
            print("The heuristic is: \t", current_state.heuristic)
            print("The cost is: \t", current_state.cost)
            print("\n---------------------------------------------\n")
            self.visited[str(current_state)] = current_state
            self.parent_key = str(current_state)
            # check if the current state is a win state
            if current_state.isfinish():
                self.print_path(current_state)
                print("The cost is: \t", current_state.cost)
                print("path:\t", len(self.path), "\nstates:\t", counter)
                print("You Win Congrats")
                return
            else:
                next_states = current_state.next_state()
                for state in next_states:
                    if self.visited.get((str(state)), -1) == -1:
                        self.pQueue.append(state)
                        state.parent = self.parent_key
                        #
                        # self.visited[str(state)] = state
                        # self.parent_key = str(state)
                self.pQueue = self.sorting()
