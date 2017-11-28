from GridMDP_PM import GridMDP, orientations, turn_right, turn_left, NORTH, EAST, SOUTH, WEST
import time
import random
import numpy as np
import matplotlib.patches as patches
from copy import deepcopy
import math
#from playsound import playsound


gridworld = GridMDP( [[1.0, 1.0, 1.0, 1.0, 1.0],
                      [1.0, None,1.0, None, 1.0],
                      [0.0, 1.0, 1.0, 1.0, 1.0]], terminals=[((3, 2),1,(1,0)), ((3, 1),-1,(1,0))] )

gridworld = GridMDP( [[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                      [1.0, None,1.0, None, 1.0, None, 1.0, None, 1.0],
                      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                      [1.0, None,1.0, None, 1.0, None, 1.0, None, 1.0],
                      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                      [1.0, None, 1.0, None, 1.0, None, 1.0, None, 1.0],
                      [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]], terminals=[((4, 3),1,(1,0)), ((4, 2),-1,(1,0))] )


pacman_face = 0
pacman_mouth = 0

def DrawPacman(s, a):
    global pacman_face, pacman_mouth
    
    pacman_face = plt.Circle((s[0]*CSTEP+CSTEP/2, s[1]*RSTEP+RSTEP/2), radius=RSTEP/4, ec='black', fc='yellow', zorder=2)
    pacman_mouth = patches.Wedge((s[0]*CSTEP+CSTEP/2, s[1]*RSTEP+RSTEP/2), RSTEP/4, (a*90)-20.0, (a*90)+20.0, fc='black', zorder=2 )        
    plt.gca().add_patch(pacman_face)
    plt.gca().add_patch(pacman_mouth)
    
def ErasePacman(s):
    pacman_face.remove()
    pacman_mouth.remove()    

def DrawDot(s):
    dot_face = plt.Circle((s[0]*CSTEP+CSTEP/2, s[1]*RSTEP+RSTEP/2.0), radius=RSTEP/32, ec='white', fc='white', zorder=2)
    plt.gca().add_patch(dot_face)
    
def EraseDot(s):
    dot_face = plt.Circle((s[0]*CSTEP+CSTEP/2, s[1]*RSTEP+RSTEP/2), radius=RSTEP/4, ec='k', fc='k', zorder=2)
    plt.gca().add_patch(dot_face)

head = 0
left_eye = 0
right_eye = 0
rectangle = 0
def DrawGhost(s, a):
    global head, left_eye, right_eye, rectangle
    head = plt.Circle((s[0]*CSTEP+CSTEP/2, s[1]*RSTEP+RSTEP/2), radius=RSTEP/5, ec='black', fc='red', zorder=2)
    left_eye = plt.Circle((s[0]*CSTEP+CSTEP/2.7, s[1]*RSTEP+RSTEP/1.65), radius=RSTEP/16, lw = 28*CSTEP, ec='white', fc='black', zorder=2)
    right_eye = plt.Circle((s[0]*CSTEP+CSTEP/1.55, s[1]*RSTEP+RSTEP/1.65), radius=RSTEP/16, lw = 28*CSTEP, ec='white', fc='black', zorder=2)
    rectangle = plt.Rectangle((s[0]*CSTEP+CSTEP/4, s[1]*RSTEP+RSTEP/4), CSTEP/2, RSTEP/4, joinstyle = 'round', ec = 'red', fc='red', zorder=2)
    plt.gca().add_patch(head)
    plt.gca().add_patch(left_eye)
    plt.gca().add_patch(right_eye)
    plt.gca().add_patch(rectangle)
    
def EraseGhost(s, dotgrid):
    head.remove()
    left_eye.remove()
    right_eye.remove()
    rectangle.remove()
    if ( dotgrid[s[1]][s[0]] == 1.0 ):
        DrawDot(s)

def DrawDots():
    # draw all uneaten food dots
    rows=len(gridworld.grid)
    cols=len(gridworld.grid[0])
    dot_count = 0
    for x in range(cols):
        for y in range(rows):
            if gridworld.grid[y][x] == 1.0:
               DrawDot((x, y))
               dot_count = dot_count + 1
    return dot_count

def DrawGhosts(s, a):
    DrawGhost(s, a)

def EraseGhosts(s, dotgrid):
    EraseGhost(s, dotgrid)


def FoodDetection(s, dotgrid):
    input_state = s
    if ( dotgrid[s[1]][s[0]] == 1.0 ):
        return 1.0
       
    # check N
    action = None
    ncount = 1
    min_distance = math.inf
    sn = gridworld.go(input_state, orientations[NORTH])
    while ( sn != s ):
        s = sn
        ncount = ncount + 1
        if ( dotgrid[sn[1]][sn[0]] == 1.0 ):
            if (ncount < min_distance):
                min_distance = ncount
                action = NORTH
        else:
            sn = gridworld.go(s, orientations[NORTH])
        
    # check E
    ecount = 1
    sn = gridworld.go(input_state, orientations[EAST])
    while ( sn != s ):
        s = sn
        ecount = ecount + 1
        if ( dotgrid[sn[1]][sn[0]] == 1.0 ):
            if (ecount < min_distance):
                min_distance = ecount
                action = EAST
        else:
            sn = gridworld.go(s, orientations[EAST])
    
    # check S
    scount = 1
    sn = gridworld.go(input_state, orientations[SOUTH])
    while ( sn != s ):
        s = sn
        scount = scount + 1
        if ( dotgrid[sn[1]][sn[0]] == 1.0 ):
            if (scount < min_distance):
                min_distance = scount
                action = SOUTH
        else:
            sn = gridworld.go(s, orientations[SOUTH])
        
    # check W
    wcount = 1
    sn = gridworld.go(input_state, orientations[WEST])
    while ( sn != s ):
        s = sn
        wcount = wcount + 1
        if ( dotgrid[sn[1]][sn[0]] == 1.0 ):
            if (wcount < min_distance):
                min_distance = wcount
                action = WEST
        else:
            sn = gridworld.go(s, orientations[WEST])
    
    return 1.0/(min_distance*min_distance)

def GhostDetection(s,gs):
    if ( s == gs ):
        return 1.0
    range = 3
    ydiff = s[1]-gs[1]
    print("ydiff", ydiff)
    xdiff = s[0]-gs[0]
    print("xdiff", xdiff)
    if (xdiff == 0.0 and ydiff > 0.0 and ydiff < range):
        return 1.0/(ydiff)
    elif (xdiff == 0.0 and ydiff < 0.0 and ydiff > -range):
        return 1.0/(-ydiff)
    elif (xdiff > 0.0 and xdiff < range and ydiff == 0.0):
        return 1.0/(xdiff)
    elif (xdiff < 0.0 and xdiff > -range and ydiff == 0.0):
        return 1.0/(-xdiff)
    else:
        return 0.0   #1.0/(math.inf)
    


#=========================================================================
# EXPLORATION and EXPLOITATION
#=========================================================================
w1 = 0
w2 = 0

score = 0

ROWS = gridworld.rows
COLS = gridworld.cols
RSTEP = 1/ROWS
CSTEP = 1/COLS

#playsound('C:\\Users\\david.claveau\\Documents\\pacmanstart.wav')

# learning rate
alpha = 0.1

# initial weights
w1 = 0.0
w2 = 0.0

# list of weights per training episode
weights = []
weights.append((w1, w2))
score_list = []

# reward for current state
reward = 0 

i = 0
while i in range(10):    
    plt = gridworld.DrawGrid( gridworld )
    plt.gcf().canvas.draw()
    plt.gcf().canvas.flush_events()

    #time.sleep(1)    
    
    s = (0,0)   # pacman state
    gs = (2,2)  # ghost state
    term = False
    DrawPacman(s,0)
    dot_count = DrawDots()
    dotgrid = deepcopy(gridworld.grid) 
    DrawGhosts(gs,0) 
    score = 0
    
    while not term:
        if i >=4:
            time.sleep(0.0)
        reward = 0
        
        #---- pacman decides on his action
        if (w1 == w2 == 0.0) or i < 4:
            a = random.randint(0,3)
        else:
            QN = QE = QS = QW = -math.inf
            sN = gridworld.go(s, orientations[NORTH])
            if sN != s:
                df = FoodDetection(sN, dotgrid)
                dg = GhostDetection(sN, gs)
                if (df != 0.0) or (dg != 0.0):
                    QN = w1 * df + w2 * dg
                    print("QN= %f" % (QN))
            
            sE = gridworld.go(s, orientations[EAST])
            if sE != s:
                df = FoodDetection(sE, dotgrid)
                dg = GhostDetection(sE, gs)
                print(df, dg)
                if (df != 0.0) or (dg != 0.0):
                    QE = w1 * df + w2 * dg
                    print("QE= %f" % (QE))
            
            sS = gridworld.go(s, orientations[SOUTH])
            if sS != s:
                df = FoodDetection(sS, dotgrid)
                dg = GhostDetection(sS, gs)
                if (df != 0.0) or (dg != 0.0):
                    QS = w1 * df + w2 * dg
                    print("QS= %f" % (QS))
            
            sW = gridworld.go(s, orientations[WEST])
            if sW != s:
                df = FoodDetection(sW, dotgrid)
                dg = GhostDetection(sW, gs)
                if (df != 0.0) or (dg != 0.0):
                    QW = w1 * df + w2 * dg
                    print("QW= %f" % (QW))
            
            list = [QE, QN, QW, QS]
            print(list)
            lmax = max(list)
            if lmax > -math.inf:
                a = list.index(lmax)
            else:
                a = random.randint(0,3)

        
        #---- update and draw pacman
        ErasePacman(s)
        s = gridworld.go(s, orientations[a])
        EraseDot(s)
        DrawPacman(s,a)                            

           
        #---- check for food
        df = FoodDetection(s, dotgrid)
            
        #---- check for ghosts
        dg = GhostDetection(s, gs)

        #---- update dots
        if ( dotgrid[s[1]][s[0]] == 1.0 ):
            dotgrid[s[1]][s[0]] = 0.0
            dot_count = dot_count - 1
            score = score + 10
            reward = 100
                
        if ( dot_count == 0 ):        
            term = True                     
            
        #---- update and draw ghosts
        ga = random.randint(0,3)   # ghost action
        EraseGhosts(gs, dotgrid)
        gs = gridworld.go(gs, orientations[ga])
        DrawGhosts(gs,ga)                     
                             
        if ( gs == s ):        
            term = True
            reward = -500
        
        #---- use feature values to compute expected Q value
        Q = w1 * (df) + w2 * (dg)
        
        #---- update weights
        if ( not math.isnan(df) and not math.isnan(dg)):
            w1 = w1 + alpha * (reward - Q) * (df)
            w2 = w2 + alpha * (reward - Q) * (dg)            
                        
        csfont = {'fontname':'Comic Sans MS'}
        plt.suptitle('EPISODE: %d   SCORE: %d' % (i,score), color='white', fontsize=24, **csfont, fontweight='bold') 
        plt.title('w1 = %f   w2 = %f' % (w1,w2), color='white', fontsize=24, **csfont, fontweight='bold') 
        plt.gcf().canvas.draw()
        plt.gcf().canvas.flush_events()
        plt.show()
        if ( gs == s ):
            pass
            #playsound('C:\\Users\\david.claveau\\Documents\\pacman_death.wav')
        #else:
            #playsound('C:\\Users\\david.claveau\\Documents\\pacman_chomp.wav')

                        
    weights.append((w1, w2))
    score_list.append(score)
    plt.close()
    i = i + 1
    

plt = gridworld.DrawGrid( gridworld )
dot_count = DrawDots()
DrawPacman((0,0),0)

rectangle = plt.Rectangle((0.2, 0.1), 0.65, 0.85, joinstyle = 'round', ec = 'blue', fc='black', zorder=2)
plt.gca().add_patch(rectangle)

plt.text(0.35, 0.8, "w1       w2     score", backgroundcolor='black', color='white', fontsize=24, **csfont, fontweight='bold')

for i in range(1,len(weights)):
    plt.text(0.3, 0.8-(i+0.5)*0.05, "%f       %f       %d" % (weights[i-1][0],weights[i-1][1],score_list[i-1]), backgroundcolor='black', color='white', fontsize=14, **csfont, fontweight='bold')


plt.gcf().canvas.draw()
plt.gcf().canvas.flush_events()



time.sleep(10)    
plt.close()

