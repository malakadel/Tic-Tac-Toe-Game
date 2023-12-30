class player:

  def __init(self):
    self.name = ""
    self.symbol = ""

  def choose_name(self):
    while True:
      name = input("Enter your name (letters only): ")
      if name.isalpha():
        self.name = name
        break
      else: print("Please enter a valid name")

  def choose_symbol(self):
    while True:
      symbol = input("Choose a symbol (letters only): ")
      if symbol.isalpha() and len(symbol) == 1:
        self.symbol = symbol.upper()
        break
      else :print("Please enter a valid symbol")


class menu:

  def display_start_menu(self):
    welcome_msg = """
      Welcome to Tic Tac Toe!
      Please choose an option:
      1. Start Game
      2. Exit Game
      """
    choice = input(welcome_msg)
    if choice == "1" or choice == "2":
      return choice
    else:
      print("Please enter a valid option")
      self.display_start_menu()

    return choice

  def display_end_menu(self):
    welcome_msg = """
      Game Over!
      Please choose an option:
      1. Restart Game
      2. Exit Game
      """
    choice = input(welcome_msg)
    return choice


class board:

  def __init__(self):
    self.board = [str(i) for i in range(1, 10)]

  def display_board(self):
    for i in range(0, 9, 3):
      print("|".join(self.board[i:i + 3]))
      if i < 6:
        print("-----")

  def update_board(self, position, symbol):
    if self.is_valid_move(position):
      self.board[position - 1] = symbol
      return True
    return False

  def is_valid_move(self, position):
    return self.board[position - 1].isdigit()

  def reset_board(self):
    self.board = [str(i) for i in range(1, 10)]


class Game:

  def __init__(self):
    self.player = [player(), player()]
    self.board = board()
    self.menu = menu()
    self.current_player_index = 0

  def start_game(self):
    choice = self.menu.display_start_menu()
    if choice == "1":
      self.setup_players()
      self.play_game()
    else:
      self.quit_game()

  def setup_players(self):
    for number, player in enumerate(self.player, start=1):
      print(f"Player {number} , enter your detalis:")
      player.choose_name()
      player.choose_symbol()
      print('-' * 20)

  def play_game(self):
    while True:
      self.play_turn()
      if self.check_win() or self.check_draw():
        if self.check_draw():
          print("It's a draw!")
          self.board.display_board()
        elif self.check_win():
            self.switch_player()
            print(f"{self.player[self.current_player_index].name} wins!")
            self.board.display_board()
        choice = self.menu.display_end_menu()
        if choice == "1":
          self.restart_game()
        else:
          self.quit_game()
          break

  def play_turn(self):
    player = self.player[self.current_player_index]
    self.board.display_board()
    print(f"{player.name}'s turn({player.symbol}):")
    while True:
      try:
        position = int(input("Choose a position between 1-9: "))
        if 1 <= position <= 9 and self.board.update_board(
            position, player.symbol):
          break
        else:
          print("Please enter a valid position")
      except ValueError:
        print("Please enter a valid position between 1-9")

    self.switch_player()

  def switch_player(self):
    self.current_player_index = 1 - self.current_player_index

  def check_win(self):
    win_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  #rows
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  #columns
        [0, 4, 8],
        [2, 4, 6]  #diagonals
    ]
    for combination in win_combinations:
      if self.board.board[combination[0]] == self.board.board[
          combination[1]] == self.board.board[combination[2]]:
        return True
    return False

  def check_draw(self):
    all(not cell.isdigit() for cell in self.board.board)

  def restart_game(self):
    self.board.reset_board()
    self.current_player_index = 0
    self.play_game()

  def quit_game(self):
    print("Thanks for playing!")


if __name__ == "__main__":
  game = Game()
  game.start_game()
