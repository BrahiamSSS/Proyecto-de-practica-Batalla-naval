# Creación de las clases Ship, Player y BattleshipGame con sus respectivas subclases y metodos
class Ship:
    def __init__(self, name:str, size:int):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0

    def place_ship(self, start_row:int, start_column:int, direction:str, board:list):
        is_correct_position = self.check_board_positions(start_row, start_column, direction, board)
        if not is_correct_position:
            return False

        for increment in range(self.size):
            piece_coordinate = self.get_ship_positions(start_row, start_column, direction, increment)
            self.positions.append(piece_coordinate)

        for piece_postion in self.positions:
            self.place_piece_in_board(piece_postion, board)

    def check_board_positions(self, start_row:int, start_column:int, direction:str, board:list):
        vertical_size = len(board)
        horizontal_size = len(board[0])

        if start_row > vertical_size or start_column > horizontal_size:
            return False
        elif direction == 'H' and start_column + self.size > horizontal_size:
            return False
        elif direction == 'V' and start_row + self.size > vertical_size:
            return False

        return True

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

        return False

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
        self.board = [[' ' for _ in BOARD_POSITIONS ] for _ in BOARD_POSITIONS]
        self.hits = [[' ' for _ in BOARD_POSITIONS ] for _ in BOARD_POSITIONS]
        self.ships = []

    def get_positions(self, messages:dict, has_direction:bool=False, is_attack:bool=False):
        start_row = input(messages['row'])
        start_column = input(messages['column'])
        direction = 'No direction defined'

        if has_direction:
            direction = input(messages['direction']).upper()

        allowed_positions = {str(number) for number in range(1, 11)}
        allowed_directions ={'H', 'V'}

        if start_row not in allowed_positions:
            return False
        elif start_column not in allowed_positions:
            return False
        elif has_direction and direction not in allowed_directions:
            return False

        coordinates = {'row': int(start_row) - 1, 'column':int(start_column) - 1, 'direction': direction}
        current_board_position = self.hits[coordinates['row']][coordinates['column']]
        is_available_hit_postion = ' ' == current_board_position

        if not is_available_hit_postion:
            return False
        elif is_attack:
            return coordinates

        ship = self.ships[-1]
        current_ship_positions = []
        for increment in range(ship.size):
            current_ship_positions.append(ship.get_ship_positions(coordinates['row'], coordinates['column'], coordinates['direction'], increment))

        all_ships_positions = self.get_all_ship_positions()
        available_positions = [True for actual_postion in current_ship_positions if actual_postion not in all_ships_positions]
        all_posions_are_allowed = False not in available_positions

        if not all_posions_are_allowed:
            return False

        is_available_board_position = ship.check_board_positions(coordinates['row'], coordinates['column'], coordinates['direction'], self.board)
        if not is_available_board_position:
            return False

        return coordinates

    def place_ships(self, clean_screen):
        allowed_ships = [Destroyer, Submarine, Battleship]
        total_ships = range(9)
        print(f'{self.name} coloca tus barcos')

        for actual_ship in total_ships:
            ship_selector = actual_ship % 3
            new_ship = allowed_ships[ship_selector]()
            print(f'{self.name}, coloca tu {new_ship.name} de tamaño {new_ship.size}')

            self.ships.append(new_ship)
            self.place_single_ship(new_ship, clean_screen)

    def place_single_ship(self, ship, clean_screen): 
        messages = {'row': 'Fila inicial: ', 'column': 'Columna inicial: ', 'direction': 'Dirección (H para horizonatal, V para vertical): '}
        coordinates = self.get_positions(messages, True)

        while coordinates is False:
            clean_screen()
            print('Las posiciones ingresadas no son validas')
            print(f'{self.name}, coloca tu {ship.name} de tamaño {ship.size}')
            coordinates = self.get_positions(messages, ship, True)

        ship.place_ship(coordinates['row'], coordinates['column'], coordinates['direction'], self.board)
        clean_screen()

    def print_board(self):
        main_messages = 'Elige el tablero a visualizar, para barcos ingresa (ships) y para impactos ingresa (impacts): '
        select_board = input(main_messages)
        allowed_boards = {'ships':self.board, 'impacts':self.hits}

        while select_board not in allowed_boards.keys():
            select_board = input(main_messages)

        header_row = [str(column + 1) for column in range(10)]
        header_row = ' ' +  '|'.join(header_row) + '|'
        rows_letters = [letter.upper() for letter in 'abcedfjhij']
        barrier = '-' * len(header_row)
        print(header_row, barrier, sep='\n')

        for row_number, board_row in enumerate(allowed_boards[select_board]):
            current_row = rows_letters[row_number] +'|' + '|'.join(board_row) + '|'
            print(current_row, barrier, sep='\n')

    def attack(self, next_player, clean_screen):
        print(f'{self.name}, elige posición para atacar.')

        messages = {'row': 'Fila: ', 'column': 'Columna: '}
        coordinates = self.get_positions(messages, is_attack=True)

        while coordinates is False:
            coordinates = self.get_positions(messages, is_attack=True)

        x_position, y_position = coordinates['column'], coordinates['row']
        all_ships_positions = next_player.get_all_ship_positions()
        attack_position = (x_position, y_position)

        if attack_position not in all_ships_positions:
            clean_screen()
            print('Haz impactado en el agua')
            self.hits[y_position][x_position] = 'x'
            next_player.board[y_position][x_position] = 'x'
            return None

        ship_selector = all_ships_positions.index((x_position, y_position)) // 3
        strike_ship = next_player.ships[ship_selector]
        clean_screen()
        print('Haz impactado uno de los navios del rival')

        self.hits[y_position][x_position] = 'o'
        next_player.board[y_position][x_position] = 'x'
        is_ship_sunk = strike_ship.hit()

        if is_ship_sunk:
            print(f'El {strike_ship.name} del enemigo ha sido hundido')
            next_player.ships.pop(ship_selector)

    def get_all_ship_positions(self):
        all_ships_positions = [position for ship in self.ships for position in ship.positions]
        return all_ships_positions

    def all_ships_sunk(self):
        current_shps_total = len(self.ships)

        if current_shps_total != 0:
            return False

        return True

