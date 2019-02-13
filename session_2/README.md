# Bandits algorithms, Practical session 2
In this second practical, you are asked to put what you just learnt
about bandits to good use. You are provided with the `main.py` file,
a bandits test bed. Use `python main.py -h` to check how you are
supposed to use this file.

You will implement:
* Epsilon-greedy bandit
* Besa https://hal.archives-ouvertes.fr/hal-01025651v1/document
* UCB https://homes.di.unimi.it/~cesabian/Pubblicazioni/ml-02.pdf
* softmax https://www.cs.mcgill.ca/~vkules/bandits.pdf
* Thompson sampling Agent https://en.wikipedia.org/wiki/Thompson_sampling

Bonus for:
* KL UCB https://hal.archives-ouvertes.fr/hal-00738209v2


**You need to choose which agent to use by modifying the last line of `agent.py`**

## How do I complete these files ?
Remove the expection raising part, and
complete the three blank methods for each Agent.

In `__init__`, build the buffers your agent requires.
It might be interesting, for instance, to store the
number of time each action has been selected.

In `choose`, prescribe how the agent selects its
actions (interact must return an action, that is
an index in [0, ..., 9]).

Finally, in update, implement how the agent updates
its buffers, using the newly observed `action` and `reward`.

**You need to choose which agent to use by modifying the last line of `agent.py`**

## Challenge your friends
You are required to have a codalab account (https://codalab.lri.fr).
Please use an username in the format of *firstname.lastname* when creating your account.
You can enter to the competition here https://codalab.lri.fr/competitions/328

For submission, you need to zip `agent.py` and `metadata` files then submit the zipped file to codalab.
`baseline.zip` as an example of submission.


For further questions, please use the codalab forum.

## Grading
* 2/3: implementation of the 5 agents
* 1/3: rank on the competition (by tuning hyperparameter)


Only the last submission is considered for grading (agent implementation) and ranking (challenge).
