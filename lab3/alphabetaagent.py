from exceptions import AgentException
from connect4 import Connect4


class AlphaBetaAgent:
    def __init__(self, my_token='o', depth=4, enable_heuristics=True):
        self.my_token = my_token
        self.depth = depth
        self.enable_heuristics = enable_heuristics

    def decide(self, connect4: Connect4):
        if connect4.who_moves != self.my_token:
            raise AgentException('not my round')

        BestValue = float('-inf')
        BestColumn = None

        for column in connect4.possible_drops():
            connect4.drop_token(column)
            value = self.alphabeta(connect4, False, self.depth - 1, float('-inf'), float('inf'))
            connect4.undrop_token(column)

            if value > BestValue:
                BestValue = value
                BestColumn = column

        return BestColumn

    def alphabeta(self, connect4: Connect4, maximizing: bool, depth: int, alpha: float, beta: float) -> float:
        if connect4.game_over:
            if connect4.wins == self.my_token:
                return 1.0
            elif connect4.wins is not None:
                return -1.0
            else:
                return 0.0

        if depth <= 0:
            if self.enable_heuristics:
                return connect4.evaluate(self.my_token)
            else:
                return 0.0

        if maximizing:
            value = float('-inf')
            for n_column in connect4.possible_drops():
                connect4.drop_token(n_column)
                value = max(value, self.alphabeta(connect4, False, depth - 1, alpha, beta))
                connect4.undrop_token(n_column)

                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = float('inf')
            for n_column in connect4.possible_drops():
                connect4.drop_token(n_column)
                value = min(value, self.alphabeta(connect4, True, depth - 1, alpha, beta))
                connect4.undrop_token(n_column)

                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value