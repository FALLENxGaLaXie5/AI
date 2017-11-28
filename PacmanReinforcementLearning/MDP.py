import random


class MDP:
    def __init__(self, init, actlist, terminals, gamma=.9):
        self.init = init
        self.actlist = actlist
        self.terminals = terminals
        self.gamma = gamma
        self.states = set()
        self.reward = {}

    # a fixed list of actions that can be performed in this state
    def actions(self, state):
        if state in self.terminals:
            return [None]
        else:
            return self.actlist

    # return a list of (result-state, probability) pairs."""
    def T(state, action):
        abstract
        
    # return a numeric reward for this state.
    def R(self, state):
        return self.reward[state]


# solve an MDP using value iteration
def ValueIteration(mdp, epsilon=0.001):
    U1 = dict([(s, 0) for s in mdp.states])
    while True:    #for _ in range(0,3):   for smaller tests
        U = U1.copy()
        delta = 0
        for s in mdp.states:
            if s == mdp.terminals[0][0]: 
                U1[s] = 1 
            elif s == mdp.terminals[1][0]: 
                U1[s] = -1
            else:
                for a in mdp.actions(s):
                    U1[s] = max(Q(a, s, U, mdp), U1[s])
                
            delta = max(delta, abs(U1[s] - U[s]))
        if delta < epsilon: #* (1 - gamma) / gamma:
             return U
    return U

def ValueIterationStep(mdp, V):
    U = V.copy()
    for s in mdp.states:
        if s == mdp.terminals[0][0]: 
            V[s] = 1 
        elif s == mdp.terminals[1][0]: 
            V[s] = -1
        else:
            for a in mdp.actions(s):
                V[s] = max(Q(a, s, U, mdp), V[s])                
    return V

# given MDP and utility function U, compute best policy, a mapping from state to action
def PolicyExtraction(mdp, U):
    pi = {}
    for s in mdp.states:
        pi[s] = argmax(mdp.actions(s), lambda a:Q(a, s, U, mdp))
    return pi

# given MDP and utility function U, compute best policy, a mapping from state to action
def QExtraction(mdp, U):
    Qs = dict([(s, [a for a in mdp.actions(s)] ) for s in mdp.states  ])
    for s in mdp.states:
        i = 0
        for a in mdp.actions(s):
            Qs[s][i] = Q(a, s, U, mdp)
            i = i + 1
    return Qs

# expected utility of doing a in state s, according to the MDP and U
def Q(a, s, U, mdp):
    return sum([p * (mdp.R(s) + mdp.gamma * U[s1]) for (p, s1) in mdp.T(s, a)])

# solve an MDP using policy iteration
def PolicyIteration(mdp):
    U = dict([(s, 0) for s in mdp.states])
    pi = dict([(s, random.choice(mdp.actions(s))) for s in mdp.states])
    while True:
        U = PolicyEvaluation(pi, U, mdp)
        pii = PolicyExtraction(mdp, U)
        if pi == pii:
            return pi
        else:
            pi = pii


# return updated utility mapping U from each state to its utility, using an approximation (modified policy iteration)."""
def PolicyEvaluation(pi, U, mdp, k=20):
    for i in range(k):
        for s in mdp.states:
            U[s] = Q(pi[s], s, U, mdp)
    return U

#======================================================================================   


def PrintDict(obj):
        for k, v in obj.items():
            if hasattr(v, '__iter__') and hasattr(v, 'items'):
                print( k )
                PrintDict(v)
            else:
                print( '%s : %s' % (k, v) )

def argmax( x, f ):
    return max(x, key=f)

