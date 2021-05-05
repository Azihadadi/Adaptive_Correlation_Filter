clc;
close all;
clear all;

org_img = imread('../../data/matlab/patch_1.png'); % input patch
org_tmp = imread('../../data/matlab/patch_template.png'); % template

% Converting images into greyscale
img = im2bw(org_img);
tmp = im2bw(org_tmp);

% cross correlating patch and the template
res = xcorr2(double(img),double(tmp));

% plot of result
[ssr,snd] = max(res(:));
[ij,ji] = ind2sub(size(res),snd);
figure
mesh(res)
title('Cross-Correlation (a)')

