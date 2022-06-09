from .abstract_choice import AbstractChoice
from .exceptions import InvalidChoiceException


class Choice(AbstractChoice):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2
    VALID_CHOICES = ['r', 'p', 's']
    RESULTS = [ROCK, PAPER, SCISSORS]

    def __init__(self, entered_choice=None):
        self.set_choice(entered_choice)

    def is_valid(self):
        return self._entered_choice in self.VALID_CHOICES

    def set_choice(self, entered_choice):
        if not entered_choice:
            raise InvalidChoiceException(
                f'A choice must be provided'
            )

        self._entered_choice = entered_choice.lower()

    def get_choice(self):
        if not self.is_valid():
            raise InvalidChoiceException(
                f'{self._entered_choice} is not a valid choice.'
            )

        choice_index = self.VALID_CHOICES.index(self._entered_choice)
        return self.RESULTS[choice_index]
