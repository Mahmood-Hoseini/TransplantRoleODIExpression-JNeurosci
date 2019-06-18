function [] = plot_spike_raster(spk_samp, stiminfo, P, L, E, ston, R,...
								orients, ch, ss, cellind, tag, savepath)

% copyright (c) 2017 Mahmood Hoseini
tot_trials = length(P(ss))/length(orients)/4;
xgap = 0.05;
ygap = 0.02;
ywaves = 0.1;
width = (1 - xgap*6)/4;
height = (1 - ygap*(length(orients)+1) - ywaves)/length(orients);
widthwave = width/6;

for eye = 1 : 2
	eyestr = 'ipsi'; if eye==2; eyestr = 'cont'; end;
	figure('Units', 'normalized', 'Position', [0.45 0.01 0.5 0.92])
    for ii = 1 : length(orients)
        
        subplot('Position', [xgap, (ygap+height)*(length(orients)-ii)+ygap*2, width, height])
        stimval = stiminfo((stiminfo(:, 2)==orients(ii) & stiminfo(:, 3)==0 & stiminfo(:, 4)==eye), 1);
        plot_rastergram(spk_samp, P(ss), L(ss), E(ss), ston(ss), R(ss), eye, stimval, 0, 0, 'k'); %Still and led off
        text(-1.5, 5, ['Dir: ', num2str(orients(ii))], 'HorizontalAlignment', 'center', 'Rotation', 90, 'FontWeight', 'bold')
        if ii==1; title(['[eye, state, led]: [', eyestr, ',still , off]']); end
        hold off; axis off
        
        subplot('Position', [xgap*2+width, (ygap+height)*(length(orients)-ii)+ygap*2, width, height])
        stimval = stiminfo((stiminfo(:, 2)==orients(ii) & stiminfo(:, 3)==1 & stiminfo(:, 4)==eye), 1);
        fill([0.1, 1.6, 1.6, 0.1], [0, 0, tot_trials, tot_trials], [0.8,1,0.8], 'LineStyle', 'none'); hold on
        plot_rastergram(spk_samp, P(ss), L(ss), E(ss), ston(ss), R(ss), eye, stimval, 0, 1, 'k'); %Still and led on
        if ii==1; title(['[eye, state, led]: [', eyestr, ',still , on]']); end
        hold off; axis off
        
        subplot('Position', [xgap*4+width*2, (ygap+height)*(length(orients)-ii)+ygap*2, width, height])
        stimval = stiminfo((stiminfo(:, 2)==orients(ii) & stiminfo(:, 3)==0 & stiminfo(:, 4)==eye), 1);
        plot_rastergram(spk_samp, P(ss), L(ss), E(ss), ston(ss), R(ss), eye, stimval, 1, 0, 'r'); %Run and led off
        if ii==1; title(['[eye, state, led]: [', eyestr, ',run, off]']); end
        hold off; axis off
        
        subplot('Position', [xgap*5+width*3, (ygap+height)*(length(orients)-ii)+ygap*2, width, height])
        stimval = stiminfo((stiminfo(:, 2)==orients(ii) & stiminfo(:, 3)==1 & stiminfo(:, 4)==eye), 1);
        fill([0.1, 1.6, 1.6, 0.1], [0, 0, tot_trials, tot_trials], [0.8,1,0.8], 'LineStyle', 'none'); hold on
        plot_rastergram(spk_samp, P(ss), L(ss), E(ss), ston(ss), R(ss), eye, stimval, 1, 1, 'r'); %Run and lser on
        if ii==1; title(['[eye, state, led]: [', eyestr, ',run, on]']); end
        hold off; axis off
        
    end

	%%% Waveforms plots
