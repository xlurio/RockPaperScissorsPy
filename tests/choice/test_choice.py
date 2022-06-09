import unittest

from src.choice import Choice
from src.choice.exceptions import InvalidChoiceException


class UserChoiceTests(unittest.TestCase):
    """Tests for the user choice class"""

    def test_valid_choice(self):
        """Test valid user input"""
        choice = Choice('r')
        self.assertTrue(choice.is_valid())
        self.assertEqual(choice.get_choice(), 0)

    def test_invalid_choice(self):
        """Test invalid user input"""
        choice = Choice('h')
        self.assertFalse(choice.is_valid())
        with self.assertRaises(InvalidChoiceException):
            choice.get_choice()


if __name__ == '__main__':
    unittest.main()
