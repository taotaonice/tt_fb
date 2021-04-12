clear;clc;close all

x = [2, 10, 20, 40, 50]';
y = [500, 2000, 3200, 4500, 4800]';

P = polyfit(x, y, 3);

X = [2:50]';
Y = polyval(P, X);

figure(1)
plot(X, Y)

grid on
xlabel('num of accounts')
ylabel('reward')

figure(2)
plot(X, Y./(X.*1000))
grid on
xlabel('num of accounts')
ylabel('percent of reward')