load('Fig.4.mat'); 

ii = 28; %cell #78, dir: 90
cellind = cinds(ii);
ss = tris(ii,1)*nstim+1:tris(ii,2)*nstim;
    
plot_spike_raster(spk_samp, stim_info, P, L, E, ston, runtrials, ...
                  orients, ch, ss, cellind, labels(cellind), savepath);
