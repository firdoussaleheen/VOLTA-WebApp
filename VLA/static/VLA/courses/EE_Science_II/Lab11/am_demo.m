clear;clc;

% replace 'sax.wav' with the name of your wav file
[x,fs] = audioread('sax.wav');

% bandlimit to 2kHz by downsampling to 4kHz
x = resample(x,4000,fs)';

%upsample to 20kHz
fs2 = 20e3;
x = resample(x,fs2,4000);

%am - fc = 10kHz
t = (0:length(x)-1)/fs2;
fc = 10e3;
x = x./max(abs(x));
xmod = (1+x).*cos(2*pi*fc*t);
xmod = xmod./max(abs(xmod));

audiowrite('xmod.wav',xmod,fs2);
%%
%demod
xdemod = 0*xmod;
tau = 0.5e-3;
dt = 1/fs2;
for i = 2:length(xmod)
   if (xmod(i) > xdemod(i-1)) && xmod(i)>0
       xdemod(i) = xmod(i);
   else
       xdemod(i) = xdemod(i-1)*exp(-dt/tau);
   end
end

%hpf - optional (commented out)
% H = tf([1 0],[1 10]);
% xdemod=lsim(H,xdemod,t);

figure(1);clf;
plot(t,x,t,xdemod,t,xmod); xlabel('time (s)'); legend('original signal','demodulated signal','modulated signal');
xlim([2 2.01])
ylim([-1 1]);

[Xmod,f]=myFFT(xmod,fs2);
[Xdemod,~]=myFFT(xdemod,fs2);
figure(2);clf;
subplot(2,1,1); plot(f,abs(Xmod)); xlabel('freq (Hz)'); title('amplitude modulated signal');
subplot(2,1,2); plot(f,abs(Xdemod)); xlabel('freq (Hz)'); 
title('demodulated signal');

