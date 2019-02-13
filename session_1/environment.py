"""
This file contains the definition of the environment
in which the agents are run.
Do not modify this file
"""
from gym.envs.toy_text import cliffwalking
import numpy as np
import sys
from gym.envs.toy_text import discrete

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class GridworldEnv(discrete.DiscreteEnv):
    """
    Grid World environment from Sutton's Reinforcement Learning book chapter 4.
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
    """

    metadata = {'render.modes': ['human', 'ansi']}

    def __init__(self, shape=[4,4]):
        if not isinstance(shape, (list, tuple)) or not len(shape) == 2:
            raise ValueError('shape argument must be a list/tuple of length 2')

        self.shape = shape
        # Nb states: self.mdp.env.nS
        # Nb actions: self.mdp.env.nA
        nS = np.prod(shape)
        nA = 4

        MAX_Y = shape[0]
        MAX_X = shape[1]
        # Transition function: self.mdp.P
        P = {}
        grid = np.arange(nS).reshape(shape)
        it = np.nditer(grid, flags=['multi_index'])

        while not it.finished:
            s = it.iterindex
            y, x = it.multi_index

            P[s] = {a : [] for a in range(nA)}

            is_done = lambda s: s == 0 or s == (nS - 1)
            reward = 0.0 if is_done(s) else -1.0

            # We're stuck in a terminal state
            if is_done(s):
                P[s][UP] = [(1.0, s, reward, True)]
                P[s][RIGHT] = [(1.0, s, reward, True)]
                P[s][DOWN] = [(1.0, s, reward, True)]
                P[s][LEFT] = [(1.0, s, reward, True)]
            # Not a terminal state
            else:
                ns_up = s if y == 0 else s - MAX_X
                ns_right = s if x == (MAX_X - 1) else s + 1
                ns_down = s if y == (MAX_Y - 1) else s + MAX_X
                ns_left = s if x == 0 else s - 1
                P[s][UP] = [(1.0, ns_up, reward, is_done(ns_up))]
                P[s][RIGHT] = [(1.0, ns_right, reward, is_done(ns_right))]
                P[s][DOWN] = [(1.0, ns_down, reward, is_done(ns_down))]
                P[s][LEFT] = [(1.0, ns_left, reward, is_done(ns_left))]

            it.iternext()

        # Initial state distribution is uniform
        isd = np.ones(nS) / nS

        # We expose the model of the environment for educational purposes
        # This should not be used in any model-free learning algorithm
        self.P = P

        super(GridworldEnv, self).__init__(nS, nA, P, isd)

    def _render(self, mode='human', close=False):
        if close:
            return

        outfile = StringIO() if mode == 'ansi' else sys.stdout

        grid = np.arange(self.nS).reshape(self.shape)
        it = np.nditer(grid, flags=['multi_index'])
        while not it.finished:
            s = it.iterindex
            y, x = it.multi_index

            if self.s == s:
                output = " x "
            elif s == 0 or s == self.nS - 1:
                output = " T "
            else:
                output = " o "

            if x == 0:
                output = output.lstrip()
            if x == self.shape[1] - 1:
                output = output.rstrip()

            outfile.write(output)

            if x == self.shape[1] - 1:
                outfile.write("\n")

            it.iternext()

class Environment:
    # List of the possible actions by the agents
    possible_actions = [0, 1, 2, 3] # UP, RIGHT, DOWN, LEFT

    def __init__(self):
        """Instanciate a new environement in its initial state.
        """
        self.env = cliffwalking.CliffWalkingEnv()

    def observe(self):
        """Returns the current observation that the agent can make
        of the environment, if applicable.
        """
        return self.env.s

    def act(self, action):
        """Perform given action by the agent on the environment,
        and returns a reward.
        """
        observation, reward, done, _ = self.env.step(action)
        return reward, done


class EnvironmentGridWorld:
    # List of the possible actions by the agents
    possible_actions = [0, 1, 2, 3] # UP, RIGHT, DOWN, LEFT

    def __init__(self):
        """Instanciate a new environement in its initial state.
        """
        self.env = GridworldEnv()

    def observe(self):
        """Returns the current observation that the agent can make
        of the environment, if applicable.
        """
        return self.env.s

    def act(self, action):
        """Perform given action by the agent on the environment,
        and returns a reward.
        """
        """The environment’s step function returns what our actions are doing to the environment. In fact, step returns four values.
            * observation (object): an environment-specific object representing your observation of the environment.
            * reward (float): amount of reward achieved by the previous action. 
            * done (boolean): whether it’s time to reset the environment again.done being True indicates the episode has terminated. 
            * info (dict): diagnostic information useful for debugging.
        """  
        observation, reward, done, _ = self.env.step(action)
        return reward, done
