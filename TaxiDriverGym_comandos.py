import gym
env = gym.make("Taxi-v3").env

state = env.reset()
s = env.decode(state)
taxi_row, taxi_col, pass_idx, dest_idx = s


c = env.desc[1:-1]
taxi_col_r = (taxi_col*2)+1
 
print(c)
env.render()
print(taxi_row, taxi_col, pass_idx, dest_idx)
print(c[taxi_row][taxi_col_r].decode("utf-8") )

state, reward, done, info = env.step(4)
s = env.decode(state)
taxi_row, taxi_col, pass_idx, dest_idx = s
taxi_col_r = (taxi_col*2)+1
print(taxi_row, taxi_col, pass_idx, dest_idx)
print(c[taxi_row][taxi_col_r].decode("utf-8") )

env.render()

# The filled square represents the taxi, which is yellow without a passenger and green with a passenger.
# The pipe ("|") represents a wall which the taxi cannot cross.
# R, G, Y, B are the possible pickup and destination locations. The blue letter represents the current 
# passenger pick-up location, and the purple letter is the current destination.

# actions:
# 0 = south
# 1 = north
# 2 = east
# 3 = west
# 4 = pickup
# 5 = dropoff


