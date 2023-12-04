from abc import abstractmethod


class Algo:
    @abstractmethod
    def print_path(self, current_state):
        pass

