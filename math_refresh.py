# -*- coding: utf-8 -*-
"""math refresh.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nx9lz1py0Vv3nkFZDACyNZtj61XQlcL4
"""

import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
import matplotlib

randnums = np.random.rand(100)
randnums2 = np.random.rand(100)
mean = np.mean(randnums)
mode = stats.mode(randnums)
std = np.std(randnums)
mad = stats.median_absolute_deviation(randnums)
var = np.var(randnums)
pearsonr = stats.pearsonr(randnums, randnums)
pearsonr2 = stats.pearsonr(randnums, randnums2)
spearmanr = stats.spearmanr(randnums, randnums)
spearmanr2 = stats.spearmanr(randnums, randnums2)
log = np.log(randnums)
exp = randnums**2
exp2 = 2**randnums
summ = sum(randnums)
z = randnums + randnums2
x = randnums.reshape(-1,1)
z = z.reshape(-1,1)
regression = LinearRegression().fit(x,z)
regScore = regression.score(x,z)

print("100 random numbers = " + str(randnums) + "\n")
print("mean = " + str(mean) + "\n")
print("mode = " + str(mode) + "\n")
print("standard deviation = " + str(std) + "\n")
print("MAD = " + str(mad) + "\n")
print("Variance = " + str(var) + "\n")
print("Correlation 1 = " + str(pearsonr) + "\n")
print("Correlation 2 = " + str(pearsonr2) + "\n")
print("Rank Correlation 1 = " + str(spearmanr) + "\n")
print("rank Correlation 2 = " + str(spearmanr2) + "\n")
print("Log = " + str(log) + "\n")
print("exp = " + str(exp) + "\n")
print("exp2 = " + str(exp2) + "\n")
print("Summ = " + str(summ) + "\n")
print("Regression = " + str(regScore) + "\n")

print("scatter plot")
matplotlib.pyplot.scatter(randnums, randnums2)