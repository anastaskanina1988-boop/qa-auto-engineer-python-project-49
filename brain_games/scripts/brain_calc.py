
import brain_games.engine
from brain_games.games.calc import DESCRIPTION, generate_round


def main():
    brain_games.engine.run_game(DESCRIPTION, generate_round)
