class Play:

    def __init__(self):
        self._keep_playing = True
        self._message ="YOU LOSE"

    def stop_play(self):
        self._keep_playing = False
    def get_play_state(self):
        return self._keep_playing
    def print_message(self):
        print(self._message)
    def get_message(self):
        return self._message
