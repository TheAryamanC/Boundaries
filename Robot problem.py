def list_of_moves(str_of_moves):
    list_of_moves = list(str_of_moves)
    return list_of_moves

#current d is a number from 0-3 for the index of the list showing which direction the robot is currently facing
def direction(move, current_d):
    if move == "L":
        current_d -= 1
    if move == "R":
        current_d += 1
    
    if current_d < 0:
        current_d = 3
    if current_d > 3:
        current_d = 0
    return current_d

def new_position(direction, x_pos, y_pos):
    if direction == 0:
        y_pos += 1
    if direction == 1:
        x_pos += 1
    if direction == 2:
        y_pos -= 1
    if direction == 3:
        x_pos -= 1
    return [x_pos, y_pos]

if __name__ == "__main__":
    moves = "RFLFRLFRLFL"

    list_moves = list_of_moves(moves)
    position = [0, 0]
    current_direction = 0
    for move in list_moves:
        if move == "R" or move == "L":
            current_direction = direction(move, current_direction)
        else:
            position = new_position(current_direction, position[0], position[1])
    
    print(position)