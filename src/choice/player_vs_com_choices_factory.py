from .abstract_choices_factory import AbstractChoicesFactory
from .choice import Choice
from src.round import Output
from random import randrange

class PlayerVsComChoicesFactory(AbstractChoicesFactory):

    def make_player1_choice():
        player_choice = Choice('placeholder')
        while not player_choice.is_valid():
            entered_choice = input(Output.get_user_choice_header())
            player_choice.set_choice(entered_choice)
        return player_choice

    def make_player2_choice():
        valid_choices = Choice.VALID_CHOICES
        number_of_valid_choices = len(valid_choices)
        com_entry_index = randrange(number_of_valid_choices)
        com_entry = valid_choices[com_entry_index]
        com_choice = Choice(com_entry)
        return com_choice
