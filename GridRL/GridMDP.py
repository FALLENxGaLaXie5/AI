import operator
from MDP import MDP
import numpy as np
import matplotlib.pyplot as plt
import colorsys
from math import log


def if_(test, result, alternative):
    if test:
        if callable(result): return result()
        return result
    else:
        if callable(alternative): return alternative()
        return alternative


# ======================================================================================
orientations = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def turn_right(orientation):
    return orientations[(orientations.index(orientation) - 1) % len(orientations)]


def turn_left(orientation):
    return orientations[(orientations.index(orientation) + 1) % len(orientations)]


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
        grid.reverse()  ## because we want row 0 on bottom, not on top
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        for x in range(self.cols):
            for y in range(self.rows):
                self.reward[x, y] = grid[y][x]  # each reward is from the grid
                if grid[y][x] is not None:
                    self.states.add((x, y))  # each state is a tuple of indices

    def T(self, state, action):
        if action == None:
            return [(0.0, state)]
        else:
            if (state == self.terminals[0][0] or state == self.terminals[1][0]):
                return [(1.0, (1, 0))]
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

    def DrawGrid(self, gridworld):
        plt.figure(figsize=(10, 8))
        ax = plt.axes()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.set_xlim(0.0, 1.0)
        ax.set_ylim(0.0, 1.0)

        # -- draw bold outer frame
        ax.spines['top'].set_linewidth(5)
        ax.spines['right'].set_linewidth(5)
        ax.spines['bottom'].set_linewidth(5)
        ax.spines['left'].set_linewidth(5)

        ROWS = gridworld.rows
        COLS = gridworld.cols
        RSTEP = 1 / ROWS
        CSTEP = 1 / COLS

        # -- draw columns
        col_range = np.arange(1 / COLS, 0.99, 1 / COLS)
        print(col_range)
        for x in col_range:
            plt.plot([x, x], [0.0, 1.0], color='k', linestyle='-', linewidth=2)

        # -- draw rows
        row_range = np.arange(1 / ROWS, 0.99, 1 / ROWS)
        print(row_range)
        for y in row_range:
            plt.plot([0.0, 1.0], [y, y], color='k', linestyle='-', linewidth=2)

        # -- draw crosses
        for x in range(COLS):
            for y in range(ROWS):
                if (x, y) != gridworld.terminals[0][0] and (x, y) != gridworld.terminals[1][0]:
                    plt.plot([x * CSTEP, (x + 1) * CSTEP], [y * RSTEP, (y + 1) * RSTEP], zorder=1, color='k',
                             linestyle='-', linewidth=0.5)
                    plt.plot([(x + 1) * CSTEP, (x) * CSTEP], [(y) * RSTEP, (y + 1) * RSTEP], zorder=1, color='k',
                             linestyle='-', linewidth=0.5)

        # -- draw obstacles
        for x in range(COLS):
            for y in range(ROWS):
                if gridworld.grid[y][x] is None:
                    rectangle = plt.Rectangle((x * CSTEP, y * RSTEP), CSTEP, RSTEP, fc='grey', zorder=2)
                    plt.gca().add_patch(rectangle)
        return plt

    def DrawVs(self, gridworld, V):
        ROWS = gridworld.rows
        COLS = gridworld.cols
        RSTEP = 1 / ROWS
        CSTEP = 1 / COLS
        # -- print Vs
        for k, v in V.items():
            x = k[0] * CSTEP
            y = k[1] * RSTEP
            # -- Vs
            vfontsize = 8 / log(ROWS, 10)
            if v > 0:
                fcolor = colorsys.hsv_to_rgb(0.55, v, 1.0)
            else:
                fcolor = colorsys.hsv_to_rgb(1.0, abs(v), 1.0)

            t = plt.text(x + CSTEP / 2 - CSTEP / 8, y + RSTEP / 2 - 0 * RSTEP / 16, '%2.2f' % (v),
                         fontname='Comic Sans MS', fontsize=vfontsize)
            t.set_bbox(dict(facecolor=fcolor, alpha=0.9, edgecolor='white'))

    def DrawQs(self, gridworld, Qs):
        ROWS = gridworld.rows
        COLS = gridworld.cols
        RSTEP = 1 / ROWS
        CSTEP = 1 / COLS
        # -- print Qs
        for k, v in Qs.items():
            x = k[0] * CSTEP
            y = k[1] * RSTEP
            d = RSTEP / 3.5
            qfontsize = 6 / log(ROWS, 10)

            if k == gridworld.terminals[0][0] or k == gridworld.terminals[1][0]:
                t = plt.text(x + CSTEP / 2 - CSTEP / 8, y + RSTEP / 2 - 0 * RSTEP / 16, '%2.2f' % (v[0]),
                             fontname='Comic Sans MS', fontsize=qfontsize)
                t.set_bbox(dict(facecolor='white', alpha=0.9, edgecolor='white'))
            else:
                # left
                t = plt.text(x + (CSTEP / 2 - d), y + RSTEP / 2, '%2.2f' % (v[2]), color='grey',
                             fontname='Comic Sans MS', fontsize=qfontsize)
                t.set_bbox(dict(facecolor='white', alpha=0.9, edgecolor='white'))
                # right
                t = plt.text(x + (CSTEP / 2 + d / 2), y + RSTEP / 2, '%2.2f' % (v[0]), color='grey',
                             fontname='Comic Sans MS', fontsize=qfontsize)
                t.set_bbox(dict(facecolor='white', alpha=0.9, edgecolor='white'))
                # bottom
                t = plt.text(x + (CSTEP / 2 - 0.1 * CSTEP), y + (RSTEP / 2 - d / 2), '%2.2f' % (v[3]), color='grey',
                             fontname='Comic Sans MS', fontsize=qfontsize)
                t.set_bbox(dict(facecolor='white', alpha=0.9, edgecolor='white'))
                # top
                t = plt.text(x + (CSTEP / 2 - 0.1 * CSTEP), y + (RSTEP / 2 + d / 2), '%2.2f' % (v[1]), color='grey',
                             fontname='Comic Sans MS', fontsize=qfontsize)
                t.set_bbox(dict(facecolor='white', alpha=0.9, edgecolor='white'))

    def DrawQ(self, gridworld, s, a, Q):
        ROWS = gridworld.rows
        COLS = gridworld.cols
        RSTEP = 1 / ROWS
        CSTEP = 1 / COLS
        # -- print Q
        x = s[0] * CSTEP
        y = s[1] * RSTEP
        d = RSTEP / 3.5
        qfontsize = 6 / log(ROWS, 10)

        if s == gridworld.terminals[0][0] or s == gridworld.terminals[1][0]:
            t = plt.text(x + CSTEP / 2 - CSTEP / 8, y + RSTEP / 2 - 0 * RSTEP / 16, '%2.2f' % (Q),
                         fontname='Comic Sans MS', fontsize=qfontsize)
            t.set_bbox(dict(facecolor='white', alpha=0.9, edgecolor='white'))
            return

        if a == 0:
            # right
            t = plt.text(x + (CSTEP / 2 + d / 2), y + RSTEP / 2, '%2.2f' % (Q), color='grey', fontname='Comic Sans MS',
                         fontsize=qfontsize)
            t.set_bbox(dict(facecolor='white', alpha=0.9, edgecolor='white'))
        elif a == 1:
            # top
            t = plt.text(x + (CSTEP / 2 - 0.1 * CSTEP), y + (RSTEP / 2 + d / 2), '%2.2f' % (Q), color='grey',
                         fontname='Comic Sans MS', fontsize=qfontsize)
            t.set_bbox(dict(facecolor='white', alpha=0.9, edgecolor='white'))
        elif a == 2:
            # left
            t = plt.text(x + (CSTEP / 2 - d), y + RSTEP / 2, '%2.2f' % (Q), color='grey', fontname='Comic Sans MS',
                         fontsize=qfontsize)
            t.set_bbox(dict(facecolor='white', alpha=0.9, edgecolor='white'))
        elif a == 3:
            # bottom
            t = plt.text(x + (CSTEP / 2 - 0.1 * CSTEP), y + (RSTEP / 2 - d / 2), '%2.2f' % (Q), color='grey',
                         fontname='Comic Sans MS', fontsize=qfontsize)
            t.set_bbox(dict(facecolor='white', alpha=0.9, edgecolor='white'))

    def DrawArrows(self, gridworld, pi):
        ROWS = gridworld.rows
        COLS = gridworld.cols
        RSTEP = 1 / ROWS
        CSTEP = 1 / COLS
        # -- erase old policy arrows
        for k, v in pi.items():
            x = k[0] * CSTEP
            y = k[1] * RSTEP
            # top
            points = [[x + (CSTEP / 2 - 0.1 * CSTEP), y + (RSTEP - 0.1 * RSTEP)],
                      [x + (CSTEP / 2 + 0.1 * CSTEP), y + (RSTEP - 0.1 * RSTEP)], [x + CSTEP / 2, y + RSTEP]]
            triangle = plt.Polygon(points, fc='white')
            plt.gca().add_patch(triangle)
            # bottom
            points = [[x + (CSTEP / 2 - 0.1 * CSTEP), y + (0.1 * RSTEP)],
                      [x + (CSTEP / 2 + 0.1 * CSTEP), y + (0.1 * RSTEP)], [x + CSTEP / 2, y]]
            triangle = plt.Polygon(points, fc='white')
            plt.gca().add_patch(triangle)
            # left
            points = [[x + (0.1 * CSTEP), y + (RSTEP / 2 - 0.1 * RSTEP)],
                      [x + (0.1 * CSTEP), y + (RSTEP / 2 + 0.1 * RSTEP)], [x, y + RSTEP / 2]]
            triangle = plt.Polygon(points, fc='white')
            plt.gca().add_patch(triangle)
            # right
            points = [[x + (CSTEP - 0.1 * CSTEP), y + (RSTEP / 2 - 0.1 * RSTEP)],
                      [x + (CSTEP - 0.1 * CSTEP), y + (RSTEP / 2 + 0.1 * RSTEP)], [x + CSTEP, y + RSTEP / 2]]
            triangle = plt.Polygon(points, fc='white')
            plt.gca().add_patch(triangle)

            # -- draw new policy arrows
        for k, v in pi.items():
            x = k[0] * CSTEP
            y = k[1] * RSTEP
            if v == (0, 1):
                print('%s : %s' % (k, v))
                # top
                points = [[x + (CSTEP / 2 - 0.1 * CSTEP), y + (RSTEP - 0.1 * RSTEP)],
                          [x + (CSTEP / 2 + 0.1 * CSTEP), y + (RSTEP - 0.1 * RSTEP)], [x + CSTEP / 2, y + RSTEP]]
                triangle = plt.Polygon(points, fc='limegreen')
                plt.gca().add_patch(triangle)
            elif v == (0, -1):
                print('%s : %s' % (k, v))
                # bottom
                points = [[x + (CSTEP / 2 - 0.1 * CSTEP), y + (0.1 * RSTEP)],
                          [x + (CSTEP / 2 + 0.1 * CSTEP), y + (0.1 * RSTEP)], [x + CSTEP / 2, y]]
                triangle = plt.Polygon(points, fc='limegreen')
                plt.gca().add_patch(triangle)
            elif v == (-1, 0):
                print('%s : %s' % (k, v))
                # left
                points = [[x + (0.1 * CSTEP), y + (RSTEP / 2 - 0.1 * RSTEP)],
                          [x + (0.1 * CSTEP), y + (RSTEP / 2 + 0.1 * RSTEP)], [x, y + RSTEP / 2]]
                triangle = plt.Polygon(points, fc='limegreen')
                plt.gca().add_patch(triangle)
            elif v == (1, 0):
                print('%s : %s' % (k, v))
                # right
                points = [[x + (CSTEP - 0.1 * CSTEP), y + (RSTEP / 2 - 0.1 * RSTEP)],
                          [x + (CSTEP - 0.1 * CSTEP), y + (RSTEP / 2 + 0.1 * RSTEP)], [x + CSTEP, y + RSTEP / 2]]
                triangle = plt.Polygon(points, fc='limegreen')
                plt.gca().add_patch(triangle)

