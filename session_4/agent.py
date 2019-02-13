import numpy as np
from environment import Environment
import os
import cma
"""
Contains the definition of the agent that will run in an
environment.
"""

class RandomAgent:
    def __init__(self):
        """
        Init a new agent.
        """
        self.train() # Do not remove this line!!

    def train(self):
        """
        Learn your (final) policy.

        Use evolution strategy algortihm CMA-ES: https://pypi.org/project/cma/

        Possible action: [0, 1, 2]
        Range observation (tuple):
            - position: [-1.2, 0.6]
            - velocity: [-0.07, 0.07]
        """
        # 1- Define state features
        # 2- Define search space (to define a policy)
        # 3- Define objective function (for policy evaluation)
        # 4- Use CMA-ES to optimize the objective function
        # 5- Save optimal policy

        # This is an example of using Envrironment class (No learning is done yet!)
        for i in range(10):
            env = Environment()
            done = False
            while not done:
                reward, done = env.act(env.sample_action())
                # print(env.state)

    def act(self, observation):
        """
        Acts given an observation of the environment (using learned policy).

        Takes as argument an observation of the current state, and
        returns the chosen action.
        See environment documentation: https://github.com/openai/gym/wiki/MountainCar-v0
        Possible action: [0, 1, 2]
        Range observation (tuple):
            - position: [-1.2, 0.6]
            - velocity: [-0.07, 0.07]
        """
        return np.random.choice([0, 1, 2])


class CMAESAgent:
    def __init__(self):
        """
        Init a new agent.
        """
        #Init 2 hidden layer MLP
        n1_in = 2
        n1_out = 32
        n2_in = n1_out
        n2_out = 3
        self.w1_flat = np.empty(n1_in*n1_out) 
        self.b1_flat = np.empty(n1_out) 
        self.w2_flat = np.empty(n2_in*n2_out) 
        self.b2_flat = np.empty(n2_out) 
        nb_parameters = len(self.w1_flat)+len(self.b1_flat)+len(self.w2_flat)+len(self.b2_flat)
        self.es = cma.CMAEvolutionStrategy(nb_parameters*[0], 0.8) 
        if os.path.exists("./weights.npy"):
            weight = np.load("weights.npy")
            self.w1_flat = np.array(weight[0:len(self.w1_flat)])
            self.b1_flat = np.array(weight[len(self.w1_flat):len(self.w1_flat)+len(self.b1_flat)])
            self.w2_flat = np.array(weight[len(self.w1_flat)+len(self.b1_flat):len(self.w1_flat)+len(self.b1_flat)+len(self.w2_flat)])
            self.b2_flat = np.array(weight[len(self.w1_flat)+len(self.b1_flat)+len(self.w2_flat):len(self.w1_flat)+len(self.b1_flat)+len(self.w2_flat)+len(self.b2_flat)])
        else:
            self.train() # Do not remove this line!!

    def train(self):
        """
        Learn your (final) policy.

        Use evolution strategy algortihm CMA-ES: https://pypi.org/project/cma/

        Possible action: [0, 1, 2]
        Range observation (tuple):
            - position: [-1.2, 0.6]
            - velocity: [-0.07, 0.07]
        """
        # 1- Define state features
        # 2- Define search space (to define a policy)
        # 3- Define objective function (for policy evaluation)
        # 4- Use CMA-ES to optimize the objective function
        # 5- Save optimal policy

        generations  = 10000
        for i in range(generations):
            solutions = self.es.ask()
            print ("iteration:",i," ;")
            result = []
            for solution in solutions:
                env = Environment()
                n_w1 = len(self.w1_flat)
                self.w1_flat = np.array(solution[0:len(self.w1_flat)])
                self.b1_flat = np.array(solution[len(self.w1_flat):len(self.w1_flat)+len(self.b1_flat)])
                self.w2_flat = np.array(solution[len(self.w1_flat)+len(self.b1_flat):len(self.w1_flat)+len(self.b1_flat)+len(self.w2_flat)])
                self.b2_flat = np.array(solution[len(self.w1_flat)+len(self.b1_flat)+len(self.w2_flat):len(self.w1_flat)+len(self.b1_flat)+len(self.w2_flat)+len(self.b2_flat)])
                done = False
                accumulated_reward = 0
                while not done:
                    observation = env.observe()
                    reward, done = env.act(self.act(observation))
                    accumulated_reward += reward
                result.append(-accumulated_reward)
            self.es.tell(solutions, result)
            if np.mean(result) < 100: # result.avg=200 when cound not achieve aim, less is better.
                print ("Good generation founded")
                break

        index = np.argmin(result)
        weight = solutions[index]
        np.save("weights.npy",weight)
        self.w1_flat = np.array(weight[0:len(self.w1_flat)])
        self.b1_flat = np.array(weight[len(self.w1_flat):len(self.w1_flat)+len(self.b1_flat)])
        self.w2_flat = np.array(weight[len(self.w1_flat)+len(self.b1_flat):len(self.w1_flat)+len(self.b1_flat)+len(self.w2_flat)])
        self.b2_flat = np.array(weight[len(self.w1_flat)+len(self.b1_flat)+len(self.w2_flat):len(self.w1_flat)+len(self.b1_flat)+len(self.w2_flat)+len(self.b2_flat)])
        

        


    def act(self, observation):
        """
        Acts given an observation of the environment (using learned policy).

        Takes as argument an observation of the current state, and
        returns the chosen action.
        See environment documentation: https://github.com/openai/gym/wiki/MountainCar-v0
        Possible action: [0, 1, 2]
        Range observation (tuple):
            - position: [-1.2, 0.6]
            - velocity: [-0.07, 0.07]
        """
        states = np.array(observation).reshape(1,2)
        
        w1 = self.w1_flat.reshape(2,32)
        b1 = self.b1_flat.reshape(1,32)
        w2 = self.w2_flat.reshape(32,3)
        b2 = self.b2_flat.reshape(1,3)
        result = np.dot(np.tanh(np.dot(states,w1)+b1), w2)+b2
        action = np.argmax(result)
        return action #np.random.choice([0, 1, 2])

Agent =  CMAESAgent #RandomAgent
