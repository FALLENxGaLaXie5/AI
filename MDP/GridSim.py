from MDP import ValueIteration, ValueIterationStep, PolicyExtraction, QExtraction, PrintDict
from GridMDP import GridMDP
import time

gridworld = GridMDP([[0.0, 0.0, 0.0, 0.0],
                     [0.0, None, 0.0, 0.0],
                     [0.0, 0.0, 0.0, 0.0]], terminals=[((3, 2), 1, (1, 0)), ((3, 1), -1, (1, 0))])

#gridworld = GridMDP( [[0.0, 0.0, 0.0, 0.0, 0.0],
#                      [0.0, None,0.0, 0.0, 0,0],
#                      [0.0, 0.0, 0.0, None, 0,0],
#                      [0.0, 0.0, 0.0, 0.0, 0.0]], terminals=[((4, 3),1,(1,0)), ((4, 2),-1,(1,0))] )

# V = ValueIteration(gridworld, epsilon=0.001)
# pi = PolicyExtraction( gridworld, V )
# Qs = QExtraction( gridworld, V )
# PrintDict(V)
# PrintDict(pi)
# PrintDict(Qs)
# gridworld.DrawVs( gridworld, V )
# gridworld.DrawQs( gridworld, Qs )
# gridworld.DrawArrows( gridworld, pi )


waiting = False


def onclick(event):
    global waiting
    waiting = not waiting
    print("click")
    print(waiting)


plt = gridworld.DrawGrid(gridworld)
plt.ion()
plt.gcf().canvas.draw()
plt.gcf().canvas.flush_events()

time.sleep(2)

plt.gcf().canvas.mpl_connect('button_press_event', onclick)

V = dict([(s, 0) for s in gridworld.states])

i = 0
while i in range(0, 30):
    if waiting == False:
        waiting = True
        V = ValueIterationStep(gridworld, V)
        pi = PolicyExtraction(gridworld, V)
        Qs = QExtraction(gridworld, V)
        gridworld.DrawQs(gridworld, Qs)
        gridworld.DrawArrows(gridworld, pi)
        gridworld.DrawVs(gridworld, V)

        plt.title('Step: %d' % (i))
        plt.gcf().canvas.draw()
        plt.gcf().canvas.flush_events()
        i = i + 1
    plt.pause(0.1)


