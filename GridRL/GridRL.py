from MDP import ValueIteration, ValueIterationStep, PolicyExtraction, QExtraction, PrintDict
from GridMDP import GridMDP, orientations
import time
import random

gridworld = GridMDP([[0.0, 0.0, 0.0, 0.0],
                     [0.0, None, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0]], terminals=[((3, 2), 1, (1, 0)), ((3, 1), -1, (1, 0))])

# gridworld = GridMDP( [[0.0, 0.0, 0.0, 0.0, 0.0],
#                      [0.0, None,0.0, 0.0, 0,0],
#                      [0.0, 0.0, 0.0, None, 0,0],
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

print(Qs[(0, 0)][1])

ROWS = gridworld.rows
COLS = gridworld.cols
RSTEP = 1 / ROWS
CSTEP = 1 / COLS

P1 = {(0, 0): 1, (0, 1): 1, (0, 2): 0, (1, 2): 0, (2, 2): 0, (3, 2): 0, (1, 0): 2, (2, 0): 1, (2, 1): 1, (3, 0): 2,
      (3, 1): 0}
P2 = {(0, 0): 1, (0, 1): 1, (0, 2): 0, (1, 2): 0, (2, 2): 3, (3, 2): 0, (1, 0): 2, (2, 0): 1, (2, 1): 0, (3, 0): 2,
      (3, 1): 0}

alpha = 0.5
i = 0
while i in range(30):
    s = (0, 0)
    term = False
    DrawPacman(s)

    while not term:
        if waiting == True:  # False:
            waiting = True

            if random.random() <= 0.2:
                if random.random() <= 0.8:
                    if random.random() <= 0.8:
                        a = P1[s]
                    elif random.random() <= 0.5:
                        a = (P1[s] - 1) % len(orientations)
                    else:
                        a = (P1[s] + 1) % len(orientations)
                else:
                    a = random.randint(0, 3)
            else:
                if random.random() <= 0.8:
                    a = P2[s]
                else:
                    a = random.randint(0, 3)

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
            else:
                # do QL update
                Qs[s][a] = (1 - alpha) * Qs[s][a] + alpha * (gridworld.R(sp) + max(Qs[sp][a] for a in range(4)))
                gridworld.DrawQ(gridworld, s, a, Qs[s][a])

            ErasePacman(s)
            DrawPacman(sp)

            # update state
            s = sp

        plt.title('Episode: %d' % (i))
        plt.gcf().canvas.draw()
        plt.gcf().canvas.flush_events()
    ErasePacman(s)
    i = i + 1