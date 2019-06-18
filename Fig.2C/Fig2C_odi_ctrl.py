#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 10:41:07 2018

@author: mhoseini
"""

import numpy as np
import scipy.io
import pylab
import seaborn as sns

bpath = '/Users/idl/Desktop/Fig.2C/'; # set your base path
paths = ['20181220-green-01',
         '20181220-green-02',
         '20181220-magenta-01',
         '20181220-magenta-02',
         '20181221-blue-01',
         '20181221-blue-02']

odi_bs = np.zeros((0,1)); odi_ns = np.zeros((0,1));
for ii, path in enumerate(paths):
    WS = scipy.io.loadmat(path + '-Workspace.mat');
    ODI = scipy.io.loadmat(path + '-ODI.mat');
    
    for ind in range(len(ODI['odis'])):
        if all(~np.isnan(ODI['odis'][ind])):
            if ODI['tags'][ind][0] == 69:
                odi_bs = np.concatenate((odi_bs, np.reshape(ODI['odis'][ind], (1,1))), axis=0)
            elif ODI['tags'][ind][0] == 73:
                odi_ns = np.concatenate((odi_ns, np.reshape(ODI['odis'][ind], (1,1))), axis=0)


pylab.style.use('seaborn-bright')
size = [3.5, 3.5]
fig = pylab.figure(figsize=size)
ax = fig.add_axes([0.25, 0.2, 0.7, 0.75])
#ax.grid(True, which='both')
bins = np.linspace(-1, 1, 10);
n, bins, patches = ax.hist(odi_bs, bins=bins, histtype='stepfilled', alpha=0.7)
pylab.setp(patches, 'facecolor', [1,0,1], 'edgecolor', [1,0,1])
n, bins, patches = ax.hist(odi_ns, bins=bins, histtype='stepfilled', alpha=0.7)
pylab.setp(patches, 'facecolor', [0,1,1], 'edgecolor', [0,1,1])
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_ylim([0, 50])
ax.set_yticks([0,10,20,30,40])
ax.set_ylabel('Counts')
ax.set_xlabel('Ocular Dominance Index')
sns.set_style("ticks")
sns.despine(offset=5, trim=True)

fig.set_size_inches(size)
fig.savefig(bpath + 'Fig-2C.pdf', dpi=900)