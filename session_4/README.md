# Evolutionary RL, Practical session 4

In this practical, we are asked to put what we learnt
about direct policy search. 


In this project, we solved the classic Mountain Car (https://gym.openai.com/envs/MountainCar-v0/). For more details about action and observation space, please refer to the OpenAI
documentation here: https://github.com/openai/gym/wiki/MountainCar-v0


![](mountain_car.gif)


## How do I proceed ?

we are going to implement direct policy search algorithm using evolutionary computation (CMA-ES).
The running of your agent follows a general procedure:
1. Train the agent using CMA-ES in `train` method
2. Test and score the final agent using `act` method

We are in the setting of model free approach (Pg 10. https://www.lri.fr/~sebag/Slides/RL_DPS.pdf).

In order to efficienlty train your agent, we must (ref. pg 42 of Michèle's slides):
* Define the search space (policy space in which we are willing to search for)
* Define the objective function: to assess a policy (Episode-based or step based)
* Optimize the objective using cma-es: use https://pypi.org/project/cma/
