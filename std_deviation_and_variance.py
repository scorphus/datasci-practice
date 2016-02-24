import numpy as np

incomes = np.random.normal(100.0, 50.0, 10000)
N = len(incomes)

my_mean = sum(incomes) / N
variance = sum([np.power(x - my_mean, 2) for x in incomes]) / N
print variance

var = incomes.var()
print var

std_deviation = np.sqrt(variance)
print std_deviation

std = incomes.std()
print std
