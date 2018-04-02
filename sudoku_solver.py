import numpy as np


class Sudoku():

    def __init__(self, values = None, domain = None):
        self.board = np.array(list(values)).astype(int).reshape(9, 9) if values else np.zeros(81).astype(int).reshape(9,9)
        self.domain = self.get_domain()

    def clone(self):
        new = Sudoku()
        new.board = np.array(self.board)
        new.domain = dict(self.domain)
        return new

    def get_domain(self):
        domain = {}
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    used = set(self.board[i]) | set(self.board[:, j]) | self.get_box_val((i, j))
                    domain[(i, j)] = set(range(1, 10)) - used
        return domain

    def update_domain(self):
        self.domain = self.get_domain()

    def get_box_val(self, ij):
        (i, j) = ij
        box_val = set()
        (i, j) = ((i // 3) * 3, (j // 3) * 3)
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                box_val.add(self.board[x][y])
        return box_val

    def get_mrv(self):
        return min(self.domain.items(), key=lambda x: len(x[1]))

    def gameover(self):
        return False if len(self.domain) else True

    def is_consistent(self):
        return True if {} in self.domain else False

    def backtrack(self):
        if self.gameover():
            return self.clone()
        var = self.get_mrv()
        for value in var[1]:
            sudoku = self.clone()
            sudoku.board[var[0]] = value
            sudoku.update_domain()
            result = sudoku.backtrack()
            if result is not None:
                return result
        return None

s = Sudoku('000000000302540000050301070000000004409006005023054790000000050700810000080060009')
sol = s.backtrack()
print(sol.board)

#to be continued