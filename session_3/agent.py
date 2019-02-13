import numpy as np

"""
Contains the definition of the agent that will run in an
environment.
"""

class RandomAgent:
    def __init__(self):
        """Init a new agent.
        """

    def act(self, observation):#observation stands for the current state, by act(observation) we want the action to execute
        """Acts given an observation of the environment.

        Takes as argument an observation of the current state, and
        returns the chosen action.
        See environment documentation: https://github.com/openai/gym/wiki/Pendulum-v0
        Range action: [-2, 2]
        Range observation (tuple):
            - cos(theta): [-1, 1]
            - sin(theta): [-1, 1]
            - theta dot: [-8, 8]
        """
        return [np.random.uniform(-2, 2)]

    def reward(self, observation, action, reward):
        """Receive a reward for performing given action on
        given observation.

        This is where your agent can learn. (Build model to approximate Q(s, a))
        """
        pass

class QLearningAgent:
    def __init__(self):
        """Init a new agent.
        """
        self.weight = np.random.randn(4)#ones(4) #shape(4,) float64
        self.alpha = 0.01 # learning rate
        self.gamma = 0.9 # discount
        self.epsilon = 0.01 # epsilon greedy
        self.current_state = None


    def act(self, observation):#observation stands for the current state, by act(observation) we want the action to execute
        """Acts given an observation of the environment.

        Takes as argument an observation of the current state, and
        returns the chosen action.
        See environment documentation: https://github.com/openai/gym/wiki/Pendulum-v0
        Range action: [-2, 2]
        Range observation (tuple):
            - cos(theta): [-1, 1]
            - sin(theta): [-1, 1]
            - theta dot: [-8, 8]
        """
        # observation: numpy.ndarray(float64) ex: [-0.99852278 -0.05433462 -0.11415908] shape(3,)
        # epsilon greedy get the action
        self.current_state = observation

        if np.random.random_sample() < self.epsilon:
            action = np.random.uniform(-2,2,1)
        else:
            action = self.best_action(self.current_state)
        return action
        #return [np.random.uniform(-2, 2)]

    def reward(self, observation, action, reward):
        """Receive a reward for performing given action on
        given observation.

        This is where your agent can learn. (Build model to approximate Q(s, a))
        """
        # update reward according to ..
        state_after_act = observation
        next_best_action = self.best_action(state_after_act) # action_on_policy
        V_after_state = np.sum(self.weight[:3] * state_after_act) + self.weight[3] * next_best_action
        V_bf_state = np.sum(self.weight[:3] * self.current_state) + self.weight[3] * action[0]
        loss = reward + self.gamma * V_after_state - V_bf_state
        x_a = np.concatenate((self.current_state, action))
        self.weight = self.weight + self.alpha * loss * x_a
        #print(self.weight)
        

    def best_action(self, observation):
        k_x = np.sum(self.weight[:3] * observation)
        best_act_candidate = k_x + self.weight[3]#- k_x/self.weight[3]
        best_action = np.array([min(max(best_act_candidate, -2), 2)])
        return best_action

Agent = QLearningAgent
