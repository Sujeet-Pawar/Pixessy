def print_state(state):
    print(" ".join(map(str, state)))

def is_valid_move(state, i, j):
    """Check if the move between positions i and j is valid."""
    if state[i] == 0 and state[j] == 1 and state[i+1:j].count(0) == 0:
        return True
    if state[i] == 1 and state[j] == 0 and state[i:j-1].count(1) == 0:
        return True
    return False

def move_zero(state, pos):
    """Move a zero to the right."""
    if pos + 1 < len(state) and state[pos + 1] == 1:
        return state[:pos] + [1] + [0] + state[pos + 2:]
    return state

def move_one(state, pos):
    """Move a one to the left."""
    if pos - 1 >= 0 and state[pos - 1] == 0:
        return state[:pos - 1] + [1] + [0] + state[pos + 1:]
    return state

def jump_zero(state, pos):
    """Jump a zero over a single 1 if there is an underscore after it."""
    if pos + 2 < len(state) and state[pos + 1] == 1 and state[pos + 2] == 0:
        return state[:pos] + [1] + [0] + state[pos + 3:]
    return state

def jump_one(state, pos):
    """Jump a one over a single 0 if there is an underscore after it."""
    if pos - 2 >= 0 and state[pos - 1] == 0 and state[pos - 2] == 1:
        return state[:pos - 2] + [1] + [0] + state[pos + 1:]
    return state

def solve_puzzle(state):
    """Solve the puzzle based on the rules."""
    moves = []
    while state != [1, 1, 1, '_', 0, 0, 0]:
        print_state(state)
        # Find the position of the underscore
        underscore_pos = state.index('_')

        # Try to move zeros to the right or ones to the left
        if state[underscore_pos - 1] == 1:
            state = move_one(state, underscore_pos)
            moves.append("Move 1 left")
        elif state[underscore_pos + 1] == 0:
            state = move_zero(state, underscore_pos)
            moves.append("Move 0 right")
        # Check if a jump is possible
        elif state[underscore_pos + 1] == 1:
            state = jump_zero(state, underscore_pos)
            moves.append("Jump 0 over 1")
        elif state[underscore_pos - 1] == 0:
            state = jump_one(state, underscore_pos)
            moves.append("Jump 1 over 0")
        
    print_state(state)
    return moves

# Initial state
initial_state = [0, 0, 0, '_', 1, 1, 1]
moves = solve_puzzle(initial_state)

print("\nMoves taken:")
for move in moves:
    print(move)