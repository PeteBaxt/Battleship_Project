#Author: Peter Baxter
#Date: 2/20/2022
#Github: PBaxt
#Description: Make Battleship, the classic blow-up-your-friends game


def make_board():
    """Creates a new board object"""
    board = [[" ", "1  ", "2  ", "3 ", "4  ", "5 ", "6  ", "7 ", "8  ", "9 ", "10 "], ["A", "\U0001F30A ", "\U0001F30A ",
    "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A "],
    ["B", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A "],
    ["C", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A "],
    ["D", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A "],
    ["E", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A "],
    ["F", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A "],
    ["G", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A "],
    ["H", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A "],
    ["I", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A "],
    ["J", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A ", "\U0001F30A "],]
    return board



class Boat:
    """Makes a new ship object, which Shipgame will use and alter and presumably blow up very thoroughly"""
    pass
#Boom emoji is "\U0001F4A5
#Disgruntled whale "\U0001F40B"
#Lobster "\U0001F99E"
#Fountain "\U000026F2"
#Hot springs "\U00002668"
#Boat "\U000026F4"

class ShipGame:
    """Battleship, but done in Python. Your cat would be very disappointed in not being able to scatter all those little
    red and white pins everywhere"""

    def __init__(self):
        """Initialize our values"""
        self._current_player = "first"
        self._current_state = "UNFINISHED"
        self._placement_phase = True
        self._first_ships = []
        self._second_ships = []
        self._player_1_visible_board = make_board()
        self._player_1_hidden_board = make_board()
        self._player_2_visible_board = make_board()
        self._player_2_hidden_board = make_board()
        self._coord_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
        self._coord_key_list = list(self._coord_dict.keys())

    def display_board(self, player, hidden_or_visible):
        """Display the current board state for a player. Valid inputs for player are first or second, if it is not that
        player's turn they cannot check their hidden board, which would reveal their ship positions to their opponent"""

        if player == 'first' and hidden_or_visible == 'hidden' and self._current_player == 'second':
            return False
        elif player == 'second' and hidden_or_visible == 'hidden' and self._current_player == 'first':
            return False

        if player == "first" and hidden_or_visible == "hidden":
            for i in range(len(self._player_1_hidden_board)):
                print(' '.join(map(str, self._player_1_hidden_board[i])))
        elif player == "second" and hidden_or_visible == "hidden":
            for i in range(len(self._player_2_hidden_board)):
                print(' '.join(map(str, self._player_2_hidden_board[i])))
        elif player == "first" and hidden_or_visible == "visible":
            for i in range(len(self._player_1_visible_board)):
                print(' '.join(map(str, self._player_1_visible_board[i])))
        elif player == "second" and hidden_or_visible == "visible":
            for i in range(len(self._player_2_visible_board)):
                print(' '.join(map(str, self._player_2_visible_board[i])))
        else:
            print("Please enter a valid combination of player and board. Valid states are 'first' and 'second' for player, 'hidden' or 'visible' for board")

    def get_current_state(self):
        """Returns the current state of the game, as either unfinished or with a player's victory"""
        return self._current_state

    def get_num_ships_remaining(self, player):
        """Takes as parameter a given player, either 'first' or 'second', and returns how many of their ships are still
        in play"""
        if player == "first":
            return len(self._first_ships)
        elif player == "second":
            return len(self._second_ships)
        else:
            print("No valid players entered. Please state either first or second, in all lowercase, and check spelling")

    def place_ship(self, player, length, first_coord, orientation):
        """
        Takes as parameters the player, which can be 'first' or 'second', length of the ship, the coordinate closest to
        A1, and the orientation, which can be 'R' if the ship is going to be horizontal (occupying a Row) or 'C' if the
        ship is going to be vertical (occupying a Column). Resulting ships are added to the corresponding player's list
        of boats, as well as placed on their respective hidden boards. Visible boards (as the top boards in the classic
        folding setup) do not have boats added to them, and will be changed only with the torpedo function. If the boat
        being added would go off the edge of the board or overlap with an already existing ship, this function will
        return False, otherwise it will return True
        """
        if self._placement_phase == False: #Make sure no boards are placed after torpedoes are launched
            return False

        if self._coord_dict[first_coord[0]] + length > 11 and orientation == 'C':
            return False
        elif int(first_coord[1:]) + length > 11 and orientation == 'R':
            return False

        proposed_ship_coords = [] #Generates a list of ship coordinates, which we can check against existing boats

        if orientation == 'C':
            start_str_coord = self._coord_dict[first_coord[0]]
            for coord_c in range(length):
                str_coord_index = start_str_coord + coord_c - 1 #-1 is added to compensate for indexing difference
                str_coord_value = self._coord_key_list[str_coord_index]
                coord_string_c = str(str_coord_value + first_coord[1:])
                proposed_ship_coords.append(coord_string_c)
        if orientation == 'R':
            for coord_r in range(length):
                coord_int_r = str(int(first_coord[1:])+coord_r)
                coord_string_r = str(first_coord[0] +  coord_int_r)
                proposed_ship_coords.append(coord_string_r)

        #Check for overlap with preexisting ships and append to player's list of current ships
        if player == 'first':
            for ship_coord in proposed_ship_coords:
                res = any(ship_coord in ship for ship in self._first_ships)
                if res == True:
                    return False
            self._first_ships.append(proposed_ship_coords)
        elif player == 'second':
            for ship_coord in proposed_ship_coords:
                res = any(ship_coord in ship for ship in self._second_ships)
                if res == True:
                    return False
            self._second_ships.append(proposed_ship_coords)
        else:
            print("No valid players entered. Please state either first or second, in all lowercase, and check spelling")

        #Replace wave emoji with boats on the correct player's hidden board
        if player == 'first':
            for coord in range(len(proposed_ship_coords)):
                str_part = proposed_ship_coords[coord][0]
                int_part = int(proposed_ship_coords[coord][1:])
                conv_str = self._coord_dict[str_part]
                self._player_1_hidden_board[conv_str][int_part] = "\U000026F4 "
            return True
        elif player == 'second':
            for coord in range(len(proposed_ship_coords)):
                str_part = proposed_ship_coords[coord][0]
                int_part = proposed_ship_coords[coord][1:]
                conv_str = self._coord_dict[str_part]
                self._player_2_hidden_board[int(conv_str)][int(int_part)] = "\U000026F4 "
            return True

    def fire_torpedo(self, player, target_coordinates):
        """Fires a torpedo, taking player and target coordinates and returning either False if player designation is
        incorrect or game already won, or True otherwise and update the ship list, the turn counter, the win condition,
        and the boards. Fire_torpedo can target the same coordinates multiple times; this is legal, if futile. Once the
        first player fires a torpedo, ships can no longer be placed. Valid player inputs are 'first' or 'second', while
        target_coordinates can be any coordinate on the board with format 'XN' format, where X is the letter row and
        N the integer column"""
        self._placement_phase = False
        if player != self._current_player:
            return False
        elif self._current_state != "UNFINISHED":
            return False
        if target_coordinates[0] not in self._coord_dict:
            return False
        elif int(target_coordinates[1:]) > 10:
            return False
        str_coord, int_coord = int(self._coord_dict[target_coordinates[0]]), int(target_coordinates[1:])
        #check for hits
        hit_check = False
        if player == 'first':
            hit_check = any(target_coordinates in ship for ship in self._second_ships)
            if hit_check == True:
                for ship in self._second_ships:
                    ship.remove(target_coordinates)
                    self._player_2_hidden_board[str_coord][int_coord] = "\U0001F4A5 "
                    self._player_2_visible_board[str_coord][int_coord] = "\U0001F4A5 "
                    self._second_ships = [boat for boat in self._second_ships if boat]#list comprehension clearing the falsy lists
                    if self.get_num_ships_remaining('second') == 0:
                        self._current_state = 'FIRST_WON'
                        return True
        elif player == 'second':
            hit_check = any(target_coordinates in ship for ship in self._first_ships)
            if hit_check == True:
                for ship in self._first_ships:
                    ship.remove(target_coordinates)
                    self._player_1_hidden_board[str_coord][int_coord] = "\U0001F4A5 "
                    self._player_1_visible_board[str_coord][int_coord] = "\U0001F4A5 "
                    self._first_ships = [boat for boat in self._first_ships if boat]#list comprehension clearing the falsy lists []
                    if self.get_num_ships_remaining('first') == 0:
                        self._current_state = 'SECOND_WON'
                        return True

        if hit_check == False:
            if player == 'first':
                self._player_2_hidden_board[str_coord][int_coord] = "\U0001F99E"
                self._player_2_visible_board[str_coord][int_coord] = "\U0001F99E"
            elif player == 'second':
                self._player_1_hidden_board[str_coord][int_coord] = "\U00002668 "
                self._player_1_visible_board[str_coord][int_coord] = "\U00002668 "

        if player == 'first':
            self._current_player = 'second'
        elif player == 'second':
            self._current_player = 'first'


        """
        Approach: Start with ensuring the torpedo is being fired in the correct order. Once it is, reuse code from the 
        place_ship approach to update both hidden and visible boards (displayed visible boards will include both hits,
        represented by an explosion emoji, and misses, represented by peevish sea life or water geysers. In doing so, 
        check and update the ship lists, removing the target coordinates from a given ship on a hit. Then clean up the 
        ship lists, checking to see if any ships are the null set and deleting them from the ship list. Finally, it will 
        update the current player and call get_num_ships_remaining; if either player has no ships, it should update the 
        victory condition and return true. 
        """
        return True

#Testing area
"""
beep = ShipGame()
beep.place_ship('second', 5, 'D10', 'C')
beep.place_ship('first', 2, 'C8', 'R')
beep.fire_torpedo('first', 'C8')
beep.display_board('first', 'hidden')
beep.fire_torpedo('second', 'C8')
print(beep.fire_torpedo('first', 'C8'))
beep.fire_torpedo('second', 'C9')
print(beep.get_num_ships_remaining('second'))
print(beep.get_current_state())
print(beep.fire_torpedo('first', 'C9'))
print(beep.get_num_ships_remaining('first'))
"""
