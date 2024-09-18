# Creación de las clases Ship, Player y BattleshipGame con sus respectivas subclases y metodos
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
        BOARD_POSITIONS = range(10)

        self.name = name
        self.board = [['' for _ in BOARD_POSITIONS ] for _ in BOARD_POSITIONS]
        self.hits = [['' for _ in BOARD_POSITIONS ] for _ in BOARD_POSITIONS]
        self.ships = []

    def get_positions(self, messages:dict, has_direction:bool=False):
        start_row = input(messages['row'])
        start_column = input(messages['column'])
        direction = None

        if has_direction:
            direction = input(messages['direction'])

        allowed_positions = {str(number) for number in range(1, 11)}
        allowed_directions ={"H", "V"}

        if start_row not in allowed_positions:
            return False
        elif start_column not in allowed_positions:
            return False
        elif has_direction and direction not in allowed_directions:
            return False

        coordinates = {'start_row': int(start_row), 'start_column':int(start_column), 'direction':direction}
        return coordinates

    def place_ships(self):
        #TODO: Implementar la verificación para no intentar superponer barcos
        allowed_ships = [Destroyer, Submarine, Battleship]
        total_ships = range(9)
        print(f"{self.name} coloca tus barcos")

        for actual_ship in total_ships:
            ship_selector = actual_ship % 3
            new_ship = allowed_ships[ship_selector]()
            print(f"{self.name}, coloca tu {new_ship.name} de tamaño {new_ship.name}")

            self.place_single_ship(new_ship)

    def place_single_ship(self, ship): 
        messages = {'row': 'Fila inicial: ', 'column': 'Columna inicial: ', 'direction': "Dirección (H para horizonatal, V para vertical): "}
        coordinates = self.get_positions(messages, True)

        while coordinates is False:
            coordinates = self.get_positions(messages, True)

        ship.place_ship(coordinates['start_row'], coordinates['start_column'], coordinates['direction'], self.board)

    def print_board(self, select_board:str):
        allowed_boards = {'ships_board':self.ships, 'impacts_board':self.hits}

        if select_board not in allowed_boards:
            return False

        for board_row in allowed_boards["select_board"]:
            current_row = ''.join(board_row)
            print(current_row)

    def attack(self, next_player_ships:list):
        #TODO: Implementar el ataque al barco del enemigo
        print(f"{self.name}, elige posición para atacar.")

        messages = {'row': 'Fila: ', 'column': 'Columna: '}
        coordinates = self.get_positions(messages)

        while coordinates is False:
            coordinates = self.get_positions(messages)



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
