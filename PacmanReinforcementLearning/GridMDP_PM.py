import operator
from MDP import MDP
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import colorsys
from math import log


def if_(test, result, alternative):
    if test:
        if callable(result): return result()
        return result
    else:
        if callable(alternative): return alternative()
        return alternative
    
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

#======================================================================================
orientations = [(1,0), (0, 1), (-1, 0), (0, -1)]
def turn_right(orientation):
    return orientations[(orientations.index(orientation)-1) % len(orientations)]

def turn_left(orientation):
    return orientations[(orientations.index(orientation)+1) % len(orientations)]

# component-wise addition:  vector_add((0, 1), (8, 9))  ->  (8, 10)
def vector_add(a, b):
    return tuple(map(operator.add, a, b))


# 2-D grid MDP
# specify the grid as a list of lists of rewards; 
# use None for an obstacle (unreachable state).  
# specify the terminal states.
# an action is an (x, y) unit vector; e.g. (1, 0) means move east
class GridMDP(MDP):
    def __init__(self, grid, terminals, init=(0, 0), gamma=.9):
        MDP.__init__(self, init, actlist=orientations, terminals=terminals, gamma=gamma)
        grid.reverse() ## because we want row 0 on bottom, not on top
        self.grid=grid
        self.rows=len(grid)
        self.cols=len(grid[0])
        for x in range(self.cols):
            for y in range(self.rows):
                self.reward[x, y] = 0.0 #grid[y][x]  # each reward is from the grid
                if grid[y][x] is not None:
                    self.states.add((x, y))     # each state is a tuple of indices

    def T(self, state, action):
        if action == None:
            return [(0.0, state)]
        else:
            if (state == self.terminals[0][0] or state == self.terminals[1][0]):
                return [(1.0, (1,0))]
            else:
                return [(0.8, self.go(state, action)),
                        (0.1, self.go(state, turn_right(action))),
                        (0.1, self.go(state, turn_left(action)))]

    # return a numeric reward for this state.
    def R(self, state):
        return self.reward[state]

    # return the state that results from going in this direction
    def go(self, state, direction):
        state1 = vector_add(state, direction)
        return if_(state1 in self.states, state1, state)


    def DrawGrid( self, gridworld ):
        fig = plt.figure(figsize=(10,8))
        fig.patch.set_facecolor('black')        
        ax = plt.axes()

        #ax.set_facecolor('k')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.set_xlim(0.0,1.0)
        ax.set_ylim(0.0,1.0)
        
        #-- draw bold outer frame
        ax.spines['top'].set_linewidth(0)
        ax.spines['right'].set_linewidth(0)
        ax.spines['bottom'].set_linewidth(0)
        ax.spines['left'].set_linewidth(0)
        ax.spines['top'].set_color('blue')
        ax.spines['right'].set_color('blue')
        ax.spines['bottom'].set_color('blue')
        ax.spines['left'].set_color('blue')




        
        ROWS = gridworld.rows
        COLS = gridworld.cols
        RSTEP = 1/ROWS
        CSTEP = 1/COLS
        
        rectangle1 = plt.Rectangle((0.0, 0.0), self.cols*CSTEP, self.rows*RSTEP, joinstyle = 'round', lw = 2, ec = 'darkblue', fc='k', zorder=2)
        plt.gca().add_patch(rectangle1)                    
        rectangle2 = plt.Rectangle((0.01, 0.01), self.cols*CSTEP-0.02, self.rows*RSTEP-0.02, joinstyle = 'round', lw = 2, ec = 'darkblue', fill=False, zorder=2)
        plt.gca().add_patch(rectangle2)                    
        
        #-- draw obstacles
        for x in range(COLS):
            for y in range(ROWS):
                if gridworld.grid[y][x] is None:
                    rectangle = plt.Rectangle((x*CSTEP, y*RSTEP), CSTEP, RSTEP, joinstyle = 'round', lw = 2, ec = 'darkblue', fc='k', zorder=2)
                    plt.gca().add_patch(rectangle)  # bbox=dict(facecolor='none', edgecolor='black', boxstyle='round,pad=1'),                  
                    #rectangle = plt.Rectangle((x*CSTEP+0.01, y*RSTEP+0.01), CSTEP-0.02, RSTEP-0.02, joinstyle = 'round', lw = 2, ec = 'blue', fill=False, zorder=2)
                    #plt.gca().add_patch(rectangle)                    
        return plt
    


