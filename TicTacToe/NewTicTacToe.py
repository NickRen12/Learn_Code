board = [["_" for i in range(3)] for j in range(3)]

def make_move(board, player, row, col):
  # check is space is available.
  while board[row][col] != "_":
    # stops turn from getting skipped
    print("Cannot play on a taken space. Try again.")
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
  
  board[row][col] = player
  

def check_winner(board):
  for row in range(3):
    if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "_":
      return board[row][0]

  for col in range(3):
    if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "_":
      return board[0][col]

  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
    return board[0][0]
  if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "_":
    return board[2][0]

  return None

def check_draw(board):
  for row in range(3):
    for col in range(3):
      if board[row][col] == "_":
        return False
  return True

def play_game():
  player = "X"
  winner = None
  draw = False

  while not winner and not draw:
    for row in board:
      print(" ".join(row))

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    
    #Check if range is valid
    if row < 0 or row > 2 or col < 0 or col > 2:
      print ("Number is not within the range. Please pick again")
      row = int(input("Enter row (0-2): "))
      col = int(input("Enter column (0-2): "))

    make_move(board, player, row, col)

    winner = check_winner(board)

    draw = check_draw(board)

    if player == "X":
      player = "O"
    else:
      player = "X"

  for row in board:
    print(" ".join(row))

  if winner:
    print(f"Player {winner} wins!")
  else:
    print("The game is a draw.")

play_game()