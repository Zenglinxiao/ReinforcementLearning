"""
File to complete. Contains the agents
"""
import numpy as np
import math
import random

class Agent(object):
    """Agent base class. DO NOT MODIFY THIS CLASS
    """

    def __init__(self, mdp):
        super(Agent, self).__init__()
        # Init with a random policy
        #self.policy = np.zeros((4, mdp.env.observation_space.n)) + 0.25
        self.policy = np.zeros((mdp.env.observation_space.n, 4)) + 0.25
        self.mdp = mdp
        self.discount = 0.9

        # Intialize V or Q depends on your agent
        # self.V = np.zeros(self.mdp.env.observation_space.n)
        self.Q = np.zeros((mdp.env.observation_space.n, 4))
        #self.Q = np.zeros((4, self.mdp.env.observation_space.n))

    def update(self, observation, action, reward):
        # DO NOT MODIFY. This is an example
        pass

    def action(self, observation):
        # DO NOT MODIFY. This is an example
        return self.mdp.env.action_space.sample()


class QLearning(Agent):
    def __init__(self, mdp):
        super(QLearning, self).__init__(mdp)

    def update(self, observation, action, reward):
        # TO IMPLEMENT
        alpha = 0.01
        gamma = self.discount
        trans_prob, next_state, rd, done = self.mdp.env.P[observation][action]
        learned = trans_prob * (rd + gamma * self.Q[next_state][action] )
        self.Q[observation][action] += alpha * (learned - self.Q[observation][action])
        self.policy[observation] = np.eye(self.mdp.env.nA)[np.argmax(self.Q[observation])]
        observation = next_state#?self.mdp.env.step(action)
        
        #raise NotImplementedError

    def action(self, observation):
        # TO IMPLEMENT
        episilon = 0.1
        best_action = np.argmax(self.policy[observation])
        if np.random.random_sample() < episilon:
            action = np.random.randint(4)
        else:
            action = best_action
        return action#super(QLearning, self).action(observation)


class SARSA(Agent):
    def __init__(self, mdp):
        super(SARSA, self).__init__(mdp)

    def update(self, observation, action, reward):
        # TO IMPLEMENT
        raise NotImplementedError

    def action(self, observation):
        # TO IMPLEMENT
        return super(SARSA, self).action(observation)


class ValueIteration:
    def __init__(self, mdp):
        self.mdp = mdp
        self.gamma = 0.9

    def optimal_value_function(self, policy):
        """1 step of value iteration algorithm
            Return: State Value V
        """
        # Intialize random V
        V = np.zeros(self.mdp.env.nS)

        # TO IMPLEMENT
        '''
        epsilon = 0.00001
        delta = 1
        while delta > epsilon:
            delta = 0
            for s in range(self.mdp.env.nS):
                v = V[s]
                for a, act_prob in enumerate(policy[s]):
                    for trans_prob, next_state, reward, done in self.mdp.env.P[s][a]:
                        V[s] += act_prob * ( trans_prob * reward + self.gamma * trans_prob * V[next_state] )
                delta = max(delta, abs(v-V[s]))    
            for s in range(self.mdp.env.nS):
        '''
        epsilon = 0.0001
        delta = 1
        while delta > epsilon:
            delta = 0
            for s in range(self.mdp.env.nS):
                A=np.zeros(self.mdp.env.nA)
                #v = V[s]
                for a, act_prob in enumerate(policy[s]):
                    for trans_prob, next_state, reward, done in self.mdp.env.P[s][a]:
                        A[a] += trans_prob * (reward + self.gamma * V[next_state] )
                        #V[s] += act_prob *  trans_prob * (reward + self.gamma * V[next_state] )
                max_a_value = np.max(A)
                delta = max(delta, np.abs(max_a_value-V[s]))
                V[s]=max_a_value
        return V

    def optimal_policy_extraction(self, V):
        """2 step of policy iteration algorithm
            Return: the extracted policy
        """
        policy = np.zeros([self.mdp.env.nS, self.mdp.env.nA])
        # TO IMPLEMENT
        for s in range(self.mdp.env.nS):
            A=np.zeros(self.mdp.env.nA)
            for a, act_prob in enumerate(policy[s]):
                for trans_prob, next_state, reward, done in self.mdp.env.P[s][a]:
                    A[a] += trans_prob * (reward + self.gamma * V[next_state] )
            max_a = np.argmax(A)
            policy[s, max_a] = 1.0
        return policy

    def value_iteration(self):
        """This is the main function of value iteration algorithm.
            Return:
                final policy
                (optimal) state value function V
        """
        policy = np.ones([self.mdp.env.nS, self.mdp.env.nA]) / self.mdp.env.nA
        V = None

        # TO IMPLEMENT
        V = self.optimal_value_function(policy)
        policy = self.optimal_policy_extraction(V)
        return policy, V


