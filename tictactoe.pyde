# GLOBAL VARIABLES
# grid
grid = [[0,0,0],[0,0,0],[0,0,0]]

# turn 1 -> X, 2 -> O
turn = 1

score_1 = 0
score_2 = 0

# mode
# begins on "instructionsScreen"
# 1 - game on
# 2 - game over
mode = "instructionsScreen"

ai = False # when True AI will play
turncount = 0

####################################################################
def reset_game():    
    global grid, turn, mode, ai
    # grid
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    
    # turn
    turn = 1
    
    # mode
    # 1 - game on
    # 2 - game over
    mode = 1
    
    ai = False # when True AI will play

def setup():
    size(800,600)

####################################################################
def draw():
    #background(90,120,190);
    global turn
    global score_1, score_2
    global mode
    global mode, grid, ai, turn, turncount
    
    instruction()

##################################   
    if mode == 1: # on
        background(30)
        
        draw_background()
        draw_gameboard()
        
        # check for winners
        winner, win_line = find_winners()
        if winner != 0:
            mode = 2
##################################   
    elif mode == 2: # off
        background(30)
        
        draw_background()
        draw_gameboard()
        
        # check for winners
        winner, win_line = find_winners()
        if winner != 0:
            draw_winner_line(win_line)
        
        if turn == 2: # p1 won on their last turn
            fill(255)
            stroke(255,0,0)
            rect(65,202,480,200)
            fill(50,150,50)
            textSize(42)
            text("Game over - X wins!", 100, 300)
            textSize(30)
            text("Click to play again",170,350)

        elif turn == 1: # p2 won on their last turn
            fill(255)
            stroke(0,0,255)
            rect(65,202,480,200)
            fill(50,150,50)
            textSize(42)
            text("Game over - O wins!", 100, 300)
            textSize(30)
            text("Click to play again", 170, 350)
        elif winner ==0:
            fill(255)
            stroke(0,0,255)
            rect(65,202,480,200)
            fill(50,150,50)
            textSize(42)
            text("Game over - It's a tie!", 100, 300)
            textSize(30)
            text("Click to play again", 170, 350)
####################################################################
def instruction():
    global mode, ai
    if mode == "instructionsScreen":
        background(0,50,150)
        textSize(50)
        fill(255)
        text("TIC-TAC-TOE", 240, 150)
        textSize(15)
        text("The objective of the game is to get three of your respective symbol",160,200) 
        text("in a row before your opponent. Players place Xs and Os on",160,225) 
        text("the grid until either opponent has three in a row or the grid is full.",160,250)
        text("Player 1 is X and always goes first.",160,295)
        text("Player 2 is O and always goes second.",160,320)
        textSize(20)
        fill(200,10,0)
        rect(150,370,150,50)
        rect(435,370,150,50)
        fill(255)
        text("1 PLAYER", 180, 400)
        text("2 PLAYERS",460, 400)
            
####################################################################
def mousePressed(): # put the bot here; check each row with for loop 
    global mode, grid, ai, turn, turncount
    global score_1, score_2
    println( [mouseX/200,mouseY/200] )
    print(grid)
    
    ##################################  
    if mode == 2:
        reset_game()
        
    elif mode == "instructionsScreen":
        # select number of players
        if (mouseX >= 180 and mouseX <= 300) and (mouseY >= 380 and mouseY <= 420):
            ai = True
            mode = 1
        elif (mouseX >= 430 and mouseX <= 590) and (mouseY >= 380 and mouseY <= 420):
            mode = 1

##################################   
    elif mode == 1: 
        # check if click is on gameboard
        if mouseX < 600:
            # int division by 200
            if grid[mouseY/200][mouseX/200] == 0:
                grid[mouseY/200][mouseX/200] = turn
                switch_turns()
                
                ############################
                # check for winner
                winner, win_line = find_winners()
                if winner != 0:
                    if winner == 1:
                        score_1 += 1
                    elif winner == 2:
                        score_2 += 1
                    mode = 2 # game over
##################################################################
# AI
    if ai and mode == 1: # ai is True
        if turn == 2:
            spot = AI()
            if spot != 0:
                grid[y][x] = 2
            else:
                if turncount <8: # prevent while loop from crashing
                    x = int(random(0,3))
                    y = int(random(0,3))
                    
                    while grid[y][x] != 0:
                        x = int(random(0,3))
                        y = int(random(0,3))
                    turncount += 1
                    grid[y][x] = 2
                    switch_turns()
                
    
            ############################
            # check for winner
            winner, win_line = find_winners()
            if winner != 0:
                if winner == 1:
                    score_1 += 1
                elif winner == 2:
                    score_2 += 1
                mode = 2 # game over
####################################################################
def find_winners():
    global grid, mode
    winner = "Tie"
    '''
    check for winners
    returns the player number 1 or 2 of the winner
    int 1 or 2
    and returns none if no winner
    '''
    # Rows
    for y in range(3):
        if grid[y][0] == grid[y][1]== grid[y][2] != 0:
            return (grid[y][0],y)
    # Columns
    for x in range(3):
        if grid[0][x] == grid[1][x]== grid[2][x] != 0:
            return (grid[0][x],3+x)
    
##################################
   # Diagonal 
    # L to R
    if grid[0][0] == grid [1][1] == grid [2][2] != 0:
        return (grid[0][0],6)
    # R to L
    elif grid[2][0] == grid[1][1] == grid[0][2] != 0:
        return (grid[2][0],7)
    
##################################
    # no wins
    
    return (0,None)

