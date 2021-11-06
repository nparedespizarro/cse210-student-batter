from time import sleep
from game import constants

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script, play, message):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._play = play
        self._message = message
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while True:
            self._cue_action("input", self._play)
            if self._play.get_play_state():
                
                self._cue_action("update", self._play)
                self._cue_action("output", self._play)
            sleep(constants.FRAME_LENGTH)
            if self._play.get_play_state() == False:
                self._cue_action("print", self._play)
                sleep(5)
                break
                

    def _cue_action(self, tag, play):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        if tag == "update":
            for action in self._script[tag]:
                action.execute(self._cast ,self._play)
        elif tag == "print":
                    for action in self._script[tag]:
                        action.execute(self._message)
        else:
            for action in self._script[tag]:
                action.execute(self._cast)