class TurnPriority:
    def __init__(self):
        self.turn_list = list()
        self.priority_list = list()
        self.normal_list = list()
        self.good_people_list = list()


    def _priority_turns(self, turn) -> None:
        """
        Organize the turns by priority
        normal turn has 2 continuous turns for each 3 good people continuous turns
        """
        if 'N' in self.turn_list[-1]:
            
            if 'P' in self.turn_list[-2]:
                self.turn_list.insert(1, turn)

            
        elif 'B' in self.turn_list[-1]:

            self.turn_list.insert(1, turn)

    
    def get_next_turn(self) -> str|bool:
        """
        if there are turns return the first one according to their priority type
        if there are no turns return False
        """

        try:
            turns = self.get_all_turns()
            return turns[0]
        except IndexError:
            return False
    

    def delete_turn(self, turn_name:str) -> str:
        
        try:
            if 'P' in turn_name: 
                self.priority_list.remove(turn_name)
            self.turn_list.remove(turn_name)

            return f'Se eliminó el turno {turn_name}'
        
        except ValueError:
            return f'No se encontró el turno {turn_name}'


    def set_turn(self, turn:str) -> None:
        
        if 'P' == turn:
            turn_id = len(self.priority_list) + 1
            self.priority_list.append(f'P{turn_id}')

        else:
            if 'N' == turn:
                turn_id = len(self.normal_list) + 1
                turn_name = f'N{turn_id}'
                self.normal_list.append(turn_name)

            elif 'B' == turn:
                turn_id = len(self.good_people_list) + 1
                turn_name = f'B{turn_id}'
                self.normal_list.append(turn_name)

                if not self.turn_list:
                    self.turn_list.append(turn_name)
                               


    def get_all_turns(self) -> list:
        self._priority_turns()
        return self.priority_list + self.turn_list


    def __str__(self) -> str:
        return f'Turnos: {self.priority_list + self.turn_list}'
