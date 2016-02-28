import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import binom, expon, norm, poisson

fig = plt.figure()
fig.suptitle('Probability Density Functions')

values = np.random.uniform(-10.0, 10.0, 100000)
sp1 = fig.add_subplot(321)
sp1.hist(values, 50)

x = np.arange(-3, 3, 0.001)
sp2 = fig.add_subplot(322)
sp2.plot(x, norm.pdf(x))

mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
sp3 = fig.add_subplot(323)
sp3.hist(values, 50)

x = np.arange(0, 10, 0.001)
sp4 = fig.add_subplot(324)
sp4.plot(x, expon.pdf(x))

n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
sp5 = fig.add_subplot(325)
sp5.plot(x, binom.pmf(x, n, p))

mu = 500
x = np.arange(400, 600, 0.5)
sp6 = fig.add_subplot(326)
sp6.plot(x, poisson.pmf(x, mu))

plt.show()
