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

        for increment in range(self.size):
            piece_coordinate = self.get_ship_positions(start_row, start_column, direction, increment)
            self.positions.append(piece_coordinate)

        for piece_postion in self.positions:
            self.place_piece_in_board(piece_postion, board)

    def place_piece_in_board(self, piece_postion:tuple, board:list):
        x_position, y_position = piece_postion
        board[y_position][x_position] = self.name[0]
 
    def get_ship_positions(self, start_row:int, start_column:int, direction:str, increment:int):
        x_position = start_column
        y_position = start_row

        if direction == 'H':
            x_position += increment
        else:
            y_position += increment

        piece_coordinate = (x_position, y_position)
        return piece_coordinate

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

    def get_positions(self, messages:dict, has_direction:bool=False, is_attack:bool=False):
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

        start_row = int(start_row)
        start_column = int(start_column)
        coordinates = {'start_row': start_row, 'start_column':start_column}

        if is_attack:
            return coordinates

        ship = self.ships[-1]
        current_ship_positions = [ship.get_ship_positions(start_row, start_column, increment, direction) for increment in range(ship.size)]
        all_ships_positions = [position for ship in self.ships for position in ship.position]
        #TODO: Continuar la logica para evitar la superposición de barcos



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

            self.ships.append(new_ship)
            self.place_single_ship(new_ship)

    def place_single_ship(self, ship): 
        messages = {'row': 'Fila inicial: ', 'column': 'Columna inicial: ', 'direction': "Dirección (H para horizonatal, V para vertical): "}
        coordinates = self.get_positions(messages, True)

        while coordinates is False:
            coordinates = self.get_positions(messages, ship, True)

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
