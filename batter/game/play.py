class Play:
    """The class play dicides if the game should cotinue or not.
    
    Stereotype:
        'Terminator'
        
    Attributes:
        _keep_playing: An boolean value.
        _message: An string."""

    def __init__(self):
        self._keep_playing = True
        self._message ="YOU LOSE"

    def stop_play(self):
        """"This function stops the game."""
        self._keep_playing = False
    def get_play_state(self):
        """"This function keeps the game running."""
        return self._keep_playing
    def print_message(self):
        """Prints the message."""
        print(self._message)
    def get_message(self):
        """"Gets the message."""
        return self._message
