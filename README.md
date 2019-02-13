# Reinforcement Learning, Practical Session
This repository stores the code in the course of reinforcement learning for Master AIC of University Paris-Saclay.

# Introduction and set-up
For all practicals, we will make heavy use of python and many of its
libraries. To have access to the full power of python, virtual environments
and the command line, it is recommended to have access to a Unix system, an
emulated terminal (Windows 10 gives you access to such a terminal, or even anaconda), or a
Virtual Machine.

Besides, we advice you to use conda to manage the various requirements that may
change from one practical to the other. Conda can be installed following [this
link](https://conda.io/docs/install/quick.html). Install the latest python 3
version of conda. Once conda is installed, before working on a practical, you
should create a new conda environment. For example for the second practical,
execute `conda create -n practical1`. You can then access your new environment
using `source activate practical1`. Each of the practical provides you with a
`requirements.txt` file. You can install all the necessary requirements by
running `pip install -r requirements.txt` in your virtual environment.
