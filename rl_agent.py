import numpy as np
import random

def route_optimization(distance, fuel):

    actions = ["Truck", "Rail", "Air"]

    Q = np.zeros((3,3))

    for _ in range(100):
        state = random.randint(0,2)
        action = random.randint(0,2)

        reward = -(distance * 0.1 + fuel * 0.05) - action*50

        Q[state, action] += 0.1 * (reward + 0.9*np.max(Q[action,:]) - Q[state, action])

    best_action = actions[np.argmax(Q[0])]
    return best_action