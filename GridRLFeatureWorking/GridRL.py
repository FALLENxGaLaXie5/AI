from MDP import ValueIteration, ValueIterationStep, PolicyExtraction, QExtraction, PrintDict
from GridMDP import GridMDP, orientations
import time
import random

gridworld = GridMDP([[0.0, 0.0, 0.0, 0.0],
                     [0.0, None, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0]], terminals=[((3, 2), 1, (1, 0)), ((3, 1), -1, (1, 0))])

# gridworld = GridMDP( [[0.0, 0.0, 0.0, 0.0, 0.0],
#                      [0.0, 0.0, 0.0, 0.0, 0.0],
#                      [0.0, 0.0, 0.0, 0.0, 0.0],
#                      [0.0, 0.0, 0.0, 0.0, 0.0]], terminals=[((4, 3),1,(1,0)), ((4, 2),-1,(1,0))] )

waiting = True


def onclick(event):
    global waiting, a
    waiting = not waiting
    if event.key == 'right':
        a = 0
    elif event.key == 'up':
        a = 1
    elif event.key == 'left':
        a = 2
    elif event.key == 'down':
        a = 3



def DrawPacman(s):
    circle = plt.Circle((s[0] * CSTEP + CSTEP / 4, s[1] * RSTEP + RSTEP / 8), radius=RSTEP / 16, ec='black',
                        fc='yellow', zorder=2)
    plt.gca().add_patch(circle)



def DrawGhost(s):
    circle = plt.Circle((s[0]*CSTEP+CSTEP/4, s[1]*RSTEP+RSTEP/8), radius=RSTEP/16, ec='black', fc='purple', zorder=2)
    plt.gca().add_patch(circle)


def ErasePacman(s):
    circle = plt.Circle((s[0] * CSTEP + CSTEP / 4, s[1] * RSTEP + RSTEP / 8), radius=RSTEP / 15.6, ec='white',
                        fc='white', zorder=2)
    plt.gca().add_patch(circle)


plt = gridworld.DrawGrid(gridworld)
plt.ion()
plt.gcf().canvas.draw()
plt.gcf().canvas.flush_events()

time.sleep(2)

plt.gcf().canvas.mpl_connect('key_press_event', onclick)

Qs = dict([(s, [0 for a in gridworld.actions(s)]) for s in gridworld.states])
gridworld.DrawQs(gridworld, Qs)


def checkAllZeros():
    for pp in range(4):
        if Qs[s][pp] != 0:
            return False
    return True

def checkAboveZero():
    for pp in range(4):
        if Qs[s][pp] > 0:
            return True
    return False



print(Qs[(0, 0)][1])

ROWS = gridworld.rows
COLS = gridworld.cols
RSTEP = 1 / ROWS
CSTEP = 1 / COLS

# P1 = {(0, 0): 1, (0, 1): 1, (0, 2): 0, (1, 2): 0, (2, 2): 0, (3, 2): 0, (1, 0): 2, (2, 0): 2, (2, 1): 1, (3, 0): 1,
#       (3, 1): 0}
# P2 = {(0, 0): 0, (0, 1): 3, (0, 2): 3, (1, 2): 2, (2, 2): 3, (3, 2): 0, (1, 0): 0, (2, 0): 1, (2, 1): 0, (3, 0): 2,
#       (3, 1): 0}
# P3 = {(0, 0): 1, (0, 1): 1, (0, 2): 0, (1, 2): 0, (2, 2): 2, (3, 2): 0, (1, 0): 2, (2, 0): 0, (2, 1): 3, (3, 0): 1,
#       (3, 1): 0}
# P4 = {(0, 0): 0, (0, 1): 3, (0, 2): 3, (1, 2): 2, (2, 2): 0, (3, 2): 0, (1, 0): 0, (2, 0): 2, (2, 1): 1, (3, 0): 2,
#       (3, 1): 0}

P1 = {(0,0):1, (0,1):1, (0,2):0, (1,2):0, (2,2):0, (3,2):0, (1,0):2, (2,0):1, (2,1):1, (3,0):2, (3,1):0}




P2 = {(0,0):  0, (0,1):1,   (0,2):0,    (1,2):0, (2,2):0, (3,2):0,      (1,0):2,    (2,0):1, (2,1):0, (3,0):2,
      (3,1):0}
P3 = {(0, 0): 0, (0, 1): 3, (0, 2): 3, (1, 2): 2, (2, 2): 0, (3, 2): 0, (1, 0): 0, (2, 0): 2, (2, 1): 3, (3, 0): 1,
      (3, 1): 0}
P4 = {(0, 0): 1, (0, 1): 1, (0, 2): 0, (1, 2): 0, (2, 2): 3, (3, 2): 0, (1, 0): 2, (2, 0): 2, (2, 1): 1, (3, 0): 2,
      (3, 1): 0}
