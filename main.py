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

    Game = RockPaperScissor(agent)
    Game.play_single_interactive_round()


    
if  __name__ == "__main__":
    main()
    