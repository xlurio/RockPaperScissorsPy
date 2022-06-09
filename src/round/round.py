from src.choice.exceptions import InvalidChoiceException
from src.choice import Choice

class Round:
    PLAYER_ONE_WIN = 0
    PLAYER_TWO_WIN = 1
    DRAW = 2

    PLAYER_ONE_CHOICE = 0
    PLAYER_TWO_CHOICE = 1
    ROUND_RESULT = 2

    # (Player one choice, player two choice)
    ROUND_RESULTS = [
        (Choice.ROCK, Choice.ROCK, DRAW),
        (Choice.ROCK, Choice.PAPER, PLAYER_TWO_WIN),
        (Choice.ROCK, Choice.SCISSORS, PLAYER_ONE_WIN),
        (Choice.PAPER, Choice.ROCK, PLAYER_ONE_WIN),
        (Choice.PAPER, Choice.PAPER, DRAW),
        (Choice.PAPER, Choice.SCISSORS,PLAYER_TWO_WIN),
        (Choice.SCISSORS, Choice.ROCK, PLAYER_TWO_WIN),
        (Choice.SCISSORS, Choice.PAPER, PLAYER_ONE_WIN),
        (Choice.SCISSORS, Choice.SCISSORS, DRAW),
    ]

    def __init__(self, player1_choice: Choice, player2_choice: Choice):
        no_choice_provided = (not player1_choice) or (not player2_choice)
        if no_choice_provided:
            raise InvalidChoiceException("Missing choices")

        self.player1_choice = player1_choice.get_choice()
        self.player2_choice = player2_choice.get_choice()

    def get_result(self):
        result_matches = [
            self._does_choices_matches(result) \
                for result in self.ROUND_RESULTS
        ]
        index_of_match = result_matches.index(True)
        match = self.ROUND_RESULTS[index_of_match]
        return match[self.ROUND_RESULT]

    def _does_choices_matches(self, result):
        does_player1_choice_matches = (
            self.player1_choice == result[self.PLAYER_ONE_CHOICE]
        )
        does_player2_choice_matches = (
            self.player2_choice == result[self.PLAYER_TWO_CHOICE]
        )
        return (
            does_player1_choice_matches and does_player2_choice_matches
        )
