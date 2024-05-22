class TurnPriority:
    def __init__(self):
        self.turn_list = list()
        self.priority_list = list()

    def get_turn(self):
        if self.priority_list:
            return self.turn_list[0]

    def set_turn_priority(self, turn_priority):
        self.turn_priority = turn_priority