class PolicyIteration:
    def __init__(self, mdp):
        self.mdp = mdp
        self.gamma = 0.9

    def policy_evaluation(self, policy):
        """1 step of policy iteration algorithm
            Return: State Value V
        """
        V = np.zeros(self.mdp.env.nS) # intialize V to 0's

        # TO IMPLEMENT
        epsilon = 0.0001
        delta = 1
        while delta > epsilon:
            delta = 0
            for s in range(self.mdp.env.nS):
                v=0
                #v = V[s]
                for a, act_prob in enumerate(policy[s]):
                    for trans_prob, next_state, reward, done in self.mdp.env.P[s][a]:
                        v += act_prob *  trans_prob * (reward + self.gamma * V[next_state] )
                        #V[s] += act_prob *  trans_prob * (reward + self.gamma * V[next_state] )
                delta = max(delta, np.abs(v-V[s]))
                V[s]=v
            # when delta < epsilon, then break    
        return np.array(V)

    def policy_improvement(self, V, policy):
        """2 step of policy iteration algorithm
            Return: the improved policy
        """
        # TO IMPLEMENT

        for s in range(self.mdp.env.nS):
                chosen_action_bf = np.argmax(policy[s])
                action_v = np.zeros(self.mdp.env.nA)
                for a in range(self.mdp.env.nA):
                    for trans_prob, next_state, reward, done in  self.mdp.env.P[s][a]:
                        #action_v[a] += trans_prob * (reward + self.gamma * V[next_state])
                        action_v[a] += trans_prob *  V[next_state]
                chosen_action_at = np.argmax(action_v)
                if chosen_action_at != chosen_action_bf:
                    policy[s] = np.eye(self.mdp.env.nA)[chosen_action_at]

        return policy


    def policy_iteration(self):
        """This is the main function of policy iteration algorithm.
            Return:
                final policy
                (optimal) state value function V
        """
        # Start with a random policy(pi)
        policy = np.ones([self.mdp.env.nS, self.mdp.env.nA]) / self.mdp.env.nA
        V = None
        #V = self.policy_evaluation(policy)
        #print(V.reshape(self.mdp.env.shape))
        # To implement: You need to call iteratively step 1 and 2 until convergence
        isConvergence = False
        niteration = 0
        
        while not isConvergence:
            V = self.policy_evaluation(policy)
            policy_improved = self.policy_improvement(V,policy)
            V_improved = self.policy_evaluation(policy_improved)
            isConvergence = np.array_equal(V_improved, V)
            policy = policy_improved
            niteration += 1
            if isConvergence:
                print(niteration)
                print(V.reshape(self.mdp.env.shape))
                print(policy.reshape([self.mdp.env.nS, self.mdp.env.nA]))
        return policy, V
        '''
        while True:
            # Evaluate the current policy
            V = self.policy_evaluation(policy)
        
            # Will be set to false if we make any changes to the policy
            policy_stable = True
        
            # For each state...
            for s in range(self.mdp.env.nS):
                # The best action we would take under the currect policy
                chosen_a = np.argmax(policy[s])
            
                # Find the best action by one-step lookahead
                # Ties are resolved arbitarily
                action_v = np.zeros(self.mdp.env.nA)
                for a in range(self.mdp.env.nA):
                    for trans_prob, next_state, reward, done in  self.mdp.env.P[s][a]:
                        #action_v[a] += trans_prob * (reward + self.gamma * V[next_state])
                        action_v[a] += trans_prob *  V[next_state]
                best_a = np.argmax(action_v)
            
                # Greedily update the policy
                if chosen_a != best_a:
                    policy_stable = False
                policy[s] = np.eye(self.mdp.env.nA)[best_a]
            niteration += 1
            # If the policy is stable we've found an optimal policy. Return it
            if policy_stable:
                print(niteration)
                print(V.reshape(self.mdp.env.shape))
                print(policy.reshape([self.mdp.env.nS, self.mdp.env.nA]))
                return policy, V
        '''