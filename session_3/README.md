# Function approximation, Practical session 3
*This project is adapted from Guillaume Charpiat and Victor Berger courses at École Centrale*


In this third practical, I was asked to implement the algo about function approximation. The `main.py` file is provided. Use `python main.py -h` to check how to use this file.


In this project, we are going to solve the classic Pendulum problem (https://gym.openai.com/envs/Pendulum-v0/).
Unlike previous environment, the state and action space are both continuous so that we need to approximate
the Q values Q(s, a). For more details about action and observation space, refer to the OpenAI
documentation here: https://github.com/openai/gym/wiki/Pendulum-v0


![](pendulum.gif)


## How do I complete these files ?

The running of your agent follows a general procedure that will be shared
for all later practicals:
* The environment generates an observation
* This  observation  is  provided  to  the  agent  via  the
act method  which chooses an action
* The environment processes the action to generate a reward
* this reward is given to the agent in the
reward method, in which the agent will learn from the reward

This 4-step process is then repeated several times.
