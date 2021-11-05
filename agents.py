"""
Author: Jay Chakalasiya -> https://github.com/jay-chakalasiya
"""

import random
import numpy as np


class Agent:
    def __init__(self):
        self.possible_moves = ['R', 'P', 'S']
        self.move_idx = {move:i for i, move in enumerate(self.possible_moves)}
        self.player_to_comp = {'R':'P', 'P':'S', 'S':'R'}
        self.comp_to_player = {'P':'R', 'S':'P', 'R':'S'}

    def update(self, computer_move, player_move):
        raise NotImplementedError

    def move(self):
        raise NotImplementedError


class randomAgent(Agent):
    """
    This agent chooses all the actions randomly.
    """
    def update(self, computer_move, player_move):
        if computer_move == player_move:
            return 0
        return 1 if self.comp_to_player[computer_move] == player_move else -1

    def move(self):
        return random.choice(self.possible_moves)


class banditAgent(Agent):
    """
    bandit agents are based on the Thompson sampling algorithm. 
    As there are three possible moves, we will try to predict what would 
    player choose as his next move and perform beating move accordingly

    Think of any action 'R', 'P', 'S' as independent bandits, where player 
    chooses one action/bandit to play with. If we are bale to predict same 
    then its a success else failure, and according to successes and failures
    we update beta distribution of that particular action/bandit.

    Reference: http://proceedings.mlr.press/v23/agrawal12/agrawal12.pdf
    """
    def __init__(self):
        super().__init__()
        self.states = [{'successes':0, 'failures':0} for move in self.possible_moves]

    def update(self, computer_move, player_move):
        predicted_player_move = self.comp_to_player[computer_move]
        if predicted_player_move == player_move:
            score = 1
            self.states[self.move_idx[predicted_player_move]]['successes']+=1
        else:
            score = 0 if computer_move == player_move else -1
            if score!=0:
                # only increase failures if we losse, no updates if its a tie
                self.states[self.move_idx[predicted_player_move]]['failures']+=1
            
        return score

    def move(self):
        drawn_samples = [np.random.beta(state['successes']+1, state['failures']+1) for state in self.states]
        predicetd_player_move_idx = np.argmax(drawn_samples)
        return self.player_to_comp[self.possible_moves[predicetd_player_move_idx]]


class markovAgent(Agent):
    """
    Markov agent is based on markov models, There are two assumptions here
    1) The players next move is solely depending upon the precious move
    2) The player will make next move based on his previous move and 
       computer's previous move

    In brief we will create a 9x3 table where we have past 9 pairs of players 
    and computers possibe last mvoes and 3 sets of move the player can take in next step.

    We initalize all state transition with equal probability and then update according to player's action.
    """

    def __init__(self, decay):
        super().__init__()
        self.decay = decay
        possible_io_pairs = []
        for last_input in self.possible_moves:
            for last_output in self.possible_moves:
                possible_io_pairs.append(last_input+last_output) 
        
        # State transition table is in form 'RR' : [[0, 1/3], [0, 1/3], [0, 1/3]] -> 
        # where 0 is no of observations and 1/3 is probability -> which sums up to 1
        self.transition_table = {io_pair: [[0, 1/3] for next_action in self.possible_moves] for io_pair in possible_io_pairs}
        self.last_pair = random.choice(possible_io_pairs)

    def update(self, computer_move, player_move):
        predicted_player_move = self.comp_to_player[computer_move]

        for i in range(len(self.transition_table[self.last_pair])):
            self.transition_table[self.last_pair][i][0] *= self.decay

        # we predicted some move player might make in move function, but he made player_move, 
        # so we increase the observation count for the move player actually made
        players_move_idx = self.move_idx[player_move]
        self.transition_table[self.last_pair][players_move_idx][0] += 1

        # redistribute the probability to sum up to 1
        total_observations = sum([self.transition_table[self.last_pair][action_idx][0] for action_idx in range(len(self.possible_moves))])
        for action_idx in range(len(self.possible_moves)):
            self.transition_table[self.last_pair][action_idx][1] = self.transition_table[self.last_pair][action_idx][0]/total_observations

        # update last_pair
        self.last_pair = computer_move+player_move

        if player_move == predicted_player_move:
            return 1
        elif computer_move == player_move:
            return 0
        else:
            return -1


    def move(self):
        probs = [action_prob[1] for action_prob in self.transition_table[self.last_pair]]
        players_predicted_move = np.random.choice(self.possible_moves, p=probs)
        return self.player_to_comp[players_predicted_move]




        


