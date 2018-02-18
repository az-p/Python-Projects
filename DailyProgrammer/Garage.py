
class GarageDoor:
    """Solves https://redd.it/4cb7eh"""
    # Possible states
    states = ['OPEN', 'CLOSING', 'CLOSED', 'OPENING', 'STOPPED_WHILE_OPENING',
              'STOPPED_WHILE_CLOSING']

    # Map of values to add to change state
    button_map = [1, 4, 1, 1, -3, -2]
    complete_map = [0, 1, 0, -3, 0, 0]

    def __init__(self):
        # Initialize to closed
        self.current_state = 2

    def button_click(self):
        self.current_state += self.button_map[self.current_state]
        self.emit_state()

    def change_complete(self):
        self.current_state += self.complete_map[self.current_state]
        self.emit_state()

    def emit_state(self):
        print('Door: ', self.states[self.current_state])

if __name__ == "__main__":
    input_array = ['button_clicked', 'cycle_complete', 'button_clicked',
                   'button_clicked', 'button_clicked', 'button_clicked',
                   'button_clicked', 'cycle_complete']
    door = GarageDoor()

    door.emit_state()
    # Get input
    for ip in input_array:
        if ip == 'button_clicked':
            print('> Button clicked.')
            door.button_click()
        elif ip == 'cycle_complete':
            print('> Cycle complete.')
            door.change_complete()
        else:
            raise ValueError