clear;clc;

R = 1e3;
C = 10e-6;
L = 10e-3;
vs = 1;
T = 0.05e-3;
D = .75;
ton = D*T;
toff = (1-D)*T;
tend = 500e-3;
dt = .25e-6;

t = 0:dt:tend;
vout = 0*t;

iL = 0;
for i = 2:length(t)
    if (rem(t(i),T)<ton) % sw1 closed, sw2 open
        vL = vs;
        iC = -vout(i-1)/R;
    else %sw1 open, sw2 closed
        vL = vs - vout(i-1);
        iC = iL-vout(i-1)/R;
    end
    
    diL_dt = vL / L;
    dvC_dt = iC / C;

    iL = iL + diL_dt * dt;
    vout(i) = vout(i-1) + dvC_dt * dt;
end
plot(t,vout);
