#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Use PyLab to calculate – by hand, aka the hard way – the covariance between two
NumPy-generated random vars and show a scatter plot of the data with MatPlotLib
'''

import numpy
import sys

from matplotlib import pyplot
from pylab import dot, mean


def dev_mean(v):
    'Calculate the deviation from the mean'
    mean_v = mean(v)
    return [x - mean_v for x in v]


def covariance(x, y):
    'Calculate the covariance using vector product of deviations from mean'
    return dot(dev_mean(x), dev_mean(y)) / (len(x) - 1)


def correlation(x, y):
    'Calculate the correlation between x and y'
    try:
        stddevx = x.std()
        stddevy = y.std()
    except AttributeError:
        stddevx = numpy.std(x)
        stddevy = numpy.std(y)
    return covariance(x, y) / stddevx / stddevy  # What if ZeroDivisionError?


A = numpy.random.normal(3.0, 1.0, 1000)
B = numpy.random.normal(50.0, 10.0, 1000)

print('Covariance of randomness is: %f' % covariance(A, B))
print('Correlation of randomness is: %f' % correlation(A, B))
print('Correlation of randomness is by NumPy: %f' % numpy.corrcoef(A, B)[1][0])

X = range(-5, 6)
Y = [n * 2 for n in X]
P_dev = dot(dev_mean(X), dev_mean(Y))

print('X: %s\nY: %s' % (X, Y))

print(u'X ● Y = %f' % dot(X, Y))
print(u'dev_mean(X) ● dev_mean(Y) = %f' % P_dev)
print(u'dev_mean(X) ● dev_mean(Y) / %d = %f' % (len(X) - 1, (P_dev / (len(X) - 1))))
print('covariance(X, Y) = %f' % covariance(X, Y))
print('correlation(X, Y) = %f' % correlation(X, Y))
print('numpy.corrcoef(X, Y) = %f' % numpy.corrcoef(X, Y)[1][0])

if '--plot' in sys.argv:
    print('Plotting scatter plots...')
    pyplot.scatter(A, B)
    pyplot.show()
    pyplot.scatter(X, Y)
    pyplot.show()
