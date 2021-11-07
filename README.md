# Rock-Paper-Scissor Game

## How to run

### Run from source

```
$ python main.py
```

#### Requirements
- Python >= 3.6
- numpy

### Run from Docker image
```
$ dcoker pull jay-chakalasiya/rock-paper-scissor
$ docker run -it jaychakalasiya/rock-paper-scissor
```

## File Structure

```
Root
|
|-----agents.py
|-----game_env.py
|-----main.py
|-----utils.py
|-----input.txt

```

### main.py
This file is the entry point of this game

### utils.py
This file contains varioud functions used in the game, which includes commandline argument parser and some file reading helper fucntions
#### Command line arguments
```
$ python main.py -a [agent name = random/bandit/markov] -f [training_file_path = input.txt]
```
- Type of agents are described in the description below -> default is markov
- Trainig_file = input.txt is the file used to pre-teach our agent something before we start interacting with user (Optional)

### game_env.py
This file has the game environment for game of Rock-Paper-Scissor, this class handles the interaction with the player throughout the game

### agents.py
This file holds three different computer player agents
```
random -> class randomAgent()...
bandit -> class banditAgent()...
markov -> class markovAgent()...
```

#### Random Agent
- Random agents makes a random move at any time

#### Bandit Agent
- the bandit agents assumes that the player is choosing Rock, Paper or Scissor independently of previous actions it observed or took.
- Here bandit agents tries to predict players actions based on Thompson samping and computer takes winnig move agains that predicted move.
- According to the successes and failures the agent learns new sampling parameters

#### Markov Agent
- Markov agents makes decisions based on the previous moves. 
- Markov agents works on the principal that the player is taking next action based on previous actions(his and opponents).