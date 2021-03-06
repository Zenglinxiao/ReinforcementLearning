import numpy as np
import gym
np.random.seed(0)
"""
This file contains the definition of the environment
in which the agents are run.
"""

class Environment:
    # List of the possible actions by the agents

    def __init__(self):
        """Instanciate a new environement in its initial state.
        """
        self.env = gym.make("Pendulum-v0")
        self.state = self.env.reset()
        self.env.seed(0)
        self.nb_step = 0

    def reset(self):
        self.nb_step = 0
        self.state = self.env.reset()

    def render(self):
        self.env.render()

    def observe(self):
        """Returns the current observation that the agent can make
        of the environment, if applicable.
        """
        return self.state

    def act(self, action):
        """Perform given action by the agent on the environment,
        and returns a reward.
        """
        self.state, reward, _, info = self.env.step(action)
        self.nb_step += 1

        terminal = False
        if self.nb_step > 2000:
            terminal = True
        return (reward, "Victory" if terminal else None)

def envs_from_spec(spec):
    """
    Generate a list of fixed environements used for test from provided
    spec.

    spec is a list(list(float))

    Created environments are pseudo-random: two agents doing the exact
    same actions must generate the exact same tranjectory & rewards.
    """
    return [Environment() for _ in range(10)]