class BattleshipGame:
    def __init__(self, player1:str, player2:str):
        self.player1 = Player(player1)
        self.player2 = Player(player2)

        self.play()

    def play(self):
        player1 = self.player1
        player2 = self.player2

        self.clean_screen()
        player1.place_ships(self.clean_screen)
        self.clean_screen()
        player2.place_ships(self.clean_screen)
        self.clean_screen()

        is_finish_game = self.turn_controler(player1, player2)

        while is_finish_game != True:
            player1, player2 = player2, player1
            self.clean_screen()
            is_finish_game = self.turn_controler(player1, player2)
            self.clean_screen()

        total_ships_player_1 = len(player1.ships)

        if total_ships_player_1 == 0:
            player1, player2 = player2, player1

        self.clean_screen()
        print(f'¡¡¡Felicidades jugador {player1.name} has eliminado la flota del rival!!!')

    def turn(self, current_player, next_player, strikes_per_turn:int= 1):
        if next_player.all_ships_sunk():
            return True

        main_messages = [
            f'Es el turno del jugador {current_player.name} tus acciones disponibles en el turno son:',
            '=',
            f'1. Atacar al enemigo (Tus ataques restantes son: {strikes_per_turn})',
            '2. Visualizar tus tableros',
            '3. Finalizar tu turno',
            '4. Limpia la pantalla',
            '5. Rendirse',
            '=',
            'Inserta tu accion: '
        ]
        main_messages[1] = main_messages[1] * len(main_messages[0])
        main_messages[-2] = main_messages[-2] * len(main_messages[0])
        main_messages = '\n'.join(main_messages)


        action = input(main_messages).strip()
        allowed_actions = {'1':'attack', '2':'screen', '3':'next turn', '4':'clear', '5':'surrender'}

        while action not in allowed_actions.keys():
            action = input(main_messages)

        action = allowed_actions[action]

        if action == allowed_actions['1'] and strikes_per_turn > 0:
            self.clean_screen()
            current_player.attack(next_player, self.clean_screen)
            strikes_per_turn -= 1
        elif action == allowed_actions['2']:
            self.clean_screen()
            current_player.print_board()
        elif action == allowed_actions['3']:
            return False
        elif action == allowed_actions['4']:
            self.clean_screen()
        elif action == allowed_actions['5']:
            current_player.ships.clear()
            return True

        screen_change = None

        while action == allowed_actions['2'] and screen_change != '':
            screen_change = input('Para volver al menu presiona enter: ')
            self.clean_screen()

        return (current_player, next_player, strikes_per_turn)

    def turn_controler(self, current_player, next_player):
        turn_result = self.turn(current_player,next_player)

        while type(turn_result) is tuple:
            current_player = turn_result[0]
            next_player =  turn_result[1]
            strikes_per_turn = turn_result[2]

            turn_result = self.turn(current_player, next_player, strikes_per_turn)

        return turn_result

    def clean_screen(self):
        import os
        os.system('clear')

# Iniciamos el juego
def solicitud_nombre_jugador(order_jugador:int):
    jugador = ''
    confirmar_jugador = False

    while confirmar_jugador != '':
        jugador = input(f'Insertar el nombre del jugador {order_jugador}: ')
        confirmar_jugador = input(f'El nombre escogido para el jugador {order_jugador} es {jugador} para confirmar dar enter, para cambiar insertar cualquier caracter: ').upper()

    return jugador

primer_jugador = solicitud_nombre_jugador(1)
segundo_jugador = solicitud_nombre_jugador(2)
BattleshipGame(primer_jugador, segundo_jugador)
