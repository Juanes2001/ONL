%% Tarea 1 — Punto 3: razón 2.º/3.er armónico por serie de Taylor vs. resultado exacto (2b)
% Diodo: i = io*[exp(v/VT) - 1], io = 10 pA, VT = kT/e = 26 mV
% Entrada: v(t) = V0 + V1*cos(w t), V0 = 0.3 V, V1 = 0.2 V, f = 50 Hz
%
% Expansión de Taylor alrededor del punto de operación V0 (u = v - V0 = V1 cos wt):
%   i = Is*exp(u/VT) - io,  Is = io*exp(V0/VT)
%     ~ Is*[1 + u/VT + (u/VT)^2/2 + (u/VT)^3/6] - io
% Con x = V1/VT, cos^2 = (1 + cos 2wt)/2, cos^3 = (3 cos wt + cos 3wt)/4:
%   DC : Is*(1 + x^2/4) - io
%   1f : Is*(x + x^3/8)
%   2f : Is*x^2/4        (solo del término cuadrático)
%   3f : Is*x^3/24       (solo del término cúbico)
%   => I2/I3 = 6/x = 6*VT/V1
% Exacto (punto 2b): I_n = 2*Is*besseli(n, x)  =>  I2/I3 = besseli(2,x)/besseli(3,x)

clear; close all;

%% Parámetros
io = 10e-12;  VT = 26e-3;  V0 = 0.3;  V1 = 0.2;  f0 = 50;
Is = io*exp(V0/VT);
x  = V1/VT;

%% Amplitudes: Taylor (hasta orden 3, alrededor de V0) vs. exacto (Bessel)
A_tay = [Is*(1 + x^2/4) - io, Is*(x + x^3/8), Is*x^2/4, Is*x^3/24];
A_ex  = 2*Is*besseli(0:3, x);
A_ex(1) = Is*besseli(0, x) - io;

r_tay = A_tay(3)/A_tay(4);          % = 6/x
r_ex  = A_ex(3)/A_ex(4);

fprintf('\nPunto 3: x = V1/VT = %.4f, Is = io*exp(V0/VT) = %.4f uA\n', x, Is*1e6);
fprintf('%8s %16s %16s %12s\n', 'f (Hz)', 'Taylor (mA)', 'Exacto (mA)', 'Tay/Exacto');
for n = 0:3
    fprintf('%8d %16.6f %16.6f %12.4f\n', n*f0, A_tay(n+1)*1e3, A_ex(n+1)*1e3, A_tay(n+1)/A_ex(n+1));
end
fprintf('Razón I2/I3: Taylor = 6*VT/V1 = %.4f | exacta (2b) = %.4f | error relativo = %.1f %%\n', ...
    r_tay, r_ex, 100*(r_tay - r_ex)/r_ex);

% Alternativa (no recomendada): Taylor alrededor de v = 0 en vez de V0
r_tay0 = 6*(VT + V0)/V1;
fprintf('Razón I2/I3 con Taylor alrededor de v = 0: 6*(VT+V0)/V1 = %.4f\n', r_tay0);

% Amplitud de señal para la que Taylor tiene error < 10 %
x_s  = logspace(-3, log10(20), 400);
r_s  = besseli(2, x_s)./besseli(3, x_s);
err  = abs(6./x_s - r_s)./r_s;
x10  = x_s(find(err > 0.10, 1));
fprintf('Taylor (6/x) tiene error < 10 %% para x < %.3f, es decir V1 < %.1f mV\n', x10, x10*VT*1e3);

%% Figura 1: razón I2/I3 vs. amplitud de la señal
V1_s = x_s*VT;
fig = figure('Units','centimeters','Position',[2 2 18 16],'Visible','off');
subplot(2,1,1);
loglog(V1_s*1e3, r_s, 'LineWidth', 1.5); hold on;
loglog(V1_s*1e3, 6./x_s, '--', 'LineWidth', 1.5);
plot(V1*1e3, r_ex, 'ko', 'MarkerFaceColor', 'k');
plot(V1*1e3, r_tay, 'rs', 'MarkerFaceColor', 'r');
xline(V1*1e3, ':', 'V_1 = 0.2 V');
grid on; xlim([V1_s(1) V1_s(end)]*1e3);
xlabel('Amplitud de la señal V_1 (mV)'); ylabel('Razón I_{2f} / I_{3f} (adimensional)');
legend('Exacta: I_2(x)/I_3(x)', 'Taylor orden 3: 6V_T/V_1', ...
    sprintf('Exacta en V_1 = 0.2 V: %.3f', r_ex), sprintf('Taylor en V_1 = 0.2 V: %.3f', r_tay), ...
    'Location', 'southwest');
title('Razón entre 2.º y 3.er armónico de la corriente del diodo');

%% Figura 1b: comparación de amplitudes armónicas en V1 = 0.2 V
subplot(2,1,2);
b = bar(0:f0:3*f0, [A_ex; A_tay]'*1e3, 'BaseValue', 1e-3);
b(1).FaceColor = [0 0.45 0.74]; b(2).FaceColor = [0.85 0.33 0.10];
set(gca, 'YScale', 'log'); ylim([5e-3 5]); grid on;
xlabel('Frecuencia f (Hz)'); ylabel('|I(f)| (mA)');
legend('Exacto (Bessel / FFT, punto 2b)', 'Taylor hasta orden 3 alrededor de V_0', 'Location', 'northeast');
title(sprintf('Amplitudes armónicas para V_0 = %.1f V, V_1 = %.1f V (x = %.2f)', V0, V1, x));

outdir = fullfile(fileparts(mfilename('fullpath')), 'figuras');
exportgraphics(fig, fullfile(outdir, 'punto3_taylor_vs_exacto.png'), 'Resolution', 200);
fprintf('Figura guardada en %s\n', fullfile(outdir, 'punto3_taylor_vs_exacto.png'));