P5 = {(0, 0): 0, (0, 1): 3, (0, 2): 3, (1, 2): 2, (2, 2): 2, (3, 2): 0, (1, 0): 0, (2, 0): 1, (2, 1): 1, (3, 0): 1,
      (3, 1): 0}

def isGood(state, action):
    if P2[state] == action and Qs[state][action] >= 0:
        return True
    if P3[state] == action and Qs[state][action] >= 0:
        return True
    if P4[state] == action and Qs[state][action] >= 0:
        return True
    if P5[state] == action and Qs[state][action] >= 0:
        return True
    return False

alpha = 0.5
i = 0
while i in range(2000):
    s = (0, 0)
    term = False
    DrawPacman(s)

    while not term:
        if waiting == True:  # False:
            waiting = True

            time.sleep(0.05)




            DrawGhost((1, 2))
            DrawGhost((3, 0))



            if checkAllZeros():
                print(s)
                print("This state is all zeros!")
                pol = random.randint(0, 3)

                # if random.random() <= 0.2:
                #     if random.random() <= 0.8:
                #         if random.random() <= 0.8:
                #             a = P1[s]
                #         elif random.random() <= 0.5:
                #             a = (P1[s] - 1) % len(orientations)
                #         else:
                #             a = (P1[s] + 1) % len(orientations)
                #     else:
                #         a = random.randint(0, 3)
                # else:
                #     if random.random() <= 0.8:
                #         a = P2[s]
                #     else:
                #         a = random.randint(0, 3)

                if pol == 0:
                    a = P2[s]
                elif pol == 1:
                    a = P3[s]
                elif pol == 2:
                    a = P4[s]
                elif pol == 3:
                    a = P5[s]
            elif checkAboveZero():
                print("Not all zeros!")
                ind = 0
                maxN = Qs[s][0]
                for i in range(1,4):
                    if Qs[s][i] > maxN:
                        maxN = Qs[s][i]
                        ind = i
                a = ind
            else:
                #for if there are some zeros and some negative, dont take negative route, take a random 0
                listerList = []
                for i in range(4):
                    if isGood(s, i):
                        listerList.append(i)
                if len(listerList) > 0:
                    ranIndex = random.randint(0, len(listerList) - 1)
                    a = listerList[ranIndex]
                else:
                    a = 0

                #good = False
                #while good == False:


                #ind = 0
                #for i in range(4):




            print(s)
            for i in range(4):
                print(Qs[s][i])
            #for i in Qs[s]:
            #    print(i)
            #print(Qs[s])
            # get next state by doing action
            sp = gridworld.go(s, orientations[a])

            if s == gridworld.terminals[0][0]:
                for a in range(4):
                    Qs[s][a] = alpha * Qs[s][a] + alpha * (1)
                gridworld.DrawQ(gridworld, s, a, Qs[s][a])
                term = True
            elif s == gridworld.terminals[1][0]:
                for a in range(4):
                    Qs[s][a] = alpha * Qs[s][a] + alpha * (-1)
                gridworld.DrawQ(gridworld, s, a, Qs[s][a])
                term = True
            elif sp == (1, 2) or s == (3, 0):
                # do QL update based on ghosts
                # Qs[s][a] = (1 - alpha) * Qs[s][a] + alpha * (gridworld.R(sp) + max(Qs[sp][a] for a in range(4)))
                # print(Qs[s][a])
                # gridworld.DrawQ(gridworld, s, a, Qs[s][a])
                # for a in range(4):
                #     Qs[s][a] = alpha * Qs[s][a] + alpha * (-0.25)
                # gridworld.DrawQ(gridworld, s, a, Qs[s][a])


                #This will deemphasize paths towards ghosts
                Qs[s][a] = Qs[s][a] - 0.25
                print(Qs[s][a])
                gridworld.DrawQ(gridworld, s, a, Qs[s][a])
            else:
                # do QL update
                Qs[s][a] = (1 - alpha) * Qs[s][a] + alpha * (gridworld.R(sp) + max(Qs[sp][a] for a in range(4)))
                print(Qs[s][a])
                gridworld.DrawQ(gridworld, s, a, Qs[s][a])

            # else:
            #     # do QL update
            #     Qs[s][a] = (1 - alpha) * Qs[s][a] + alpha * (gridworld.R(sp) + max(Qs[sp][a] for a in range(4)))
            #     print(Qs[s][a])
            #     gridworld.DrawQ(gridworld, s, a, Qs[s][a])

            ErasePacman(s)
            DrawPacman(sp)

            # update state
            s = sp

        plt.title('Episode: %d' % (i))
        plt.gcf().canvas.draw()
        plt.gcf().canvas.flush_events()
        plt.show()

    ErasePacman(s)
    i = i + 1