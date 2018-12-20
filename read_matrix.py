#!/usr/bin/env python
# encoding: utf-8

"""
Read matrix
"""

__author__ = 'Aazim'

from numpy import genfromtxt
import numpy

matrix = genfromtxt('file.csv', delimiter=',')
n_matrix = 3 * matrix
n_matrix = n_matrix.astype(int)
print(n_matrix)
numpy.savetxt("n_file.csv", n_matrix, fmt='%i', delimiter=',')