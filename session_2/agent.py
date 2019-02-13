import numpy as np
from scipy.special import gamma

np.random.seed()
"""
Contains the definition of the agent that will run in an
environment.
"""

class RandomAgent:
    def __init__(self):
        """Init a new agent.
        """

    def choose(self):
        """Acts given an observation of the environment.

        Takes as argument an observation of the current state, and
        returns the chosen action.
        """
        return np.random.randint(0, 10)

    def update(self, action, reward):
        """Receive a reward for performing given action on
        given observation.

        This is where your agent can learn.
        """
        pass

class epsGreedyAgent:
    def __init__(self):
        self.A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.mu = np.zeros(len(self.A))
        self.optimal_mu = 0
        self.draws = np.zeros(len(self.A))
        self.epsilon = 0.0

    def choose(self):

        self.optimal_mu = np.argmax(self.mu)
        random = np.random.randn()
        if random < self.epsilon:
            return np.random.randint(0, len(self.A))
        else:
            return self.optimal_mu

    def update(self, action, reward):

        self.draws[action] += 1
        self.mu[action] = ((self.draws[action]-1)*self.mu[action] + reward)/self.draws[action]

class UCBAgent:
    # https://homes.di.unimi.it/~cesabian/Pubblicazioni/ml-02.pdf
    def __init__(self):
        self.A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.mu = np.zeros(10)
        self.optimal_mu = 0
        self.draws = np.zeros(10)

    def choose(self):
        # Compute bounds
        n = np.sum(self.draws)
        bounds = self.mu + np.sqrt(2*np.log(n)/self.draws)

        self.optimal_policy = np.argmax(bounds)

        return self.optimal_policy

    def update(self, action, reward):

        self.draws[action] += 1
        self.mu[action] = ((self.draws[action]-1)*self.mu[action] + reward)/self.draws[action]


class BesaAgent(epsGreedyAgent):
    # https://hal.archives-ouvertes.fr/hal-01025651v1/document
    def __init__(self):
        self.A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.mu = np.zeros(10)
        self.draws_rewards = [[] for i in range(10)]

    def choose(self):
        # A changer: passer le calcul de mu_hat ici
        # D'abord, tirer tous les bras qu'on a encore jamais tire
        # Puis faire le calcul "classique"

        N_per_actions = [len(draws_per_action) for draws_per_action in self.draws_rewards]
        min_arm, min_arm_len = np.argmin(N_per_actions), np.min(N_per_actions)

        if min_arm_len == 0:
            # print('explore arm no', min_arm)
            return min_arm
        else:
            for temp_action in self.A:
                random_draw_per_action = np.random.choice(N_per_actions[temp_action], min_arm_len,
                                                          replace=False)
                self.mu[temp_action] = np.mean(np.array(self.draws_rewards[temp_action\
                                                      ])[random_draw_per_action])
                # print('compute mu: {}\n try arm: {}'.format(self.mu, np.argmax(self.mu)))
            return np.argmax(self.mu)

    def update(self, action, reward):

        # Add new observation in list associated to action
        self.draws_rewards[action].append(reward)


class SoftmaxAgent:
    # https://www.cs.mcgill.ca/~vkules/bandits.pdf

    def __init__(self):
        self.A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.tau = float(0.01) # hyperparameter

        self.mu = np.ones(len(self.A))/len(self.A) # initialized mu at uniform random
        self.draws = np.zeros(len(self.A)) # number of times each arm is drawn

    def choose(self):

        p = (np.exp(self.mu)/self.tau)/np.sum((np.exp(self.mu)/self.tau))
        return np.argmax(p)


    def update(self, action, reward):
        # Update mu(action) with moving mean
        self.draws[action] += 1
        self.mu[action] = ((self.draws[action]-1)*self.mu[action] + reward)/self.draws[action]


class ThompsonAgent:
    # https://en.wikipedia.org/wiki/Thompson_sampling
    """ We will implement Bernouilli Thompson Agent (from ```A Tutorial on Thompson Sampling```,
        Daniel J. Russo)"""

    def __init__(self):
        self.A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.alpha = np.ones(len(self.A))*1e-4
        self.beta = np.ones(len(self.A))*1e-4

    def choose(self):
        # Compute probability of theta with beta distribution
        p = np.random.beta(self.alpha, self.beta)

        return np.argmax(p)


    def update(self, action, reward):
        print(self.alpha, self.beta)
        # Update alpha, beta
        self.alpha[action] += reward
        self.beta[action] += (1 - reward)

        print(self.alpha, self.beta)


class KLUCBAgent:
    # See: https://hal.archives-ouvertes.fr/hal-00738209v2
    def __init__(self):
        self.A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def choose(self):
        raise NotImplemented

    def update(self, action, reward):
        raise NotImplemented

# Choose which Agent is run for scoring
Agent = BesaAgent
