class AbstractChoice:
    VALID_CHOICES = None
    RESULTS = None

    def is_valid(self):
        pass

    def set_choice(self, entered_choice):
        pass

    def get_choice(self):
        pass
