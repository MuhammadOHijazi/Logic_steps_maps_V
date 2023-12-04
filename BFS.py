from abc import ABC
from Algo import Algo
from state import State
from levels import Levels


class BFS(Algo, ABC):
    lev = Levels.level4
    st = State(lev)
    visited = {}

    def __init__(self):
        self.parent_key = str(self.st)
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
        queue = []
        queue.append(self.st)
        self.visited[str(self.st)] = self.st
        counter = 0
        while queue:
            counter += 1
            current_state = queue.pop(0)
            self.visited[str(current_state)] = current_state
            self.parent_key = str(current_state)
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
                        queue.append(state)
                        state.parent = self.parent_key
                        self.visited[str(state)] = state
                        self.parent_key = str(state)
