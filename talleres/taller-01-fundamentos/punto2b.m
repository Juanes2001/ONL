%% Tarea 1 — Punto 2b: diodo mezclador i = io*[exp(e*v/kT) - 1]
% io = 10 pA (corriente de saturación inversa), kT/e = 26 mV (temperatura ambiente)
% Entrada: v(t) = 0.3 + 0.2*cos(2*pi*50*t)  (V)
% Se grafica la amplitud del espectro de la salida i(t) frente a la frecuencia.
%
% Resultado analítico (generatriz de Bessel modificada,
%   exp(x cos th) = I0(x) + 2*sum_{n>=1} In(x) cos(n th)):
%   i(t) = io*exp(V0/VT)*[I0(x) + 2*sum In(x) cos(2*pi*n*50*t)] - io,
%   con V0 = 0.3 V, x = V1/VT = 0.2/0.026.
% => componente DC: io*(exp(V0/VT)*I0(x) - 1); armónico n: 2*io*exp(V0/VT)*In(x).

clear; close all;

%% Parámetros físicos
io = 10e-12;          % A
VT = 26e-3;           % V (kT/e)
V0 = 0.3;             % V, polarización DC
V1 = 0.2;             % V, amplitud de la señal
f0 = 50;              % Hz

%% Parámetros de muestreo
fs = 10e3;            % Hz
T  = 1;               % s (50 periodos exactos)
N  = round(fs*T);
t  = (0:N-1)/fs;

%% Señales
v = V0 + V1*cos(2*pi*f0*t);           % entrada (V)
i = io*(exp(v/VT) - 1);                % salida (A)

%% Espectro de amplitud unilateral
X = fft(i)/N;
f = (0:N/2)*fs/N;
A = abs(X(1:N/2+1));
A(2:end-1) = 2*A(2:end-1);

%% Valores analíticos (Bessel)
x    = V1/VT;
nmax = 20;
n    = 0:nmax;
A_an = 2*io*exp(V0/VT)*besseli(n, x);
A_an(1) = io*(exp(V0/VT)*besseli(0, x) - 1);   % DC
f_an = n*f0;

%% Tabla en consola
fprintf('\nPunto 2b: diodo mezclador, x = V1/VT = %.4f\n', x);
fprintf('%6s %8s %16s %16s %12s\n', 'n', 'f (Hz)', '|I| FFT (mA)', '|I| Bessel (mA)', 'rel. al fund.');
for k = 1:12
    [~, idx] = min(abs(f - f_an(k)));
    fprintf('%6d %8.0f %16.6f %16.6f %12.4f\n', n(k), f(idx), A(idx)*1e3, A_an(k)*1e3, A_an(k)/A_an(2));
end
fprintf('Razón 2.º/3.er armónico (100 Hz / 150 Hz): FFT = %.4f, Bessel = %.4f\n', ...
    A(f==100)/A(f==150), A_an(3)/A_an(4));
fprintf('Corriente pico: %.4f mA, mínima: %.4g mA\n', max(i)*1e3, min(i)*1e3);

%% Figura
fig = figure('Units','centimeters','Position',[2 2 18 14],'Visible','off');
subplot(3,1,1);
plot(t*1e3, v, 'LineWidth', 1); xlim([0 60]); grid on;
xlabel('Tiempo t (ms)'); ylabel('v(t) (V)');
title('Entrada: v(t) = 0.3 + 0.2 cos(2\pi 50 t)');

subplot(3,1,2);
plot(t*1e3, i*1e3, 'LineWidth', 1, 'Color', [0.85 0.33 0.10]); xlim([0 60]); grid on;
xlabel('Tiempo t (ms)'); ylabel('i(t) (mA)');
title('Salida del diodo: i = i_o[exp(v/V_T) - 1]');

subplot(3,1,3);
stem(f, A*1e3, 'filled', 'MarkerSize', 3); hold on;
plot(f_an, A_an*1e3, 'ro', 'MarkerSize', 7, 'LineWidth', 1.1);
xlim([0 1000]); grid on;
xlabel('Frecuencia f (Hz)'); ylabel('|I(f)| (mA)');
legend('FFT', 'Analítico (Bessel)', 'Location', 'northeast');
title('Espectro de amplitud de la salida (armónicos de 50 Hz)');

outdir = fullfile(fileparts(mfilename('fullpath')), 'figuras');
exportgraphics(fig, fullfile(outdir, 'punto2b_espectro.png'), 'Resolution', 200);

% Escala logarítmica: muestra el decaimiento de los armónicos de orden alto
fig2 = figure('Units','centimeters','Position',[2 2 18 8],'Visible','off');
stem(f, A*1e3, 'filled', 'MarkerSize', 3, 'BaseValue', 1e-12); hold on;
plot(f_an, A_an*1e3, 'ro', 'MarkerSize', 7, 'LineWidth', 1.1);
set(gca, 'YScale', 'log'); xlim([0 1000]); ylim([1e-10 1]); grid on;
xlabel('Frecuencia f (Hz)'); ylabel('|I(f)| (mA)');
legend('FFT', 'Analítico (Bessel)', 'Location', 'northeast');
title('Espectro de amplitud de la salida del diodo (escala logarítmica)');
exportgraphics(fig2, fullfile(outdir, 'punto2b_espectro_log.png'), 'Resolution', 200);
fprintf('Figuras guardadas en %s\n', outdir);
