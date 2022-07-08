import random


class TicTacToe:
    def __init__(self, complexity, human, computer):
        self.arr = [['' for _ in range(10)] for _ in range(10)]
        self.computer = computer
        self.human = human
        self.complexity = complexity
        self.free_moves = [(m, n) for m in range(10) for n in range(10)]

    def add_position(self, n, m, player):
        self.arr[n][m] = player()
        self.free_moves.remove((n, m))
        return self.arr[n][m], self.check(n, m, player)

    def opponent_move(self):
        if len(self.free_moves) == 100 or self.complexity == 'easy':
            n, m = random.choice(self.free_moves)
        elif self.complexity == 'hard':
            temp = self.free_moves[:]
            for i in range(len(self.free_moves)):
                n, m = random.choice(temp)
                temp.remove((n,m))
                self.arr[n][m] = self.computer()
                if self.check(n, m, self.computer, hard=True) == 0:
                    break
                self.arr[n][m] = ''
        return n, m

    def check(self, n, m, player, hard=False):
        for i in range(5):
            count = [0, 0, 0, 0]
            move = [[], [], [], [], []]
            for j in range(5):
                if 0 <= (tn := n - i + j) <= 9:
                    if self.arr[tn][m] == player():
                        count[0] += 1
                        move[0].append((tn, m))
                if 0 <= (tm := m - i + j) <= 9:
                    if self.arr[n][tm] == player():
                        count[1] += 1
                        move[1].append((n, tm))
                if 0 <= (tn := n - i + j) <= 9 and 0 <= (tm := m - i + j) <= 9:
                    if self.arr[tn][tm] == player():
                        count[2] += 1
                        move[2].append((tn, tm))
                if 0 <= (tn := n - i + j) <= 9 and 0 <= (tm := m + i - j) <= 9:
                    if self.arr[tn][tm] == player():
                        count[3] += 1
                        move[3].append((tn, tm))
            if 5 in count:
                if hard is True:
                    return 1
                for elem in move:
                    if len(elem) == 5:
                        return self.end(player), elem
        if self.free_moves is []:
            return self.standoff()
        return 0

    def end(self, player):
        return 'GameOver' if player == 'human' else 'Win'

    def standoff(self):
        return 'Ничья'
