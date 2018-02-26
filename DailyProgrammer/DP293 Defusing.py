'''
Solves https://redd.it/5e4mde
'''

class Bomb:
    VALID_TRANSITIONS = {'red': ['green'],
                         'black': ['black', 'purple', 'red'],
                         'white': ['purple', 'red', 'green', 'orange'],
                         'purple': ['black', 'red'],
                         'green': ['white', 'orange'],
                         'orange': ['black', 'red'],
                         'any': ['white', 'black', 'purple', 'red', 'green', 'orange']
                         }

    def __init__(self):
        self.current_color = 'any'
        self.tripped = False

    def cut_wire(self, color):
        if self.tripped:
            pass
        elif color in self.VALID_TRANSITIONS[self.current_color]:
            self.current_color = color
        else:
            self.tripped = True

    def check_status(self):
        if self.tripped:
            print('Boom')
        else:
            print('Bomb defused')


if __name__ == '__main__':
    input_1 = ['white', 'red', 'green', 'white']
    input_2 = ['white', 'orange', 'green', 'white']

    b = Bomb()
    for color in input_1:
        b.cut_wire(color)
    b.check_status()

    for color in input_1:
        b.cut_wire(color)
    b.check_status()
