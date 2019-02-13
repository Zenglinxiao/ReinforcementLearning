# Function approximation, Practical session 3
*This project is adapted from Guillaume Charpiat and Victor Berger courses at École Centrale*


In this third practical, you are asked to put what you just learnt
about function approximation. You are provided with the `main.py` file. Use `python main.py -h` to check how you are supposed to use this file.


In this project, you are asked to solve the classic Pendulum problem (https://gym.openai.com/envs/Pendulum-v0/).
Unlike previous environment, the state and action space are both continuous so that you need to approximate
the Q values Q(s, a). For more details about action and observation space, please refer to the OpenAI
documentation here: https://github.com/openai/gym/wiki/Pendulum-v0


![](pendulum.gif)


## How do I complete these files ?
The  template  is  a  zip  file  that  you  can  download  on  the  course  website.   It
contains several files, two of them are of interest for you:
agent.py and main.py .agent.py is the file in which you will write the code of your agent,  using
the RandomAgent class as a template.  Don’t forget to read the documentation
it contains.  As usual you can have the code of your several
agents in the same file, and use the final line `Agent = MyAgent` to choose which agent you want to run.

The running of your agent follows a general procedure that will be shared
for all later practicals:
* The environment generates an observation
* This  observation  is  provided  to  your  agent  via  the
act method  which chooses an action
* The environment processes your action to generate a reward
* this reward is given to your agent in the
reward method, in which your agent will learn from the reward

This 4-step process is then repeated several times.

You can to start by implementing approximate Q-learning and its generalization TD(\lambda)


## Challenge your friends
You are required to have a codalab account (https://codalab.lri.fr).
Please use an username in the format of *firstname.lastname* when creating your account.
You can enter to the competition here https://codalab.lri.fr/competitions/342

For submission, you need to zip `agent.py` and `metadata` files then submit the zipped file to codalab.
`baseline.zip` as an example of submission.

If you want to reproduce your local score on Codalab, please use the docker image (https://cloud.docker.com/u/herilalaina/repository/docker/herilalaina/rlaic) and do not change the seed.
Then run `python main.py --ngames 1000 --niter 1500 --batch 10`

For further questions, please use the codalab forum.

## Grading
* 3/4: Agent implementation
* 1/4: rank on the competition


Only the last submission is considered for grading (agent implementation) and ranking (challenge).
