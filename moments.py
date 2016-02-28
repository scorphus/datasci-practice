import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp

values = np.random.normal(100, 0.5, 10000)

mu = values.mean()
median = np.median(values)
sigma = values.std()  # Standard Deviation
var = np.var(values)  # Variance
skewness = sp.skew(values)
kurtosis = sp.kurtosis(values)

info = r'''$\mu=%.5f$
$\tilde x=%.5f$
$\sigma=%.5f$
$\sigma^2=%.5f$
$\gamma_i=%.5f$
$\mathit{Kurt}=%.5f$''' % (mu, median, sigma, var, skewness, kurtosis)

print info

fig, sp = plt.subplots(1)
sp.hist(values, 50)
sp.set_title('Moments of Normal Distribution')

sp.text(
    x=0.05,
    y=0.94,
    s=info,
    transform=sp.transAxes,
    fontsize=14,
    verticalalignment='top',
    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5),
)

plt.show()
