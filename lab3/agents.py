import random, sys
from copy import deepcopy
from typing import Literal
from abc import ABC, abstractmethod
from exceptions import AgentException
from heuristics import simple_score, advanced_score
from connect4 import Connect4


class Agent(ABC):
    def __init__(self, my_token="o", **kwargs):
        self.my_token = my_token

    @abstractmethod
    def decide(self, connect4):
        pass

    def __str__(self):
        return f"{self.my_token} ({self.__class__.__name__})"


class RandomAgent(Agent):
    def __init__(self, my_token="o", **kwargs):
        super().__init__(my_token, **kwargs)

    def decide(self, connect4):
        if connect4.who_moves != self.my_token:
            raise AgentException("not my round")
        return random.choice(connect4.possible_drops())


"""
class MinMaxAgent(Agent):
    def __init__(
            self, my_token="o", depth=4, heuristic: Literal["simple", "advanced"] = "simple"
    ):
        super().__init__(my_token)
        self.depth = depth
        self.heuristic = heuristic
        self.heuristic_fun = simple_score if heuristic == "simple" else advanced_score

    def __str__(self):
        return f"{self.my_token} ({self.__class__.__name__}+{self.heuristic})"

    def decide(self, connect4):
        if connect4.who_moves != self.my_token:
            raise AgentException("not my round")

        best_move, best_score = self.minmax(connect4, depth=self.depth)
        return best_move

    def minmax(self, connect4: Connect4, depth=4, maximizing=True):
        # TODO

        raise NotImplementedError()


class AlphaBetaAgent(MinMaxAgent):
    def __init__(
        self, my_token="o", depth=4, heuristic: Literal["simple", "advanced"] = "simple"
    ):
        super().__init__(my_token)
        self.depth = depth
        self.heuristic = heuristic
        self.heuristic_fun = simple_score if heuristic == "simple" else advanced_score

    def decide(self, connect4):
        if connect4.who_moves != self.my_token:
            raise AgentException("not my round")

        best_move, best_score = self.alphabeta(connect4, depth=self.depth)
        return best_move

    def alphabeta(
        self,
        connect4: Connect4,
        depth=4,
        maximizing=True,
        alpha=-sys.maxsize,
        beta=sys.maxsize,
    ):
        # TODO

        raise NotImplementedError()
"""


class MinMaxAgent:
    def __init__(self, my_token='o', depth=2, heuristic ="advanced"):
        self.my_token = my_token
        self.depth = depth
        self.enable_heuristics = heuristic

    def decide(self, connect4: Connect4):
        if connect4.who_moves != self.my_token:
            raise AgentException('not my round')

        best_value = float('-inf')
        best_column = None
        for n_column in connect4.possible_drops():
            connect4.drop_token(n_column)
            value = self.minmax(connect4, False, self.depth - 1)
            connect4.undrop_token(n_column)
            if value > best_value:
                best_value = value
                best_column = n_column

        return best_column

    def minmax(self, connect4: Connect4, maximizing: bool, depth: int) -> float:
        if connect4.game_over:
            if connect4.wins == self.my_token:
                return 1.0
            elif connect4.wins is not None:
                return -1.0
            else:
                return 0.0

        if depth <= 0:
            if self.enable_heuristics == "simple":
                return connect4.simple(self.my_token)
            elif self.enable_heuristics == "advanced":
                return connect4.advanced(self.my_token)
            else:
                return 0.0

        if maximizing:
            value = float('-inf')
            for n_column in connect4.possible_drops():
                connect4.drop_token(n_column)
                value = max(value, self.minmax(connect4, False, depth - 1))
                connect4.undrop_token(n_column)
            return value
        else:
            value = float('inf')
            for n_column in connect4.possible_drops():
                connect4.drop_token(n_column)
                value = min(value, self.minmax(connect4, True, depth - 1))
                connect4.undrop_token(n_column)
            return value


class AlphaBetaAgent:
    def __init__(self, my_token='o', depth=2, heuristic="advanced"):
        self.my_token = my_token
        self.depth = depth
        self.enable_heuristics = heuristic

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
            if self.enable_heuristics == "simple":
                return connect4.simple(self.my_token)
            elif self.enable_heuristics == "advanced":
                return connect4.advanced(self.my_token)
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
