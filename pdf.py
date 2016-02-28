import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import binom, expon, norm, poisson

fig = plt.figure()
fig.suptitle('Probability Density Functions')

values = np.random.uniform(-10.0, 10.0, 100000)
sp1 = fig.add_subplot(321)
sp1.hist(values, 50)
sp1.set_title('Uniform')

x = np.arange(-3, 3, 0.001)
sp2 = fig.add_subplot(322)
sp2.plot(x, norm.pdf(x))
sp2.set_title('Normal')

mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
sp3 = fig.add_subplot(323)
sp3.hist(values, 50)
sp3.set_title('Normal (random)')

x = np.arange(0, 10, 0.001)
sp4 = fig.add_subplot(324)
sp4.plot(x, expon.pdf(x))
sp4.set_title('Exponential ("Power Law")')

n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
sp5 = fig.add_subplot(325)
sp5.plot(x, binom.pmf(x, n, p))
sp5.set_title('Binomial')

mu = 500
x = np.arange(400, 600, 0.5)
sp6 = fig.add_subplot(326)
sp6.plot(x, poisson.pmf(x, mu))
sp6.set_title('Poisson')

plt.show()
