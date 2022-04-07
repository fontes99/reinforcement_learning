from Taxi import MeuTaxi
import SearchAlgorithms as sa
import gym

def makeMap(desc):
    city = []

    for idx, row in enumerate(desc):
        new_row = []
        
        if idx in [0, (len(desc)-1)]:
            continue
        
        for idx_col, v in enumerate(row):
            
            if idx_col in [0, len(row)-1]:
                continue
            
            new_row.append(v.decode("utf-8"))
        
        city.append(new_row)

    return city

def testeSeed1():
    env = gym.make("Taxi-v3").env
    state = env.reset(seed=1)
    env.render()

    city = makeMap(env.desc)

    taxi = MeuTaxi(city, env.decode(state), '')
    assert taxi.path() == [2, 0, 0, 4, 1, 1, 3, 3, 1, 3, 1, 5]

def testeSeed2():
    env = gym.make("Taxi-v3").env
    state = env.reset(seed=2)
    env.render()

    city = makeMap(env.desc)

    taxi = MeuTaxi(city, env.decode(state), '')
    assert taxi.path() == [0, 3, 0, 0, 4, 1, 1, 1, 1, 5]

def testeSeed3():
    env = gym.make("Taxi-v3").env
    state = env.reset(seed=3)
    env.render()

    city = makeMap(env.desc)

    taxi = MeuTaxi(city, env.decode(state), '')
    assert taxi.path() == [0, 0, 3, 1, 3, 1, 4, 0, 0, 0, 0, 5]

def testeSeed14():
    env = gym.make("Taxi-v3").env
    state = env.reset(seed=14)
    env.render()

    city = makeMap(env.desc)

    taxi = MeuTaxi(city, env.decode(state), '')
    assert taxi.path() == [1, 1, 2, 2, 2, 0, 0, 4, 1, 1, 3, 3, 1, 3, 1, 5]

def testeSeed5122018():
    env = gym.make("Taxi-v3").env
    state = env.reset(seed=5122018)
    env.render()

    city = makeMap(env.desc)

    taxi = MeuTaxi(city, env.decode(state), '')
    assert taxi.path() == [3, 1, 3, 3, 1, 3, 1, 4, 2, 0, 0, 2, 2, 0, 0, 5]
