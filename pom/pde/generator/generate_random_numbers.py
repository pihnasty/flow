import numpy as np


def uniform_proposal(x, delta=2.0):
    return np.random.uniform(x - delta, x + delta)

def metropolis_sampler(p, nsamples, proposal=uniform_proposal):
    x = 1 # start somewhere

    for i in range(nsamples):
        trial = proposal(x) # random neighbour from the proposal distribution
        acceptance = p(trial)/p(x)

        # accept the move conditionally
        if np.random.uniform() < acceptance:
            x = trial
        print(x)
        yield x

def gaussian(x, mu, sigma):
    return 1./sigma/np.sqrt(2*np.pi)*np.exp(-((x-mu)**2)/2./sigma/sigma)

p = lambda x: gaussian(x, 1, 0.3) + gaussian(x, -1, 0.1) + gaussian(x, 3, 0.2)
samples = list(metropolis_sampler(p, 10))
print(samples)