####################################################################
def draw_gameboard():
    global grid
    # draw gameboard based on list
    
    # loop through rows
    for y in range(3):
        # loop through columns
        for x in range(3):
        
            # check for 1-> X, 2-> O 
            if grid[y][x] == 2:
                strokeWeight(8)
                stroke(0,0,200)
                noFill()
                ellipse((x*200)+100,(y*200)+100,150,150)
            elif grid[y][x] == 1:
                strokeWeight(8)
                stroke(200,0,0)
                line((x*200)+200,(y*200)+200,(x*200),(y*200))
                line((x*200),(y*200)+200,(x*200)+200,(y*200))

####################################################################
def draw_background():
    # draw grid
    strokeWeight(4)
    stroke(255)
    rect(200,25,4,550)
    rect(400,25,4, 550)
    rect(25,200,550, 4)
    rect(25,400,550, 4)
    
    # draw scoreboard
    textSize(20)
    text("Player 1",670,200)
    text(score_1,670,230)
    text("Player 2",670,280)
    text(score_2,670,310)
####################################################################
def switch_turns(): # switches turns
    global turn, turncount
    # switch turns
    if turn == 1:
        turn = 2
        turncount += 1
    else:
        turn = 1
        turncount += 1
        
####################################################################        
def draw_winner_line(n): # draws line when someone wins
    # horizontal wins
    if n == 0:
        if turn == 2:
            stroke(200,0,0)
            line(0,100,600,100)
        elif turn == 1:
            stroke(0,0,200)
            line(0,100,600,100)
    elif n == 1:
        if turn == 2:
            stroke(200,0,0)
            line(0,300,600,300)
        elif turn == 1:
            stroke(0,0,200)
            line(0,300,600,300)
    elif n == 2:
        if turn == 2:
            stroke(200,0,0)
            line(0,500,600,500)
        elif turn == 1:
            stroke(0,0,200)
            line(0,500,600,500)
##################################   
    # vertical wins
    elif n == 3:
        if turn == 2:
            stroke(200,0,0)
            line(100,0,100,600)
        elif turn == 1:
            stroke(0,0,200)
            line(100,0,100,600)
    elif n == 4:
        if turn == 2:
            stroke(200,0,0)
            line(300,0,300,600)
        elif turn == 1:
            stroke(0,0,200)
            line(300,0,300,600)
    elif n == 5:
        if turn == 2:
            stroke(200,0,0)
            line(500,0,500,600)
        elif turn == 1:
            stroke(0,0,200)
            line(500,0,500,600)
##################################   
    # diagonals
    elif n == 6:
        if turn == 2:
            stroke(200,0,0)
            line(0,0,600,600)
        elif turn == 1:
            stroke(0,0,200)
            line(0,0,600,600)
    elif n == 7:
        if turn == 2:
            stroke(200,0,0)
            line(600,0,0,600)
        elif turn == 1:
            stroke(0,0,200)
            line(600,0,0,600)

def AI(): # check all and give back the smart one, if return none then go random
    if ai and mode == 1:
        # ROWS
        for y in range(3):
            if grid[y][1] == grid[y][2] == 1 and grid[y][0]==0 or grid[y][1] == grid[y][2] ==  2 and grid[y][0]==0:
                grid[y][0] == 2
                return grid[y][0]
            elif grid[y][2] == grid[y][0] == 1 and grid[y][1]==0 or grid[y][2] == grid[y][0] == 2 and grid[y][1]==0:
                grid[y][1] == 2
                return grid[y][1]
            elif grid[y][0] == grid[y][1] == 1 and grid[y][2]==0 or grid[y][0] == grid[y][1] == 2 and grid[y][2]==0:
                grid[y][2] == 2
                return grid[y][2]
        # COLUMNS
        for x in range(3):
            if grid[0][x] == grid[1][x] == 1 and grid[2][x]==0 or grid[0][x] == grid[1][x] == 2 and grid[2][x]==0:
                grid[2][x] == 2
                return grid[2][x]
            elif grid[1][x] == grid[2][x] == 1 and grid[0][x]==0 or grid[1][x] == grid[2][x] == 2 and grid[0][x]==0: 
                grid[0][x] == 2
                return grid[0][x]
            elif grid[2][x] == grid[2][x] == 1 and grid[1][x]==0 or grid[2][x] == grid[2][x] == 2 and grid[1][x]==0:
                grid[1][x] == 2
                return grid[1][x]
        # DIAGONALS
        # L to R
        if grid[0][0] == grid[1][1] == 1 and grid[2][2] == 0 or grid[0][0] == grid[1][1] == 2 and grid[2][2] == 0:
            grid[2][2] == 2
            return grid[2][2]
        elif grid[1][1] == grid[2][2] == 1 and grid[0][0] == 0 or grid[1][1] == grid[2][2] == 2 and grid[0][0] == 0:
            grid[0][0] == 2
            return grid[0][0]
        elif grid[2][2] == grid[0][0] == 1 and grid[1][1] == 0 or grid[2][2] == grid[0][0] == 2 and grid[1][1] == 0:
            grid[1][1] == 2
            return grid[1][1]
        # R to L
        if grid[2][0] == grid[1][1] == 1 and grid[0][2] == 0 or grid[2][0] == grid[1][1] == 2 and grid[0][2] == 0:
            grid[0][2] == 2
            return grid[0][2]
        elif grid[0][2] == grid[1][1] == 1 and grid[2][0] == 0 or grid[0][2] == grid[1][1] == 2 and grid[2][0] == 0:
            grid[2][0] == 2
            return grid[2][0]
        elif grid[2][0] == grid[0][2] == 1 and grid[1][1] == 0 or grid[2][0] == grid[0][2] == 2 and grid[1][1] == 0:
            grid[1][1] == 2
            return grid[1][1]
        
        else:
            return 0
            
    
