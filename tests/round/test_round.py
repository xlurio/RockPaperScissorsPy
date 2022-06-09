import unittest
from src.choice import Choice
from src.round import Round

def round_factory(player1_entry, player2_entry):
    player1_choice = Choice(player1_entry)
    player2_choice = Choice(player2_entry)
    return Round(player1_choice, player2_choice)

class RoundTests(unittest.TestCase):

    def test_player1_win(self):
        """Tests the round result getter when player 1 win"""
        round = round_factory('r', 's')
        expected_result = Round.PLAYER_ONE_WIN
        output_result = round.get_result()
        self.assertEqual(output_result, expected_result)

    def test_player2_win(self):
        """Tests the round result getter when player 1 win"""
        round = round_factory('r', 'p')
        expected_result = Round.PLAYER_TWO_WIN
        output_result = round.get_result()
        self.assertEqual(output_result, expected_result)

    def test_draw(self):
        """Tests the round result getter when player 1 win"""
        round = round_factory('s', 's')
        expected_result = Round.DRAW
        output_result = round.get_result()
        self.assertEqual(output_result, expected_result)


if __name__ == '__main__':
    unittest.main()
