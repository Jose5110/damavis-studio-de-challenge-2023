from data.settings import *

class Labyrinth():
    def __init__(self, config_key):
        self.config = config[config_key]
        self.array = self.array_generator()

    def array_generator(self):
        '''
        Using the values from the settings module it creates a 2D array of dimensions [x,y] in a list[list[str]] form
        using the provided free_space_chart, and then filling the blocked coordinates with the blocked_space_char.
        '''
        coordinates = self.config['blocked_coordinates']  
        
        array = [[free_space_char for _ in range(self.config['width'])] for _ in range(self.config['height'])]     
        for coord in coordinates:
            x, y = coord
            array[x][y] = blocked_space_char
        return array