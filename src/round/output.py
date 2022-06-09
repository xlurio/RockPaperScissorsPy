GAME_TITLE = 'Rock-Paper-Scissors Ultimate'
USER_CHOICE_HEADER = (
    '[R]ock\n'
    '[P]aper\n'
    '[S]cissors\n'
    'Make your choice: \n'
)
CHOICE_LABELS = ('Rock', 'Paper', 'Scissors')
RESULT_MESSAGES = (
    'YOU WIN!',
    'YOU LOSE!',
    'DRAW!',
)

def _highlight_text(text):
    text_separator = f'{"*"*20}\n'
    return text_separator + text + '\n' + text_separator

class Output:

    def get_game_title():
        return _highlight_text(GAME_TITLE)

    def get_user_choice_header():
        return USER_CHOICE_HEADER

    def get_round_choices(choice1, choice2):
        choice1 = choice1.get_choice()
        choice1_label = CHOICE_LABELS[choice1]

        choice2 = choice2.get_choice()
        choice2_label = CHOICE_LABELS[choice2]

        message = f'{choice1_label} vs {choice2_label}'

        return _highlight_text(message)

    def get_result_message(result):
        result_message = RESULT_MESSAGES[result]
        return _highlight_text(result_message)
