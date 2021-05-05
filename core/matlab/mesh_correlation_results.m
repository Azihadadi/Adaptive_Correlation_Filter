% This file meshes the correlation results of MOSSE%
clc;
close all;
clear all;

%read correlation result images
img = imread('../../data/matlab/correlation_result_1.png');
%img = imread('../../data/matlab/correlation_result_2.png');
%img = imread('../../data/matlab/correlation_result_3.png');
%img = imread('../../data/matlab/correlation_result_4.png');
%img = imread('../../data/matlab/correlation_result_5.png');

figure(1); 
imshow(img);

%greyscale of the image
imggrey = rgb2gray(img);
dgrey = double (imggrey);
figure(2);
mesh(imggrey);
