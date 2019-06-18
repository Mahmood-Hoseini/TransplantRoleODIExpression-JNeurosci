#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 17:37:12 2017

@author: Mahmood Hoseini
"""

import numpy as np
import scipy.io

from utils import plot_ODI          
from utils import plot_fr_vs_depth
from utils import plot_ODI_CDF
from utils import plot_ODI_PDF
from utils import plot_fr
from utils import plot_cell_density
from utils import plot_ISI    
from utils import plot_dODI_vs_depth
    
def chan_depth_um (chans):
    emap = np.array([1025,925,825,725,625,525,425,325,225,125,25,50,100,150,200,250,1050,1000,950,900,850,800,750, 
                     700,650,600,550,500,450,400,350,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,
                     1050,300,250,200,150,100,50,0,75,175,275,375,475,575,675,775,875,975,
                     1025,925,825,725,625,525,425,325,225,125,25,50,100,150,200,250,1050,1000,950,900,850,800,750,
                     700,650,600,550,500,450,400,350,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,
                     1050,300,250,200,150,100,50,0,75,175,275,375,475,575,675,775,875,975]);
      
    depths = np.zeros(np.shape(chans));
    for ii in range(len(chans[0, :])) :
        depths[0, ii] = 1050 - emap[chans[0, ii]-1]
        
    return depths

filename='/Users/idl/Desktop/Gad2;Ai40-workspace.mat' # Fig.5
#filename='/Users/idl/Desktop/Gad2;Ai32-workspace.mat' # Fig.6
#filename='/Users/idl/Desktop/Ctrl-workspace.mat' # Fig.2D-I

dic = scipy.io.loadmat(filename)

target_pva_bs = 0.0292
target_pva_ns = 0.055

plot_ODI(dic['odi_bs'], dic['pva_bs'], 'm', target_pva_bs, 'BS')
plot_ODI(dic['odi_ns'], dic['pva_ns'], 'c', target_pva_ns, 'NS')

plot_ODI_CDF (dic['odi_bs'], 'm', 100, 'BS')
plot_ODI_CDF (dic['odi_ns'], 'b', 100, 'NS')

plot_ODI_PDF (dic['odi_bs'], 'm', 20, 'BS')
plot_ODI_PDF (dic['odi_ns'], 'b', 20, 'NS')

plot_dODI_vs_depth(dic['odi_bs'], dic['depth_bs'], dic['pva_bs'], 'm', target_pva_bs, 'BS')
plot_dODI_vs_depth(dic['odi_ns'], dic['depth_ns'], dic['pva_ns'], 'b', target_pva_ns, 'NS')

plot_fr(dic['frm_bs'], dic['pva_bs'], 'm', target_pva_bs, 'BS')
plot_fr(dic['frm_ns'], dic['pva_ns'], 'b', target_pva_ns, 'NS')

plot_fr_vs_depth(dic['frp_bs'], dic['depth_bs'], dic['pva_bs'], 'm', target_pva_bs, 'BS')
plot_fr_vs_depth(dic['frp_ns'], dic['depth_ns'], dic['pva_ns'], 'c', target_pva_ns, 'NS')

plot_ISI('Gad2;Ai32') # Fig.1B
plot_cell_density('Gad2;Ai40') # Fig.1D
