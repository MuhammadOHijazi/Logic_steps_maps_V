from abc import ABC
from Algo import Algo


class RecursiveDFS(Algo, ABC):
    visited = {}

    def __init__(self):
        self.path = []
        self.next_states = []
        self.counter = 0

    def print_path(self, current_state):
        temp_state = current_state
        while temp_state.parent != "":
            self.path.append(temp_state)  # win state -> root
            temp_state = self.visited[temp_state.parent]
        for node in self.path[::-1]:
            print(node)
            print("---------------------------------------")

    def play(self, state):
        current_state = state
        self.counter += 1
        self.visited[str(current_state)] = current_state
        parent_key = str(current_state)
        # check if the current state is a win state
        if current_state.isfinish():
            self.print_path(current_state)
            print("path:", len(self.path), "\nstates:", self.counter)
            print("You Win Congrats")
            return
        else:
            self.next_states = current_state.next_state()
            for state in self.next_states:
                # ToDO: Have to fix vistited method
                if self.visited.get((str(state)), -1) == -1:
                    self.next_states.append(state)
                    state.parent = parent_key
                    self.play(state)
