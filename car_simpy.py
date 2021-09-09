import simpy

def car(env):
    while True:
        print('Start parking at %d' % env.now)
        parking_duration = 10
        yield env.timeout(parking_duration)

        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)

env  = simpy.Environment()
env.process(car(env))

env.run(until=30)