#!/usr/bin/env python
# coding=utf-8
'''
Author: John
Email: johnjim0816@gmail.com
Date: 2020-10-30 15:39:37
LastEditor: John
LastEditTime: 2021-03-17 20:19:14
Discription: 
Environment: 
'''

import gym
from A2C.multiprocessing_env import SubprocVecEnv

# num_envs = 16
# env = "Pendulum-v0"

def make_envs(num_envs=16,env="Pendulum-v0"):
    ''' 创建多个子环境
    '''
    num_envs = 16
    env = "CartPole-v0"
    def make_env():
        def _thunk():
            env = gym.make(env)
            return env

        return _thunk

    envs = [make_env() for i in range(num_envs)]
    envs = SubprocVecEnv(envs)
    return envs
# if __name__ == "__main__":

#     num_envs = 16
#     env = "CartPole-v0"
#     def make_env():
#         def _thunk():
#             env = gym.make(env)
#             return env

#         return _thunk

#     envs = [make_env() for i in range(num_envs)]
#     envs = SubprocVecEnv(envs)
if __name__ == "__main__":
    envs = make_envs(num_envs=16,env="CartPole-v0") 