from levelup.controller import GameController

class StartGameLibrary:
    ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

    def initialize_controller(self):
        self.controller = GameController()

    def provided_character_with_name(self, charactername):
        self.controller.create_character(charactername)

    def character_name_should_be(self, expected):
        if self.controller.status.character_name != expected:
            raise AssertionError(
                f"{self.controller.status.character_name} != {expected}"
            )

    def number_of_map_positions_should_be(self, expected):
         global current_y_position, current_x_position, total_move_count
            total_move_count = total_move_count + 1

    def starting_X_coordinate_should_be(self, expected):
        if action_choice == "W":
            new_x_position = current_x_position - 1
        if new_x_position >= 0 and new_x_position <= 9:
            current_x_position =  new_x_position

        if action_choice == "E":
            new_x_position = current_x_position + 1
        if new_x_position >= 0 and new_x_position <= 9:
            current_x_position = new_x_position


    def starting_Y_coordinate_should_be(self, expected):
         if action_choice == "N":
            new_y_position = current_y_position + 1
        if new_y_position >= 0 and new_y_position <= 9:
            current_y_position = new_y_position

        if action_choice == "S":
            new_y_position = current_y_position - 1
        if new_y_position >= 0 and new_y_position <= 9:
            current_y_position = new_y_position

    def starting_move_count_should_be(self, expected):
         global current_y_position, current_x_position, total_move_count
            total_move_count = total_move_count + 1
