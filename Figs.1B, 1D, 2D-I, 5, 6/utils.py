#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:08:34 2018

@author: mhoseini
"""
import numpy as np
import pylab
import seaborn as sns
from scipy.stats import ranksums
from mpl_toolkits.axes_grid1 import make_axes_locatable

display_settings = {
        'suptitle_font_size':13,
        'axis_label_font_size':12,
        'plot_titles_font_size':12,
        'left_fig_padding':0.2,
        'top_fig_padding':0.12,
        'bottom_fig_padding':0.18,
        'right_fig_padding':0.03,
        'marker_size':2,
        'axis_linewidth':0.5
        }
suptit_fontsize = display_settings['suptitle_font_size']
plot_titles_font_size = display_settings['plot_titles_font_size']
ticklabel_fontsize = display_settings['axis_label_font_size']
top_plot_titles_y = 0.95
bottom_plot_titles_y = 0.5
left_fig_padding = display_settings['left_fig_padding']
top_fig_padding = display_settings['top_fig_padding']
bottom_fig_padding = display_settings['bottom_fig_padding']
right_fig_padding = display_settings['right_fig_padding']
axis_linewidth= display_settings['axis_linewidth']   
  
target_pval = 0.05; 
saveflag = True;

def savefig(fig, flag, size, name) :
    if flag == True :
        savepath = '/Users/idl/Desktop/ODI-' + name 
        fig.set_size_inches(size)
        fig.savefig(savepath + '.pdf', dpi=900)
    else :
        pylab.show()
        
def plot_ODI (odis, pvals, colstr, target_pval, name, alpha=1) :
    
    pylab.style.use('classic')
    size = [4, 4]
    fig = pylab.figure(figsize=size)
    ax = fig.add_axes([left_fig_padding, bottom_fig_padding, 1-left_fig_padding, 1-bottom_fig_padding])
    
    for ind in range(np.shape(odis)[0]):
        if min(pvals[ind, :]) > target_pval:
            col = [0.8, 0.8, 0.8]
            ax.plot(odis[ind,0], odis[ind,1], 'o', mec=col, mfc=col, mew=1, markersize=4, alpha=alpha)
    for ind in range(np.shape(odis)[0]):
        if min(pvals[ind, :]) < target_pval:
            ax.plot(odis[ind,0], odis[ind,1], 'o', mec=colstr, mfc=colstr, mew=1, markersize=4, alpha=alpha)
            
    ax.set_xlim([-1.05, 1.05])
    ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax.set_ylim([-1.05, 1.05])
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.set_ylabel('ODI light on', fontsize=ticklabel_fontsize)
    ax.set_xlabel('ODI light off', fontsize=ticklabel_fontsize)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.plot([-1.05, 1.05], [-1.05, 1.05], ls="--", c=".3")
    sns.set_style("ticks")
    sns.despine(offset=5, trim=True)
    for tick in ax.yaxis.get_major_ticks() :
        tick.label.set_fontsize(12)
        
    divider = make_axes_locatable(ax)
    axx = divider.append_axes("top", 0.8, pad=0.0, sharex=ax)
    axy = divider.append_axes("right", 0.8, pad=0.0, sharey=ax)
    
    bins = np.linspace(-1, 1, 8);
    n, bins, patches = axx.hist(odis[:, 0], bins=bins, histtype='stepfilled')
    pylab.setp(patches, 'facecolor', colstr, 'edgecolor', colstr)
    axx.spines['right'].set_visible(False)
    axx.spines['top'].set_visible(False)
    axx.xaxis.set_ticks_position('bottom')
    axx.yaxis.set_ticks_position('left')
    
    n, bins, patches = axy.hist(odis[:, 1], bins=bins, histtype='stepfilled', orientation='horizontal')
    pylab.setp(patches, 'facecolor', 'g', 'edgecolor', 'g')
    axy.spines['right'].set_visible(False)
    axy.spines['top'].set_visible(False)
    axy.xaxis.set_ticks_position('bottom')
    axy.yaxis.set_ticks_position('left')
    savefig(fig, saveflag, size, name)


def plot_deltaODI (odis, colstr, name) :
    
    pylab.style.use('classic')
    size = [5,5]
    fig = pylab.figure(figsize=size)
    ax = fig.add_axes([0.15, 0.15, 0.7, 0.7])
    
    bins = np.linspace(-1, 1, 14);
    n, bins, patches = ax.hist(odis[:,1]-odis[:,0], bins=bins, histtype='stepfilled')
    ax.set_xlim([-1, 1])
    ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    pylab.setp(patches, 'facecolor', colstr)
    ax.set_xlabel('$\Delta$ODI = $ODI_{on}$ - $ODI_{off}$', fontsize=ticklabel_fontsize)
    ax.set_ylabel('Frequency', fontsize=ticklabel_fontsize)
    savefig(fig, saveflag, size, name)

    
    
def plot_dODI_vs_depth (odis, depths, pvals, col, target_pval, name, alpha=1):
    
    pylab.style.use('seaborn-bright')
    size = [3.5, 3.5]
    fig = pylab.figure(figsize=size)
    ax = fig.add_axes([0.25, 0.2, 0.7, 0.75])
    ax.grid(True, which='both')

    for ind in range(len(depths[0,:])):
        if pvals[ind, :].min() < target_pval:
            ax.plot(odis[ind,1]-odis[ind,0], 1050-depths[0,ind], 'o', mec=col, mfc=col, mew=1, markersize=4)
        
    ax.set_ylim([230, 1075])
    ax.set_xlim([-1.5,1.5])
    ax.set_yticks(np.linspace(250, 1050, 5))
    ax.set_yticklabels([800, 600, 400, 200, 0])
    ax.set_ylabel('depth ($\mu$m)', fontsize=14)
    ax.set_xlabel('Firing rate ratio', fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    sns.set_style("ticks")
    sns.despine(offset=0, trim=True)
    for tick in ax.yaxis.get_major_ticks() :
        tick.label.set_fontsize(12)   
    savefig(fig, saveflag, size, name)
    
    
def plot_fr_vs_depth (frm, depths, pvals, colstr, target_pval, name, alpha=1):
    
    pylab.style.use('seaborn-bright')
    size = [3.5, 3.5]
    fig = pylab.figure(figsize=size)
    ax = fig.add_axes([0.25, 0.2, 0.7, 0.75])
    ax.grid(True, which='both')

    fr_ratio = 10*np.ones((len(frm[:,0]), 2))
    pp = np.ones((len(frm[:,0]), 2))
    for ind in range(np.shape(frm)[0]):
        if ~np.isnan(frm[ind,1]/frm[ind,0]):
            fr_ratio[ind,0] = frm[ind,1]/frm[ind,0];
            pp[ind, 0] = pvals[ind, 0];
        if ~np.isnan(frm[ind,3]/frm[ind,2]):
            fr_ratio[ind,1] = frm[ind,3]/frm[ind,2];
            pp[ind,1] = pvals[ind, 1];
    
    fr_ratio[fr_ratio<0.05] = 0.05;
    fr_ratio[fr_ratio>3] = 3;
   
    for ind in range(np.shape(frm)[0]): ## plotting non significant points
        if pp[ind, 0] > target_pval:
            ax.semilogx(fr_ratio[ind,0], 1050-depths[0,ind], 'o', mec=[0.8, 0.8, 0.8], mfc='w', 
                          alpha=alpha, mew=1, markersize=4)
        if pp[ind, 1] > target_pval:
            ax.semilogx(fr_ratio[ind,1], 1050-depths[0,ind], 'o', mec=[0.8, 0.8, 0.8], mfc=[0.8, 0.8, 0.8], 
                          alpha=alpha, mew=1, markersize=4)
               
    for ind in range(np.shape(frm)[0]): ## plotting significant points
        if pp[ind, 0] <= target_pval:
            ax.semilogx(fr_ratio[ind,0], 1050-depths[0,ind], 'o', mec=colstr, mfc='w', 
                          alpha=alpha, mew=1, markersize=4)
        if pp[ind, 1] <= target_pval:
            ax.semilogx(fr_ratio[ind,1], 1050-depths[0,ind], 'o', mec=colstr, mfc=colstr, 
                          alpha=alpha, mew=1, markersize=4)
    
    ax.semilogx(32.533/20.533, 500, 'o', mec='k', mfc='k', mew=1, alpha=alpha, markersize=4) #example BS cell
    #ax.semilogx(10.05/18.05, 775, 'o', mec='k', mfc='w', mew=1, alpha=alpha, markersize=4) #example NS cell
    
    ax.semilogx(0.01, 500, 'o', mec=colstr, mfc='w', alpha=alpha, mew=1, markersize=4, label='non-deprived eye')       
    ax.semilogx(0.01, 500, 'o', mec=colstr, mfc=colstr, alpha=alpha, mew=1, markersize=4, label='deprived eye')
    ax.legend(loc='lower left', numpoints=1, prop={'size': 6})
    ax.set_ylim([230, 1075])
    ax.set_xlim([0.45,3.1])
    ax.set_yticks(np.linspace(250, 1050, 5))
    ax.set_yticklabels([800, 600, 400, 200, 0])
    ax.set_ylabel('depth ($\mu$m)', fontsize=14)
    ax.set_xlabel('Firing rate ratio', fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    sns.set_style("ticks")
    sns.despine(offset=0, trim=True)
    for tick in ax.yaxis.get_major_ticks() :
        tick.label.set_fontsize(12)   
    savefig(fig, saveflag, size, name)


def plot_ODI_CDF (odis, colstr, n_bins, name) :
    
    pylab.style.use('classic')
    size = [4, 4]
    fig = pylab.figure(figsize=size)
    ax = fig.add_axes([0.15, 0.15, 0.7, 0.7])
    
    bins = np.linspace(-1, 1.02, n_bins);
    n, bins, patches = ax.hist(odis[:,0], bins=bins, ec=colstr, normed=1, histtype='step', cumulative=True, lw= 2)
    n, bins, patches = ax.hist(odis[:,1], bins=bins, ec='g', normed=1, histtype='step', cumulative=True, lw=2)
    ax.set_xlim([-1, 1]); ax.set_ylim([0,1])
    ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_ylabel('Cumulative distribution', fontsize=ticklabel_fontsize)
    ax.set_xlabel('ODI', fontsize=ticklabel_fontsize) 
    savefig(fig, saveflag, size, name)

    
    
def plot_ODI_PDF (odis, colstr, n_bins, name) :
    
    pylab.style.use('classic')
    size = [5, 5]
    fig = pylab.figure(figsize=size)
    ax = fig.add_axes([0.15, 0.15, 0.7, 0.7])
    
    bins = np.linspace(-1, 1, n_bins);
    ax.hist(odis, bins, color=[colstr,'g'])
    ax.set_xlim([-1, 1])
    ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_ylabel('Count', fontsize=ticklabel_fontsize)
    ax.set_xlabel('ODI', fontsize=ticklabel_fontsize)
    savefig(fig, saveflag, size, name)




def plot_fr (frm, pvals, colarr, target_pval, name, alpha=1) :
    
    pylab.style.use('classic')
    size = [3, 3]
    fig = pylab.figure(figsize=size)
    ax = fig.add_axes([0.28,0.25,0.67,0.67])
    
    for ind in range(np.shape(frm)[0]): ## plotting non significant points
        if pvals[ind, 0] > target_pval:
            ax.loglog(frm[ind,0], frm[ind,1], 'o', mec=[0.8, 0.8, 0.8], mfc='w', 
                          alpha=alpha, mew=1, markersize=4)
        if pvals[ind, 1] > target_pval:
            ax.loglog(frm[ind,2], frm[ind,3], 'o', mec=[0.8, 0.8, 0.8], mfc=[0.8, 0.8, 0.8], 
                          alpha=alpha, mew=1, markersize=4)
                
    for ind in range(np.shape(frm)[0]): ## plotting significant points
        if pvals[ind, 0] <= target_pval:
            ax.loglog(frm[ind,0], frm[ind,1], 'o', mec=colarr, mfc='w', 
                          alpha=alpha, mew=1, markersize=4)
        if pvals[ind, 1] <= target_pval:
            ax.loglog(frm[ind,2], frm[ind,3], 'o', mec=colarr, mfc=colarr, 
                          alpha=alpha, mew=1, markersize=4)
                
    ax.loglog(20.533, 32.533, 'o', mec='k', mfc='k', alpha=alpha, mew=1, markersize=4) # example BS cell
    #ax.loglog(18.053, 10.053, 'o', mec='k', mfc='w', alpha=alpha, mew=1, markersize=4) # example NS cell
     
    ax.loglog(0.1, 0.1, 'o', mec=colarr, mfc='w', alpha=alpha, mew=1, markersize=4, label='non-deprived eye')       
    ax.loglog(0.1, 0.1, 'o', mec=colarr, mfc=colarr, alpha=alpha, mew=1, markersize=4, label='deprived eye')
    ax.legend(loc='upper left', numpoints=1, prop={'size': 6})      
    ax.set_xlim([1, 100])
    ax.set_ylim([1, 100])
    ax.loglog([1, 100], [1, 100], ls="--", c=".3")
    ax.set_ylabel('Firing rate, light on', fontsize=ticklabel_fontsize)
    ax.set_xlabel('Firing rate, light off', fontsize=ticklabel_fontsize)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    sns.set_style("ticks")
    sns.despine(offset=5, trim=True)
    for tick in ax.yaxis.get_major_ticks() :
        tick.label.set_fontsize(13)
    savefig(fig, saveflag, size, name)


def plot_ISI (name):
    if name == 'WT ctrl' :
        isi_vals = np.array([[0.18, 0.17], [0.22, 0.185], [0.16, 0.12], [0.39, 0.28]])
    elif name == 'Gad2;Ai40' :
        isi_vals = np.array([[0.19, 0.01], [0.195, -0.03], [0.28, 0.03]])
    elif name == 'Gad2;Ai32' :
        isi_vals = np.array([[0.19, 0.01], [0.22, -0.04], [0.23, -0.09], [0.43, 0.03], [0.22, -0.03]])
        
    pylab.style.use('classic')
    size = [5, 5]
    fig = pylab.figure(figsize=size)
    ax = fig.add_axes([0.2, 0.15, 0.7, 0.7])
    jitters = np.random.normal(0, 0.0, size=(len(isi_vals[:,0])));
    
    ax.bar([0, 1], np.mean(isi_vals, axis=0), width=0.5, color='cyan', edgecolor='cyan', align='center')
    ax.plot(jitters, isi_vals[:, 0], 'none', marker='o', mfc='gold', mec='k', mew=1.25, markersize=10)
    ax.plot(1+jitters, isi_vals[:, 1], 'none', marker='o', mfc='gold', mec='k', mew=1.25, markersize=10)

    ax.set_xlim([-0.5, 1.5]);
    ax.set_ylim([1.2*np.min(isi_vals), 1.2*np.max(isi_vals)])
    ax.set_xticks([0, 1])
    ax.xaxis.set_tick_params(size=0)
    ax.set_xticklabels(['before MD', 'after MD'])
    ax.axhline(y=0, color='k')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_ylabel('ODI', fontsize=ticklabel_fontsize)
    stats, pval = ranksums(isi_vals[:,0], isi_vals[:,1])
    L = (ax.get_ylim()[1] - ax.get_ylim()[0])/100
    ypos = 1.1*np.max(isi_vals)
    if pval < 0.05:
        ax.plot([0, 1], [ypos, ypos], 'k', lw=2)
        ax.plot([0, 0], [ypos, ypos-L], 'k', lw=2)
        ax.plot([1, 1], [ypos, ypos-L], 'k', lw=2)
        s = '*'
        if pval < 0.01:
            s = '**'
        if pval < 0.001:
            s = '***'
        ax.text(0.5, ypos, s, va='bottom', ha='center')
    savefig(fig, saveflag, size, name)

 
def plot_cell_density (name):
    if name == 'Gad2;Ai40' :
        cell_nums = np.array([105, 73, 103, 100, 97, 155, 132, 112])
        
    pylab.style.use('classic')
    size = [2.5, 5]
    fig = pylab.figure(figsize=size)
    ax = fig.add_axes([0.3, 0.15, 0.7, 0.7])
    jitters = np.random.normal(0, 0.02, size=(len(cell_nums)));
    
    ax.bar([0], np.mean(cell_nums, axis=0), width=0.5, color='cyan', edgecolor='cyan', align='center')
    ax.plot(jitters, cell_nums, 'none', marker='o', mfc='gold', mec='k', mew=1.25, markersize=10)

    ax.set_xlim([-0.5, 0.5]);
    ax.set_ylim([0, 1.2*np.max(cell_nums)])
    ax.set_xticks([0])
    ax.xaxis.set_tick_params(size=0)
    ax.set_xticklabels([])
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_ylabel('cell density ($cells/mm^2$)', fontsize=ticklabel_fontsize)
    savefig(fig, saveflag, size, name)
