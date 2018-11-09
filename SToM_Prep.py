#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:40:17 2018

@author: sophie
"""

import numpy as np
import matplotlib.pyplot as plt
import STOM_higgs_tools as tools

data = tools.generate_data()
# Each list entry represents the rest mass reconstructed from a collision

# Generate histogram data
bin_heights, bin_edges = np.histogram(data, bins=30, range=(104,155))
bin_centers = 0.5*(bin_edges[1:]+bin_edges[:-1])
mean_std = np.sqrt(bin_heights) # Using Poisson error sqrt for the height
widths = bin_edges[1:]-bin_edges[:-1]

# Plotting data with 30 bins
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(8,15), sharex = True)
ax1.bar(bin_centers, bin_heights, width=widths, color='orange', 
        yerr=mean_std, error_kw=dict(elinewidth=0.5,ecolor='black'))
ax1.set_title('Bins = 30')
ax1.set_ylabel('Number of entries')
ax1.set_xlabel('Mass (GeV)')

# Plotting with 300 bins
bin_heights2, bin_edges2 = np.histogram(data, bins=300, range=(104,155))
bin_centers2 = 0.5*(bin_edges2[1:]+bin_edges2[:-1])
mean_std2 = np.sqrt(bin_heights2) # Using Poisson error sqrt for the height
widths2 = bin_edges2[1:]-bin_edges2[:-1]

ax2.bar(bin_centers2, bin_heights2, width=widths2, color='blue', 
        yerr=mean_std2, error_kw=dict(elinewidth=0.5,ecolor='black'))
ax2.set_title('Bins = 300')
ax2.set_ylabel('Number of entries')
ax2.set_xlabel('Mass (GeV)')
plt.show()

plt.figure()
plt.subplot(2,1,1)
plt.errorbar(bin_centers, bin_heights, yerr=mean_std, xerr=widths,
             fmt='.', ecolor='black', elinewidth=0.5, capsize=1)
plt.ylabel('Number of entries')
plt.xlabel('Mass (Gev)')

# Defining exponential decay
def exp_dist(x, A, lamb):
    B = A*np.exp(-x/lamb)
    return B

# Generate histogram data for masked data
data_arr = np.array(data)
data_filtered = np.ma.masked_where(data_arr > 120, data_arr).compressed() # Mask data which is greater than 120MeV
bin_heights_masked, bin_edges_masked = np.histogram(data_filtered, bins=30, 
                                                    range=(104,155))
bin_centers_masked = 0.5*(bin_edges_masked[1:]+bin_edges_masked[:-1])
mean_std_masked = np.sqrt(bin_heights_masked) # Using Poisson error sqrt for the height
widths_masked = bin_edges_masked[1:]-bin_edges_masked[:-1]

plt.subplot(2,1,2)
plt.errorbar(bin_centers_masked, bin_heights_masked, yerr=mean_std_masked, xerr=widths_masked,
             fmt='.', ecolor='black', elinewidth=0.5, capsize=1)
plt.ylabel('Number of entries')
plt.xlabel('Mass (Gev)')

# Determining the value of lambda and A
# Lambda is 1/mean value

lamb = 1/np.mean(data)
print(1/lamb)
