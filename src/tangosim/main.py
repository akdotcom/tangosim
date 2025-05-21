import sys
#sys.path.append("/home/thatcher/dev/tangosim/src/")
from tangosim.models import Tile
from tangosim.strategy import GreedyStrategy, RandomStrategy
from tangosim.gameengine import SimpleTangoGame

def main() -> None:
    player1_strategy = RandomStrategy(0)
    player2_strategy = GreedyStrategy(1)

    game = SimpleTangoGame([player1_strategy, player2_strategy])
    (game_state, last_player) = game.play()
    scores = game_state.get_scores()
    print(f"Score is {scores}")

    board_representation = game_state.get_human_readable_state()
    print("\nFinal board state:") # Use double backslash for newline in the string literal
    print(board_representation)

if __name__ == "__main__":
    main()