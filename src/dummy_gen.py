import numpy as np
import random
import datetime

all_pilots = ['atushi', 'Saqoosha', 't.oka', 'inoue', 'masap']
num_heats = 4


for heat in range(1, num_heats+1):
    with open('../data/heat{}.csv'.format(heat), 'w') as f:
        for p in np.random.choice(all_pilots, 3, replace=False):
            l1 = random.uniform(25.0, 35.0)
            l2 = random.uniform(25.0, 35.0)
            l3 = random.uniform(25.0, 35.0)
            l4 = random.uniform(25.0, 35.0)
            total = l1+l2+l3+l4
            timestamp = int(datetime.datetime.now().timestamp())
            data = [p]
            data.extend([f'{t:.03f}' for t in [l1, l2, l3, l4, total]])
            data.extend([timestamp, heat])
            f.write(','.join([str(d) for d in data]))
            f.write('\n')
