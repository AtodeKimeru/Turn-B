class TurnPriority:
    def __init__(self):
        self.turn_list = list()
        self.sorted = False
        self.priority_list = list()
        self.normal_list = list()
        self.good_people_list = list()


    def _good_people_priority(self) -> None:
        """
        add 3 good people turns for each 2 normal turns
        if there are no normal turns add a good people turns
        if there are no good people turns call to _normal_priority method
        """
        if len(self.turn_list) >= 3 and self.normal_list:
            
            if 'B' in self.turn_list[-1]:
            
                if ('B' in self.turn_list[-2]) or (not self.good_people_list):
                
                    if 'B' in self.turn_list[-3] or (not self.good_people_list):
                        # case when the condition is valid but there are no good people turns
                        # or the case when the condintion is not valid
                        self._normal_priority()


        if self.good_people_list:
            # case when there are no normal turns in turn_list
            self.turn_list.append(self.good_people_list.pop(0))
            self._good_people_priority()


    def _normal_priority(self) -> None:
        """
        add 2 normal turns for each 3 good people turns
        if there are no good people turns add a normal turn
        if there are no normal turns call to _good_people_priority method
        """
        if len(self.turn_list) >= 2 and self.good_people_list:

            if 'N' in self.turn_list[-1]:
                
                if 'N' in self.turn_list[-2]:
                    # case when the condition is not valid
                    self._good_people_priority()
                elif not self.normal_list:
                    # case when there are no normal turns in normal_list
                    self._good_people_priority()
                

        if self.normal_list:
            # case when there are no good people turns in turn_list
            self.turn_list.append(self.normal_list.pop(0))
            self._normal_priority()


    def _priority_turns(self) -> None:
        """
        Organize the turns by priority
        normal turn has 2 continuous turns for each 3 good people continuous turns
        """
        if 'N' in self.turn_list[0]:
            
            self.normal_list.pop(0) # remove the first element of the list to avoid duplicates

            if len(self.normal_list) > 0:
                
                self._normal_priority()

            
        elif 'B' in self.turn_list[0]:

            self.good_people_list.pop(0) # remove the first element of the list to avoid duplicates

            if len(self.good_people_list) > 0:
                    
                self._good_people_priority()


    def get_turn_list(self) -> list:
        """
        Return a list with the no priority turns sorted by category
        normal turn has 2 continuous turns for each 3 good people continuous turns
        """
        if self.turn_list and not self.sorted:
            self._priority_turns()
            self.sorted = True

        return self.turn_list

    
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
        
        except TypeError:
            return f'No se encontró el turno'


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
                self.good_people_list.append(turn_name)

                if not self.turn_list:
                    self.turn_list.append(turn_name)
                               


    def get_all_turns(self) -> list:
        return self.priority_list + self.get_turn_list()


    def __str__(self) -> str:
        return f'Turnos: {self.priority_list + self.turn_list}'
