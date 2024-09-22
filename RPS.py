# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

from random import randint

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    guess = "R"
    n = 5  # Sequence length

    if len(opponent_history) >= n:
        recent = ''.join(opponent_history[-n:])
        sequences = [opponent_history[i:i+n] for i in range(len(opponent_history) - n)]
        next_moves = [opponent_history[i+n] for i, seq in enumerate(sequences) if seq == list(recent)]

        if next_moves:
            most_common = max(set(next_moves), key=next_moves.count)
            guess = {'R': 'P', 'P': 'S', 'S': 'R'}[most_common]

    if randint(0, 100) < 0:  # Probability to play a random move
        guess = ['R', 'P', 'S'][randint(0, 2)]

    return guess



