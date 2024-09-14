# Creación de las clases Ship, Player y BattleshipGame con sus respectivas subclases
class Ship:
    def __init__(self, name:str, size:int) -> None:
        #TODO: Crea los atributos del barco
        pass
    def place_ship(self) -> None:
        #TODO: Ubica el barco en el tablero y verifica que el barco no se salga del tablero
        pass

    def hit(self) -> None:
        #TODO: Gestionar la logica de los impactos del barco para el juego
        pass

class Destroyer(Ship):
    def __init__(self) -> None:
        super().__init__('Destructor', 2)

class Submarine(Ship):
    def __init__(self) -> None:
        super().__init__('Submarino', 3)

class Battleship(Ship):
    def __init__(self) -> None:
        super().__init__('Acorazado', 4)

class Player:
    def __init__(self, name:str) -> None:
        #TODO: Crea los atributos del jugador
        pass

    def place_ships(self) -> None:
        #TODO: Ubica los barcos en el tablero
        pass

    def print_board(self) -> None:
        #TODO: 
        pass

    def attack(self) -> None:
        #TODO: Gestiona la logica para el ataque a los barcos del enemigo
        pass

    def all_ships_sunk(self) -> None:
        #TODO: Consulta si todos los navios del rival fueron hundidos
        pass

class BattleshipGame:
    def __init__(self, player1:str, player2:str) -> None:
        #TODO: Inicializa los jugadores para empezar el juego
         pass

    def play(self) -> None:
        #TODO: Empieza el juego
        pass
