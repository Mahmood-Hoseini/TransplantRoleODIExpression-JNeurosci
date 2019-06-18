function [waveforms, tags, parameters] = EIanalysis_3params(file)

bpath = pwd;
%% 1. Get templates
if nargin < 1
    [file, bpath] = uigetfile('templates.mat', 'Select all waveform files', ...
                             'MultiSelect', 'on','/Volumes/data1/mhoseini/data/');
end
             
load([bpath, file]);

parameters = NaN(size(waveforms, 2), 3); % 3 columns for: after-hyper:depolar ratio, 
                                         % trough to after-hyper time, slope 0.5 ms after trough

for ii = 1 : size(waveforms, 2)
    wave = waveforms(:, ii);
    [dp_val, dp_t] = min(wave);
    [ahp_val, ahp_t] = max(wave(dp_t+1:end));
    
    parameters(ii, 1) = ahp_val/dp_val;
    parameters(ii, 2) = ahp_t/20;
    parameters(ii, 3) = (wave(dp_t+12) - wave(dp_t+8))/(12-8)/20;
end

[labels, C] = kmeans(parameters, 2);

tags = zeros(length(labels), 1);
if mean(parameters(labels==1, 3)) > mean(parameters(labels==2, 3))
    tags(labels==1) = 'E';
    tags(labels==2) = 'I';
else
    tags(labels==2) = 'E';
    tags(labels==1) = 'I';
end

figure('Position', [200, 500, 800, 300]) 
subplot(121)
plot3(parameters(tags=='E',1), parameters(tags=='E',2), parameters(tags=='E', 3), 'mo'); hold on
plot3(parameters(tags=='I',1), parameters(tags=='I',2), parameters(tags=='I', 3), 'bo');
xlabel('peak:trough ratio', 'FontSize',13,'FontWeight','bold')
ylabel('trough to peak time', 'FontSize',13,'FontWeight','bold')
zlabel('slope 0.5 ms after trough', 'FontSize',13,'FontWeight','bold')
grid on

subplot(122)
time = (1:size(waveforms,1))'/20;
for ii = 1 : length(labels)
    col = 'm'; if tags(ii)=='I'; col = 'b'; end
    plot(time, waveforms(:, ii), col); hold on
end
title(['BS/NS: ', num2str(sum(tags=='E')), '/', num2str(sum(tags=='I'))])
xlabel('time (ms)')
ylabel('amp (\muV)')
xlim([0,2.5]); axis off
print([bpath, 'waveforms-3params'], '-dpng')