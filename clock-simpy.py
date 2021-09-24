import simpy

def clock(env, name, tick):
        while True:
            print(name, env.now)
            yield env.timeout(tick)

env = simpy.Environment()
env.process(clock(env, 'fast', 0.5))
env.process(clock(env, 'slow', 1))
env.run(until=2)

# OUTPUT:
# fast 0
# slow 0  
# fast 0.5
# slow 1  
# fast 1.0
# fast 1.5


