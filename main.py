"""
Author: Jay Chakalasiya -> https://github.com/jay-chakalasiya
"""

from utils import parse_arguments, train
from agents import banditAgent, randomAgent, markovAgent
from game_env import RockPaperScissor

def main():
    args = parse_arguments()
    agent = randomAgent()
    if args.agent == 'bandit':
        agent = banditAgent()
    elif args.agent == 'markov':
        agent = markovAgent(0.9)
        pass

    if args.input_data:
        train(agent, args.input_data)

    for i in range(5):
        print('')
    print('==========> Welcome to Rock-Paper-Scissor <===========')
    print(' When prompted the input , you can choose R, P, S : chatcters for Rock, Paper or Scissor(It is case sensitive)')
    print('')
    print(' Other input option is F and then there will be prompt to provice input va a file, the file must contain R, P or S, each action in new line, example file is provided as input.txt')
    print('')
    print(' Input E to exit the game')
    print('')

    Game = RockPaperScissor(agent)
    Game.play_single_interactive_round()


    
if  __name__ == "__main__":
    main()
    
