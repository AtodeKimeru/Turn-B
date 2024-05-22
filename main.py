from turn_priority import TurnPriority


def manager(turns:TurnPriority) -> None:
    """
    Manage the turn system. 
    Start by taking the customers' turns, then organize them by priority 
    and return them to the advisors for handling it
    """

    print('____Bienvenido a Turn-B, sistema de gestión de turnos____')
    print('##Se va a habilitar la TOMA de turnos##')
    print('Por favor en cada linea seleccioné la opción correspondiente con el tipo de perfil del cliente')
    
    taking_turns = True
    while taking_turns:
        print('Escribe cuál es la categoría del cliete o finaliza la toma de turnos con [F]:')
        option = str(input('Cliente Normal[N], Buena Gente[B] o Prioritario[P]   '))

        if 'F' in option.upper():
            taking_turns = False
            print('Se ha finalizado la toma de turnos')

        elif 'N' in option.upper():
            turns.set_turn('N')

        elif 'B' in option.upper():
            turns.set_turn('B')

        elif 'P' in option.upper():
            turns.set_turn('P')

        else:
            print('Opción inválida, por favor seleccione una opción válida')
            continue
        

def advisor(turns:TurnPriority) -> None:

    print('____Bienvenido a Turn-B, sistema de gestión de turnos____')
    print('##Se va a habilitar la ATENCIÓN de turnos##')
    
    # While there are turns to attend
    while turns.get_all_turns():
        
        turn = turns.get_next_turn()
        print(f'Turno actual: {turn}')
        next = str(input('Escriba [OK] cuando desee dar por terminado el turno actual   '))
        
        try:
            if 'OK' == next.upper():
                turns.delete_turn(turn)
                print(f'Se ha atendido el turno {turn}')
        except ValueError:
            print('No se pudo atender el turno actual')

    print('No hay más turnos por atender')          


def run() -> None:
    turns = TurnPriority()
    manager(turns)
    advisor(turns)
    print('Gracias por usar Turn-B')


if __name__ == "__main__":
    run()