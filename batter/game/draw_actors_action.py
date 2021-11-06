from game.action import Action

class DrawActorsAction:
    """Draw the actors(bricks, ball, and bat) and also draw the actions(movement and placement).
    
    Steriotype:
        Responsive for the visual.
        
    Attributes:
        _output_service: The output_service class."""
    
    def __init__(self, output_service):
         """The constructor function."""
        
        self._output_service = output_service
        
    def execute(self, cast):
        """This function executes and tells the program to start drawing."""
        self._output_service.clear_screen()
        for i in cast:
            self._output_service.draw_actors(cast[i])
        self._output_service.flush_buffer()
        
        
