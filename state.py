import copy

from levels import manhattan_distance


class State:
    def __init__(self, state):
        self.state = state
        self.row = state[0]
        self.columns = state[1]
        self.grid = state[2]
        self.players = state[3]
        self.parent = ""
        self.to_win = state[4]
        self.cost = state[5]
        self.heuristic = state[6]

    def start_state(self):
        # to Get the  grid from the user
        self.random_map()

    # Getting the levels or map from the  player
    def random_map(self):
        self.row = int(input("Enter the number of rows\n"))
        self.columns = int(input("Enter the number of columns\n"))
        self.grid = [self.row][self.columns]
        for i in range(0, self.row):
            for j in range(0, self.columns):
                self.grid[i][j] = int(input())
        number_of_player = int(input("Enter how many squares player will be"))
        for i in range(0, number_of_player):
            player_rows = int(input("Enter the Start point indexes for rows\n"))
            player_columns = int(input("Enter the Start point indexes for columns\n"))
            player = (player_rows, player_columns)
            self.players.append(player)

    def isfinish(self):
        for player in self.players:
            # print("This is the player", player)
            # print("You should go to ", self.to_win)
            if player == self.to_win:
                return True
        return False

    def can_move(self, x, y):
        cells = []
        possible_moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for j, k in possible_moves:
            if self.row > j >= 0 and self.columns > k >= 0 and self.grid[j][k] > 0:
                cells.append((j, k))
        return cells

    def move(self, x, y, direction):
        # print("players list", self.players)
        player = self.players.index((x, y))
        to_move = (x + 1, y) if direction == 'D' \
            else (x - 1, y) if direction == 'U' \
            else (x, y + 1) if direction == 'R' \
            else (x, y - 1) if direction == 'L' \
            else (x, y)
        cells = self.can_move(x, y)
        if to_move in cells:
            # self.grid[to_move[0]][to_move[1]] -= 1
            # self.to_win -= 1
            self.players[player] = (to_move[0], to_move[1])
            self.state[2] = self.grid
            self.state[3] = self.players
            self.state[4] = self.to_win
            self.heuristic = manhattan_distance(self.players, self.to_win)
            self.state[6] = self.heuristic
            if direction == 'D' or direction == 'L':
                self.cost += (2 * self.grid[to_move[0]][to_move[1]])
            elif direction == 'R' or direction == 'U':
                self.cost += (1 * self.grid[to_move[0]][to_move[1]])
            self.state[5] = self.cost
            return True
        return False

    def next_state(self):
        directions = ['R', 'U', 'L', 'D']
        states = []
        states.append(State(self.state))
        new_state = copy.deepcopy(State(self.state))
        for player in self.players:
            for direction in directions:
                if new_state.move(player[0], player[1], direction):
                    states.append(new_state)
                    new_state = copy.deepcopy(State(self.state))
        return states

    def __str__(self):
        s = ''
        for row in self.grid:
            for cell in row:
                s += str(cell) + " "
            s += "\n"
        s += str(self.players)
        return s

    # stat1 < state2 => True or False
    def __lt__(self, other):
        return self.cost < other.cost

