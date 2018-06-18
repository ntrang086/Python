"""A simple minimax algorithm for a 2-player game."""

import math


def minimax(depth, node_i, is_max, scores):
    """Minimax without alpha-beta pruning.
    Paramters:
    depth: depth of the game tree. 0 means we're at a leaf
    node_i: index of the current node in scores
    is_max: whether max player is playing
    scores: list of scores at leaves
    """
    if depth <= 0:
        return scores[node_i]
    if is_max:
        return max(minimax(depth - 1, node_i * 2, False, scores),
            minimax(depth - 1, node_i * 2 + 1, False, scores))
    else:
        return min(minimax(depth - 1, node_i * 2, True, scores),
            minimax(depth - 1, node_i * 2 + 1, True, scores))

def minimax_alpha_beta(depth, node_i, is_max, scores, alpha, beta):
    """Minimax with alpha-beta pruning.
    Paramters:
    depth: depth of the game tree. 0 means we're at a leaf
    node_i: index of the current node in scores
    is_max: whether max player is playing
    scores: list of scores at leaves
    alpha: best value that the max player can guarantee at current level or above
    beta: best value that the min player can guarantee at current level or above
    """
    if depth <= 0:
        return scores[node_i]
    if is_max:
        v = float("-INF")
        for i in range(2):
            v = max(v, minimax_alpha_beta(depth - 1, node_i * 2 + i, False, scores, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
    else:
        v = float("INF")
        for i in range(2):
            v = min(v, minimax_alpha_beta(depth - 1, node_i * 2 + i, True, scores, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
    return v        


if __name__ == "__main__":
    # Test minimax
    scores = [3, 5, 2, 9]
    """
    Binary tree of each player's choices
    max               3
    min          3          2
    leaves    3     5    2     9

    is_max, depth, node_i --> current player's choice (scores[node_i])
    max 2.0 0 --> 3
        min 1.0 0 --> 3
            max 0.0 0 --> 3
            max 0.0 1 --> 5
        min 1.0 1 --> 2
            max 0.0 2 --> 2
            max 0.0 3 --> 9
    """
    # Height of the game tree
    h = math.log(len(scores), 2);
    assert minimax(h, 0, True, scores) == 3

    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    """
    Binary tree of each player's choices
    max                         12
    min               5                      12
    max          5         9           12          23
    leaves    3    5    2     9     12    5     23    23

    is_max, depth, node_i --> current player's choice (scores[node_i])
    max 3.0 0 --> 12
        min 2.0 0 --> 5
            max 1.0 0 --> 5
                min 0.0 0 --> 3
                min 0.0 1 --> 5
            max 1.0 1 --> 9
                min 0.0 2 --> 2
                min 0.0 3 --> 9
        min 2.0 1 --> 12
            max 1.0 2 --> 12
                min 0.0 4 --> 12
                min 0.0 5 --> 5
            max 1.0 3 --> 23
                min 0.0 6 --> 23
                min 0.0 7 --> 23
    """
    h = math.log(len(scores), 2)
    assert minimax(h, 0, True, scores) == 12
    assert minimax(h - 1, 0, True, scores) == 3

    # Test minimax_alpha_beta
    scores = [3, 5, 6, 9, 1, 2, 0, -1]
    h = math.log(len(scores), 2)
    assert minimax_alpha_beta(h, 0, True, scores, float("-INF"), float("INF")) == 5