%     axes = [];
% 	axes = [axes, subplot('Position', [xgap*2+width+widthwave/2, 1-ywaves, widthwave, ywaves])];
% 	plotting_waveforms(spk_samp, waveforms, ston, [E, L, R], [eye, 1, 0], [-1,0])
% 
% 	axes = [axes, subplot('Position', [xgap*2+width+3*widthwave, 1-ywaves, widthwave, ywaves])];
% 	plotting_waveforms(spk_samp, waveforms, ston, [E, L, R], [eye, 1, 0], [0,1.5])
% 
% 	axes = [axes, subplot('Position', [xgap*2+width+5*widthwave, 1-ywaves, widthwave, ywaves])];
% 	plotting_waveforms(spk_samp, waveforms, ston, [E, L, R], [eye, 1, 0], [1.5,2.5])
% 
% 	axes = [axes,subplot('Position', [xgap*5+width*3+widthwave/2, 1-ywaves, widthwave, ywaves])];
% 	plotting_waveforms(spk_samp, waveforms, ston, [E, L, R], [eye, 0, 1], [-1,0])
% 		
% 	axes = [axes, subplot('Position', [xgap*5+width*3+3*widthwave, 1-ywaves, widthwave, ywaves])];
% 	plotting_waveforms(spk_samp, waveforms, ston, [E, L, R], [eye, 0, 1], [0,1.5])
% 
% 	axes = [axes, subplot('Position', [xgap*5+width*3+5*widthwave, 1-ywaves, widthwave, ywaves])];
% 	plotting_waveforms(spk_samp, waveforms, ston, [E, L, R], [eye, 0, 1], [1.5,2.5])
%     linkaxes(axes, 'y');
% 	scalebar_Xonly(gca, 'scalelengthratio', 0.5, 'unit', 'ms')
    
	%%% Stimulus onset bars
	subplot('Position', [xgap, ygap, width, ygap])
	fill([0, 1.5, 1.5, 0], [0, 0, 1, 1], 0.8*ones(1,3), 'LineStyle', 'none'); 
	xlim([-1, 2]); hold off; axis off
	scalebar_Xonly(gca, 'scalelengthratio', 0.2, 'unit', 's')

	subplot('Position', [xgap*2+width, ygap, width, ygap])
	fill([0, 1.5, 1.5, 0], [0, 0, 1, 1], 0.8*ones(1,3), 'LineStyle', 'none');
	xlim([-1, 2]); hold off; axis off
	
	subplot('Position', [xgap*4+width*2, ygap, width, ygap])
	fill([0, 1.5, 1.5, 0], [0, 0, 1, 1], 0.8*ones(1,3), 'LineStyle', 'none');
	xlim([-1, 2]); hold off; axis off
	
	subplot('Position', [xgap*5+width*3, ygap, width, ygap])
	fill([0, 1.5, 1.5, 0], [0, 0, 1, 1], 0.8*ones(1,3), 'LineStyle', 'none');
	xlim([-1, 2]); hold off; axis off

% 	suplabel(['Cell#', num2str(cellind), '-Ch', num2str(ch)], 't');
	print([savepath, 'C', num2str(cellind), tag, '-Ch', num2str(ch), '-', eyestr, '-Rst.svg'], '-dsvg')
   	close
end
end


function [] = plot_rastergram(spkt, stimlst, ledlst, Eyes, ston, runtrials, eye, stim, state, led, cval)
adjtimes = spkt/2e4;
tot_trials = length(stimlst)/length(unique(stimlst));
pre_stim_s = 1;
post_stim_s = 2;
twindow = 20e-3; % time window for instataneous FR in sec
trial_ids = find(Eyes==eye & stimlst==stim & runtrials==state & ledlst==led);

all_spks = [];
for trial = 1 : length(trial_ids)
	times = adjtimes(adjtimes > ston(trial_ids(trial))-pre_stim_s & ...
                     adjtimes < ston(trial_ids(trial))+post_stim_s) - ston(trial_ids(trial));
	plot([times; times], repmat([trial-1; trial-0.05], 1, length(times)), cval); hold on
	all_spks = [all_spks, times];
end

fr = NaN(1, (pre_stim_s+post_stim_s)/twindow);
for ii = 1 : (pre_stim_s + post_stim_s)/twindow
	fr(ii) = sum(((all_spks>=(ii-1)*twindow-pre_stim_s) & (all_spks<ii*twindow-pre_stim_s)));
end
plot(-pre_stim_s+twindow:twindow:post_stim_s, 0.5*fr-10, 'k')
if ~isempty(trial)
    ylim([-10, max(10, trial)])
else
    ylim([-10, 10])
end
xlim([-pre_stim_s, post_stim_s])
%fprintf('[ipsi(1)/contra(2), dir(1-12), still(1)/run(2), average, and max firing rates]: %d, %d, %d, %d\n', eye, stim, state, sum(fr(50:125)/length(trial_ids)/1.5), max(fr))
end

function [] = plotting_waveforms(spktimes, waveforms, ston, infolst, info, Range)

adjtimes = spktimes/2e4;

onsets = ston((sum((infolst == info), 2) == 3));
waves = [];
for ii = 1 : size(waveforms, 2)
    if any(adjtimes(ii)>onsets+Range(1) & adjtimes(ii)<onsets+Range(2))
        waves = [waves, waveforms(:, ii)];
    end
end

if ~isempty(waves)
    max_num = min(100, size(waves,2));
    plot((-20:20)/20, waves(5:45, 1:max_num), 'Color', [0.86,0.86,1]);
    alpha(0.3); hold on;
    plot((-20:20)/20, mean(waves(5:45, 1:max_num),2), 'b', 'LineWidth', 2);
    axis off
end
end
