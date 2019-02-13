# Reinforcement Learning, Practical 1 (Revised version)

## IMPORTANT
**You need to install OpenAI gym into your laptop: pip install gym**


**You are expected to modify new_agent.py (not agent.py)**

## A) Environment

This assignement will be divide in two part:

#### 1. Value Iteration + Policy Iteration
To practice Value / Policy iteration algorithm, we choose the
standard *Grid world* environment (inspired from Sutton's Reinforcement Learning book chapter 4).

You are an agent on an MxN grid and your goal is to reach the terminal
state at the top left or the bottom right corner.

For example, a 4x4 grid looks as follows:

    T  o  o  o
    
    o  x  o  o
    
    o  o  o  o
    
    o  o  o  T

x is your position and T are the two terminal states.

You can take actions in each direction (UP=0, RIGHT=1, DOWN=2, LEFT=3).
Actions going off the edge leave you in your current state.
You receive a reward of -1 at each step until you reach a terminal state.

#### 2. Q-Learning + SARSA
We used the Cliff Walking Environment (also from Sutton's book).

    Adapted from Example 6.6 (page 132) from Reinforcement Learning: An Introduction
    by Sutton and Barto:
    The board is a 4x12 matrix, with (using Numpy matrix indexing):
        [3, 0] as the start at bottom-left
        [3, 11] as the goal at bottom-right
        [3, 1..10] as the cliff at bottom-center
    Each time step incurs -1 reward, and stepping into the cliff incurs -100 reward
    and a reset to the start. An episode terminates when the agent reaches the goal.


## B) How can I interact with my environment ?
Both environments (`self.mdp.env` of your agent) are all a subclass of OpenAI 
Gym environment (docs: https://gym.openai.com/docs/#environments)
* Get observation space: `self.mdp.env.observation_space`
* Get action space: `self.mdp.env.action_space`
* Nb states: `self.mdp.env.nS`
* Nb actions: `self.mdp.env.nA`
* Transition function: `self.mdp.P`



## C) How do I complete these files ?

You are provided with the `main.py` file, a MDP test bed. Use `python main.py -h`
to check how you are supposed to use this file. You will quickly notice that all
subcommands return error messages.

Fill in the `# TO IMPLEMENT` part of the
code of `new_agent.py`. Remove the expection raising part (`raise NotImplementedError` ), and
complete the three blank methods for each Agent.


## D) How do I procede to be evaluated ?

You will be noted on the implementation of the 3 agents (SARSA is a bonus) in the `new_agents.py` file.
Bonus points will be given to clean and scalable code.
(Think of your code complexity)

You need to send `new_agent.py` and related dependancy to heri(at)lri(dot)fr
before December, 9th 2018 at 23:59.
