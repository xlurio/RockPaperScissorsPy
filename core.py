from src.choice import Choice, PlayerVsComChoicesFactory
from src.round import Round, Output


def print_choices(choice1, choice2):
    round_choices = Output.get_round_choices(choice1, choice2)
    print(round_choices)


def print_result(result):
    result_message = Output.get_result_message(result)
    print(result_message)


def main(choices_factory):
    # prints the game title
    print(Output.get_game_title())
    # Get player 1 choice
    player1_choice = choices_factory.make_player1_choice()
    # Get player 2 choice
    player2_choice = choices_factory.make_player2_choice()
    # Compare the user and the PC choice
    round = Round(player1_choice, player2_choice)
    round_result = round.get_result()
    # Show the choices
    print_choices(player1_choice, player2_choice)
    # Show the result
    print_result(round_result)


if __name__ == '__main__':
    main(PlayerVsComChoicesFactory)
