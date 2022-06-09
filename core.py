from src.choice import Choice, PlayerVsComChoicesFactory
from src.round import Round, Output


def get_user_choice():
    user_choice = Choice('placeholder')
    while not user_choice.is_valid():
        entered_choice = input(Output.get_user_choice_header())
        user_choice.set_choice(entered_choice)
    return user_choice


def get_com_choice():
    valid_choices = Choices.VALID_CHOICES
    number_of_valid_choices = len(valid_choices)
    com_entry_index = randrange(number_of_valid_choices)
    com_entry = valid_choices[com_entry_index]
    return Choice(com_entry)


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
