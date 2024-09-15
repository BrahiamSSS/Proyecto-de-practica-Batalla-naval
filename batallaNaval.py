# Creación de las clases Ship, Player y BattleshipGame con sus respectivas subclases
class Ship:
    def __init__(self, name:str, size:int):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0

    def place_ship(self, start_row:int, start_column:int, direction:str, board:list):
        vertical_size = len(board)
        horizontal_size = len(board[0])

        if start_row > vertical_size or start_column > horizontal_size:
            return False
        elif direction == 'H' and start_column + self.size > horizontal_size:
            return False
        elif direction == 'V' and start_row + self.size > vertical_size:
            return False

        self.positions.append([])
        for piece_position in range(self.size):
            self.place_ship_piece(start_row, start_column, direction, piece_position, board)
 
    def place_ship_piece(self, start_row:int, start_column:int, direction:str, piece_position:int, board:list):
        ship_coordinates = self.positions[-1]
        x_position = start_column
        y_position = start_row

        if direction == 'H':
            x_position += piece_position
            board[y_position][x_position] = self.name[0]
        else:
            y_position += piece_position
            board[y_position][x_position] = self.name[0]

        piece_coordinate = (x_position, y_position)
        ship_coordinates.append(piece_coordinate)

    def hit(self):
        self.hits += 1
        is_ship_sunk = self.hits == self.size

        if is_ship_sunk:
            return True

class Destroyer(Ship):
    def __init__(self):
        super().__init__('Destructor', 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__('Submarino', 3)

class Battleship(Ship):
    def __init__(self):
        super().__init__('Acorazado', 4)

class Player:
    def __init__(self, name:str):
        self.name = name
        self.board = [['' for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.hits = [['' for _ in range(10)] for _ in range(10)]

    def place_ships(self):
        #TODO: Ubica los barcos en el tablero
        pass

    def print_board(self):
        #TODO: 
        pass

    def attack(self):
        #TODO: Gestiona la logica para el ataque a los barcos del enemigo
        pass

    def all_ships_sunk(self):
        #TODO: Consulta si todos los navios del rival fueron hundidos
        pass

class BattleshipGame:
    def __init__(self, player1:str, player2:str):
        self.player1 = Player(player1)
        self.player2 = Player(player2)

    def play(self):
        #TODO: Empieza el juego
        pass
