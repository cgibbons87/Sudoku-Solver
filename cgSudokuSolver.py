import pprint as pp

#example boards
#easy and quick...
board1 = [
  [0,0,0,7,9,0,0,5,0],
  [3,5,2,0,0,8,0,4,0],
  [0,0,0,0,0,0,0,8,0],
  [0,1,0,0,7,0,0,0,4],
  [6,0,0,3,0,1,0,0,8],
  [9,0,0,0,8,0,0,1,0],
  [0,2,0,0,0,0,0,0,0],
  [0,4,0,5,0,0,8,9,1],
  [0,8,0,0,3,7,0,0,0]
  ]
  
#...hard and slow
board2 = [
  [0,0,0,7,0,0,0,0,0],
  [1,0,0,0,0,0,0,0,0],
  [0,0,0,4,3,0,2,0,0],
  [0,0,0,0,0,0,0,0,6],
  [0,0,0,5,0,9,0,0,0],
  [0,0,0,0,0,0,4,1,8],
  [0,0,0,0,8,1,0,0,0],
  [0,0,2,0,0,0,0,5,0],
  [0,4,0,0,0,0,3,0,0]
  ]

def CheckValue(localboard, pos, k):
  #prepare a holder variable containing all values in the row, column, subgrid
  #then check to see if our proposed value is included in this set  

  holder = localboard[pos[0]][:]

  for i in [0,1,2,3,4,5,6,7,8]:
    holder.append(localboard[i][pos[1]])
    
  if pos[0] < 3 and pos[1] < 3:
    for i in [0,1,2]:
      for j in [0,1,2]:
        holder.append(localboard[i][j])
  elif 2 < pos[0] < 6 and pos[1] < 3:
    for i in [3,4,5]:
      for j in [0,1,2]:
        holder.append(localboard[i][j])
  elif pos[0] > 5 and pos[1] < 3:
    for i in [6,7,8]:
      for j in [0,1,2]:
        holder.append(localboard[i][j])   
    
  elif pos[0] < 3 and 2 < pos[1] < 6:
    for i in [0,1,2]:
      for j in [3,4,5]:
        holder.append(localboard[i][j])
  elif 2 < pos[0] < 6 and 2 < pos[1] < 6:
    for i in [3,4,5]:
      for j in [3,4,5]:
        holder.append(localboard[i][j])
  elif pos[0] > 5 and 2 < pos[1] < 6:
    for i in [6,7,8]:
      for j in [3,4,5]:
        holder.append(localboard[i][j])  
    
  elif pos[0] < 3 and pos[1] > 5:
    for i in [0,1,2]:
      for j in [6,7,8]:
        holder.append(localboard[i][j])
  elif 2 < pos[0] < 6 and pos[1] > 5:
    for i in [3,4,5]:
      for j in [6,7,8]:
        holder.append(localboard[i][j])
  elif pos[0] > 5 and pos[1] > 5:
    for i in [6,7,8]:
      for j in [6,7,8]:
        holder.append(localboard[i][j])  
  else:
    print("error")
      
  if k in holder:
    return False
  else:
    return True


#perform backtracking. Try 1-9, checking validity in accordance with the rules of sudoku, 
#backtracking when it becomes impossible to fill a square
def SSolver(localboard):
  pos = [-1,-1]
  for i in localboard:
    pos[0] = pos[0] + 1
    for j in localboard[pos[0]]:
      pos[1] = pos[1] + 1
      if j == 0:
        for k in range(1, 10):
          if CheckValue(localboard, pos, k):
            localboard[pos[0]][pos[1]] = k
            [newboard, x] = SSolver(localboard)
            if x is True:
              return [newboard, True]
            localboard[pos[0]][pos[1]] = 0
        return [localboard, False]
    pos[1] = -1
  return [localboard, True]

      
[solvedboard, x] = SSolver([x[:] for x in board1])
pp.pprint(solvedboard)

