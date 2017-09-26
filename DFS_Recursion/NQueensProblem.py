import numpy


#-----------------------------------------------------------
class Action(object):
    def __init__(self, w=1, ns=None):
        self.action_cost = w
        self.next_state = ns
    def ActionCost(self):
        return self.action_cost
    def NextState(self):
        return self.next_state


class State(object):
    def __init__( self, n=0, qr=[]):
        self.queen_count = n
        self.queen_row_positions = qr
        self.label = str(self.queen_row_positions)
    
    def __gt__(self, other):
        return self.queen_count > other.queen_count
    def GetLabel( self ):
        return self.label
    def Print( self ):
        print("rp: ", self.queen_row_positions, " qc: ", self.queen_count)


#-----------------------------------------------------------
class NQueensProblem(object):
    def __init__(self, filename=None, N=8):
        self.num_queens = N
        self.start_state = State(0,numpy.array([-1]*N))
    
    def Actions( self, state ):
        actions = []
        used_rows = numpy.array([-1]*self.num_queens)
        used_tuples = set()
        
        # find the free rows    and the used tuples
        for i in range(0,state.queen_count):
            used_rows[state.queen_row_positions[i]]=1
            used_tuples.add((state.queen_row_positions[i],i))
        
        #print("used tuples: ", used_tuples)
        
        if state.queen_count == 0:
            free_rows = numpy.r_[0:self.num_queens]
            free_rows_size = free_rows.size
        else:
            tmp = numpy.where(used_rows==-1)
            free_rows = tmp[0]
            free_rows_size = free_rows.size
    
        #print("free rows: ", free_rows)
        
        # for each free row, check the diagonals to the left
        for i in range(0,free_rows_size):
            # check up
            up = True
            r = free_rows[i]-1
            c = state.queen_count-1
            while r >= 0 and c >= 0 and up:
                #print("r,c ", (r,c))
                #print(used_tuples)
                #print((r,c) in used_tuples)
                if ( (r,c) in used_tuples ):    up = False
                r = r-1
                c = c-1
            
            # check down
            down = True
            r = free_rows[i]+1
            c = state.queen_count-1
            while r < self.num_queens and c >= 0 and down and up:
                if ( (r,c) in used_tuples ):    down = False
                r = r+1
                c = c-1
            
            #print("up: ", up, ' ', down, ' ', i)
            if (up and down) or state.queen_count == 0:
                new_positions = numpy.array(state.queen_row_positions)
                new_positions[state.queen_count] = free_rows[i]
                actions.append(Action(1, State(state.queen_count+1, new_positions)))
        
            return actions
                        
                        
    def GoalTest( self, state ):
        #print("GT: ", state.queen_count)
        return self.num_queens == state.queen_count

    def SetStartState( self, start ):
        self.start_state = start
    def GetStartState( self ):
        return self.start_state