"""A simple minimax algorithm for a 2-player game."""

import math


def minimax(current_depth, node_i, is_max, scores):
    if current_depth <= 0:
        return scores[node_i]
    if is_max:
        return max(minimax(current_depth-1, node_i*2, False, scores),
            minimax(current_depth-1, node_i*2 + 1, False, scores));
    else:
        return min(minimax(current_depth-1, node_i*2, True, scores),
            minimax(current_depth-1, node_i*2 + 1, True, scores));

if __name__ == "__main__":
    scores = [3, 5, 2, 9]
    """
    Binary tree of each player's choices
    max            3
    min       3          2
    max    3     5    2     9

    is_max, current_depth, node_i --> current player's choice (scores[node_i])
    max 2.0 0 --> 3
        min 1.0 0 --> 3
            max 0.0 0 --> 3
            max 0.0 1 --> 5
        min 1.0 1 --> 2
            max 0.0 2 --> 2
            max 0.0 3 --> 9
    """
    h = math.log(len(scores), 2);
    print(minimax(h, 0, True, scores))

    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    """
    Binary tree of each player's choices
    max                        12
    min            5                      12
    max       5         9           12          23
    min    3    5    2     9     12    5     23    23

    is_max, current_depth, node_i --> current player's choice (scores[node_i])
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
    h = math.log(len(scores), 2);
    print(minimax(h, 0, True, scores))