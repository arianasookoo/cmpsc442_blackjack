import gymnasium as gym 
env = gym.make('Blackjack-v1', natural=False, sab=False, render_mode="human")
# implement a Q-learning algorithm
# initializing the Q(s,a) table for all possible values of s and a
# print out whether the bot won or lost in each episode and the total win rate