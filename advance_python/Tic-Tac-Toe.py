board = [[" " for _ in range(3)] for _ in range(3)]

def display_board():
    for row in board:
        print("|".join(row))
        if row != board[-1]:
            print("---------")
            
def check_won(symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    for col in range(3):
        if all(row[col] == symbol for row in board):
            return True
        
    if all(board[i][i] == symbol for i in range(3)) or \
         all(board[i][2 - i] == symbol for i in range(3)):    
        return True
    return False

current_player = "X"
turns = 0

while turns < 9:
    display_board()
    move = input(f"Player {current_player}, enter your move (row and column): ").split(',')
    
    if len(move) != 2:
        print("invalid input")
        continue
    
    row, col = map(int, move)
    
    if row < 1 or row > 3 or col < 1 or col > 3:
        print("invalid position")
        continue
    
    if board[row - 1][col - 1] != " ":
        print("cell already occupied")
        continue
    
    board[row - 1][col - 1] = current_player
    turns += 1
    
    if check_won(current_player):
        display_board()
        print(f"Player {current_player} wins!")
        break
    
    current_player = "X" if current_player == "O" else "O"
else:
    display_board()
    print("It's a draw!")    