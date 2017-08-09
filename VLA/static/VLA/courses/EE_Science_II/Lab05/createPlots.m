clear;clf;

t = linspace(0,10e-3,1e4);
x = 1-exp(-t/0.3e-3);
subplot(2,1,1);
plot(t/1e-3,x);
axis([0 5 0 1.1]);
set(gca,'xtick',0:.5:5);
set(gca,'ytick',0:.2:1);
bigText('g');
xlabel('time (ms)');


%%
clear;clf;
C = 0.1e-6;
L = 1e-3;
R = 1250;
RC = R*C;
LC = L*C;

s = roots([1 1/RC 1/LC]);
clc; disp(s);
H = tf(1/LC,[1 1/RC 1/LC]);
t = linspace(0,1.5e-3,1e4);
x = step(H,t);
subplot(2,1,1);
plot(t/1e-3,x);
axis([0 1.2 0 2]);
set(gca,'xtick',0:.25:1.5);
set(gca,'ytick',0:.5:2);
bigText('g');
xlabel('time (ms)');

