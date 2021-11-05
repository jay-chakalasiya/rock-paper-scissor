"""
Author: Jay Chakalasiya -> https://github.com/jay-chakalasiya
"""

import os
import argparse



def parse_arguments():
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-a", "--agent", default = "markov", \
        help = "it should one of the following agent [random, bandit, markov] -> defult is random")
    parser.add_argument("-f", "--fileinput", default = None, \
        help = "Provide path to the input file, the file containes each time step inpus in form of R, P, S each entry i its own line")

    args = parser.parse_args()

    if args.agent not in ['random', 'bandit', 'markov']:
        raise Exception("Argument random can only holds values from [random, bandit, markov]")

    args.input_data = None
    if args.fileinput:
        args.input_data = get_file_data(args.fileinput)
        if not args.input_data:
            raise Exception("File Does not exist or Don't have any data in it")

    return args


def get_file_data(filepath):
    if not os.path.exists(filepath):
        print("File Does not exist")
        return []
    data = open(filepath).readlines()
    data = [instance.strip('\n') for instance in data]
    return data


def train(agent, training_data):
    if not training_data:
        return
    training_wins = 0
    training_ties = 0
    for player_move in training_data:
        computer_move = agent.move()
        current_move_score = agent.update(computer_move, player_move)

        if current_move_score == 1:
            training_wins += 1
        elif current_move_score == 0:
            training_ties += 1

    print("Training States ===>  (Wins, Lost, Ties, Total_Moves) = ({}, {}, {}, {})".format(training_wins, \
        len(training_data)-training_wins-training_ties, training_ties, len(training_data)))
    return 

