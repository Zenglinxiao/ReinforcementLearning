# Reinforcement Learning, Practical 1 (Revised version)

## IMPORTANT
**You need to install OpenAI gym into your laptop: pip install gym**


## A) Environment

This assignement is divided in two part:

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
