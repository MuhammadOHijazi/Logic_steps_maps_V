from abc import ABC

from Algo import Algo
from state import State
from levels import Levels


class DFS(Algo, ABC):
    lev = Levels.level41
    st = State(lev)
    visited = {}

    def __init__(self):
        self.path = []

    def print_path(self, current_state):
        temp_state = current_state
        while temp_state.parent != "":
            self.path.append(temp_state)  # win state -> root
            temp_state = self.visited[temp_state.parent]
        for node in self.path[::-1]:
            print(node)
            print("---------------------------------------")

    def play(self):
        stack = []
        stack.append(self.st)
        counter = 0
        while stack:
            counter += 1
            # print("Counter: ", counter)
            current_state = stack.pop()
            self.visited[str(current_state)] = current_state
            parent_key = str(current_state)
            # check if the current state is a win state
            if current_state.isfinish():
                self.print_path(current_state)
                print("path:", len(self.path), "\nstates:", counter)
                print("You Win Congrats")
                return
            else:
                next_states = current_state.next_state()
                for state in next_states:
                    if self.visited.get((str(state)), -1) == -1:
                        stack.append(state)
                        state.parent = parent_key

