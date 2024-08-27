class Game():
  def __init__(self , turn = "X" , tie = False , winner = None  ):
    self.turn = turn
    self.tie = tie
    self.winner = winner
    self.board = {'a1': None, 'b1': None, 'c1': None,'a2': None, 'b2': None, 'c2': None,'a3': None, 'b3': None, 'c3': None,}

  def play_game(self):
    print("Shall we play ?")
    while self.winner == None and self.tie == False:
     self.print_board()
     self.get_move()
     self.check_winner()
     self.check_tie()
     self.switch_turns()

    self.render()

  def print_board(self):
    b = self.board
    print(f"""
          A   B   C
      1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
          ----------
      2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
          ----------
      3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
    """)
  def print_message(self):
    if self.tie:
      print("It's a tie!")
    elif self.winner:
      print(f"Player {self.winner} wins!")
    else:
      print(f"Player {self.turn}'s turn")
  
  def render(self):
    self.print_board()
    self.print_message()


  def get_move(self):
    
    while True:
      print(f'it is {self.turn} Turn')
      move = input('Enter your move: ').lower()
      if move in self.board and self.board[move] == None:
        self.board[move] = self.turn
        break
      else:
        print("Invalid move.")


  def check_winner(self):
    b = self.board
    if self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']) or self.board['a1'] and  (self.board['a1'] == self.board['a2'] == self.board['a3']) or self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']):
      self.winner = self.turn
    elif self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']) or self.board['b2'] and (self.board['b2'] == self.board['a2'] == self.board['c2']) or self.board['b2'] and (self.board['b2'] == self.board['a3'] == self.board['c1']):
      self.winner = self.turn
    elif self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']) or self.board['c3'] and (self.board['c3'] == self.board['b2'] == self.board['a3']):
      self.winner = self.turn


  def check_tie(self):
    if all(self.board.values()) and self.winner == None:
      self.tie = True


  def switch_turns(self):
    if self.turn =='X':
      self.turn = 'O'
    elif self.turn == 'O':
      self.turn = 'X'
 

    

game_instance = Game()
game_instance.play_game()