"""
Author: Jay Chakalasiya -> https://github.com/jay-chakalasiya
"""

from utils import get_file_data


class RockPaperScissor:
    def __init__(self, agent):
        self.agent = agent
        self.wins_so_far = 0
        self.ties_so_far = 0
        self.total_plays = 0
    
    def play_single_interactive_round(self):
        player_move = input('Enter Your Move:')

        if player_move == 'E':
            print(' <===== Final Summary For Computer =====> ')
            print("Wins = {}, Lost = {}, Ties = {}, Total = {}".format(self.wins_so_far, \
                self.total_plays-self.wins_so_far-self.ties_so_far, self.ties_so_far, self.total_plays))
            return

        elif player_move in ['R', 'P', 'S']:
            computer_move = self.agent.move()
            current_move_score = self.agent.update(computer_move, player_move)
            if current_move_score == 1:
                self.wins_so_far += 1
            elif current_move_score == 0:
                self.ties_so_far += 1
            self.total_plays +=1
            print(self.make_string(current_move_score))
            
        elif player_move == 'F':
            file_path = input('Enter File Path:')
            self.play_from_file(file_path)

        else:
            print("Invaid input -> please enter of the [R, P, S] -> (Rock, Paper, Scissor) or [E, F] -> (Exit, or File input)")
        
        self.play_single_interactive_round()
        return

    def play_from_file(self, file_path):
        data = get_file_data(file_path)
        if not data:
            print('File Does not exist or Dont have any data, Please input valid filename with some data')
            return
        round_wins = 0
        round_ties = 0
        for player_move in data:
            computer_move = self.agent.move()
            current_move_score = self.agent.update(computer_move, player_move)
            if current_move_score == 1:
                round_wins += 1
            elif current_move_score == 0:
                round_ties += 1
        print("Summary of Playing from file -> (Wins, Lost, Ties, Total_Games) = ({}, {}, {}, {})".format(round_wins, \
            len(data)-round_wins-round_ties, round_ties, len(data)))
        self.wins_so_far += round_wins
        self.ties_so_far += round_ties
        self.total_plays += len(data)
        
        print("So far (Wins, Lost, Ties, Total_Games) = ({}, {}, {}, {})".format(self.wins_so_far, \
            self.total_plays-self.wins_so_far-self.ties_so_far, self.ties_so_far, self.total_plays))

    def make_string(self, current_score):
        action = 'LOST'
        if current_score == 1:
            action = 'WON '
        elif current_score == 0:
            action = 'TIE '
        return "Computer {}, So far (Wins, Lost, Ties, Total_Games) = ({}, {}, {}, {})".format(action, \
            self.wins_so_far, self.total_plays-self.wins_so_far-self.ties_so_far, self.ties_so_far, self.total_plays)