from connectfour.agents.computer_player import RandomAgent
import random
import copy

class StudentAgent(RandomAgent):
    def __init__(self, name):
        super().__init__(name)
        self.MaxDepth = 2
        # self.NextState = None


    def get_move(self, board):
        """
        Args:
            board: An instance of `Board` that is the current state of the board.

        Returns:
            A tuple of two integers, (row, col)
        """

        # self.NextState = copy.deepcopy(board)
        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            next_state = board.next_state(self.id, move[1])
            moves.append( move )
            vals.append( self.dfMiniMax(next_state, 1) )

        bestMove = moves[vals.index( max(vals) )]
        print(bestMove)
        
        return bestMove

    def dfMiniMax(self, board, depth):
        # Goal return column with maximized scores of all possible next states
        
        if depth == self.MaxDepth:
            return self.evaluateBoardState(board)

        valid_moves = board.valid_moves()
        vals = []
        moves = []

        for move in valid_moves:
            if depth % 2 == 1:
                next_state = board.next_state(self.id % 2 + 1, move[1])
            else:
                next_state = board.next_state(self.id, move[1])
                
            moves.append( move )
            vals.append( self.dfMiniMax(next_state, depth + 1) )
            #max(vals)
            #alpha = max(alpha,value)
            #if alpha > beta: break

        
        if depth % 2 == 1:
            bestVal = min(vals)
        else:
            bestVal = max(vals)

        return bestVal
    
    def score(self, array, board):
        return 0
    
    def evaluateBoardState(self, board):        
        # Check if winning piece/move
        if board.winner() == self.id:
            return 1
        elif board.winner() == self.id % 2 + 1:
            return -1

        # Check if draw
        if board.terminal():
            return 0

        # Check row 4 piece position
        # Check for each winning position
        score = 0
        for row in range(board.height):
            for col in range(board.width - (board.num_to_connect - 1)) :
                checkRow = board.board[row][col:col + board.num_to_connect]
                if checkRow.count(self.id) == 3 and checkRow.count(0) == 1:
                    score += 10
                elif checkRow.count(self.id) == 2 and checkRow.count(0) == 2:
                    score += 3
                elif checkRow.count(self.id % 2 + 1) == 3 and checkRow.count(0) == 1:
                    score -= 5  


        return score
        # Check column 4 piece position
       
        """
        Your evaluation function should look at the current state and return a score for it. 
        As an example, the random agent provided works as follows:
            If the opponent has won this game, return -1.
            If we have won the game, return 1.
            If neither of the players has won, return a random number.
        """
        
        """
        These are the variables and functions for board objects which may be helpful when creating your Agent.
        Look into board.py for more information/descriptions of each, or to look for any other definitions which may help you.

        Board Variables:
            board.width 
            board.height
            board.last_move
            board.num_to_connect
            board.winning_zones
            board.score_array 
            board.current_player_score

        Board Functions:
            get_cell_value(row, col)
            try_move(col)
            valid_move(row, col)
            valid_moves()
            terminal(self)
            legal_moves()
            next_state(turn)
            winner()
        """
				
        # return random.uniform(0, 1)

