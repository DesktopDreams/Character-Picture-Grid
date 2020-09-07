#This is the CharacterPictureGrid project.
#The goal is to convert the following grid into
# .  . OO . OO .  . 
#  . OOOOOOO . 
#  . OOOOOOO . 
# .  . OOOOO .  . 
# .  .  . OOO .  .  . 
# .  .  .  . O .  .  .  .

#Coming up with the concept was pretty easy, but I had trouble getting my loop right.
#So I had to look up a bunch of stuff and pieced together the solution for loop.
#For incremental loop: https://stackoverflow.com/questions/50189469/how-to-increment-for-loop-index-when-used-with-range-in-python

grid = [[' . ', ' . ', ' . ', ' . ', ' . ', ' . '],
          [' . ', 'O', 'O', ' . ', ' . ', ' . '],
          ['O', 'O', 'O', 'O', ' . ', ' . '],
          ['O', 'O', 'O', 'O', 'O', ' . '],
          [' . ', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', ' . '],
          ['O', 'O', 'O', 'O', ' . ', ' . '],
          [' . ', 'O', 'O', ' . ', ' . ', ' . '],
          [' . ', ' . ', ' . ', ' . ', ' . ', ' . ']]

u = 0
while True:
    try:
        for i in range(0, len(grid)):
            print(grid[i][u], end='')
        print('') #This allows me print a new 'invisible line'
    except:
        pass #I wanted to run the code and see if there was any error, but
               #I found out that you cannot skip the except statement, unless
               #You use 'pass', refer https://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed
    if u == 6:
        break
    else:
        if u == u + 1 == 6:
            break
        else:
            u = u + 1
    continue
