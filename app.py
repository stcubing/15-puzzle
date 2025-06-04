import random

empty = "  "
board = [[" 1"," 2"," 3"," 4"],
         [" 5"," 6"," 7"," 8"],
         [" 9","10","11","12"],
         ["13","14","15",empty]]

gap = [3,3]

def printBoard():
   flatBoard = ""
   for row in board:
      for col in row:
         flatBoard += str(col) + " "
      flatBoard += "\n"

   print(flatBoard)

def down(state="c"):
   global gap
   if gap[0] == 0:
      if state == "player":
         print("* cannot make move")
   else:
      board[gap[0]][gap[1]] = board[gap[0]-1][gap[1]]
      board[gap[0]-1][gap[1]] = empty
      gap = [gap[0]-1,gap[1]]
def up(state="c"):
   global gap
   if gap[0] == 3:
      if state == "player":
         print("* cannot make move")
   else:
      board[gap[0]][gap[1]] = board[gap[0]+1][gap[1]]
      board[gap[0]+1][gap[1]] = empty
      gap = [gap[0]+1,gap[1]]
def right(state="c"):
   global gap
   if gap[1] == 0:
      if state == "player":
         print("* cannot make move")
   else:
      board[gap[0]][gap[1]] = board[gap[0]][gap[1]-1]
      board[gap[0]][gap[1]-1] = empty
      gap = [gap[0],gap[1]-1]
def left(state="c"):
   global gap
   if gap[1] == 3:
      if state == "player":
         print("* cannot make move")
   else:
      board[gap[0]][gap[1]] = board[gap[0]][gap[1]+1]
      board[gap[0]][gap[1]+1] = empty
      gap = [gap[0],gap[1]+1]

def checkWin():
   winState = [[" 1"," 2"," 3"," 4"],
               [" 5"," 6"," 7"," 8"],
               [" 9","10","11","12"],
               ["13","14","15",empty]]
   
   if board == winState:
      return True
   else: 
      return False
   
def shuffle():
   # OLD SHUFFLE (leads to impossible parity cases)
   # # turn board into single array
   # lineBoard = []
   # for row in board:
   #    for col in row:
   #       lineBoard.append(str(col))
      
   # random.shuffle(lineBoard)

   # # get new location of gap
   # newGap = lineBoard.index(empty)
   # gap[0] = (newGap % 4)
   # gap[1] = (newGap // 4)

   # # turn back into 2d array
   # i = 0
   # for row in range(4):
   #    for col in range(4):
   #       board[col][row] = lineBoard[i]
   #       i += 1

   for i in range(1000):
      dir = random.randint(1,4)
      match dir:
         case 1:
            up()
         case 2:
            down()
         case 3:
            left()
         case 4:
            right()


if __name__=="__main__":

   shuffle()
   counter = 0

   print("welcome to 15 puzzle")
   inputType = int(input("> control using ULDR [1] or WASD [2]? "))
   match inputType:
      case 1:
         keys = ["U","L","D","R"]
         print(f"> controls set to {keys}")
      case 2:
         keys = ["W","A","S","D"]
         print(f"> controls set to {keys}")
      case _:
         keys = ["U","L","D","R"]
         print(f"> defaulting to {keys}")

   while not checkWin():
      printBoard()
      counter += 1
      move = input(f"> [{counter}] make a move {keys}: ").upper()

      if move == keys[0]:
         up("player")
      elif move == keys[1]:
         left("player")
      elif move == keys[2]:
         down("player")
      elif move == keys[3]:
         right("player")
      elif move == "EXIT":
         exit()
      else:
         print("* not a valid move")

      checkWin()
   
   printBoard()
   if counter <= 1:
      print(f"> you win!! took you {counter} move")
   else:
      print(f"> you win!! took you {counter} moves")

   

   