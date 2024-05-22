from turn_priority import TurnPriority


def manager(turns:TurnPriority) -> None:
    """
    Manage the turn system. 
    Start by taking the customers' turns, then organize them by priority 
    and return them to the advisors for handling it
    """

    print('Bienvenido a Turn-B, sistema de gestión de turnos')
    print('Se va a habilitar la toma de turnos')
    print('Por favor en cada linea seleccioné la opción correspondiente con el tipo de perfil del cliente')
    
    taking_turns = True
    while taking_turns:
        print('Escribe cuál es la categoría del cliete o finaliza la toma de turnos con [F]:')
        option = str(input('Cliente Normal[N], Buena Gente[B] o Prioritario[P]'))

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

    print('T')        


def run() -> None:
    turns = TurnPriority()
    manager(turns)
    advisor(turns)


if __name__ == "__main__":
    run()