%% Tarea 1 — Punto 2a: dispositivo de ley cuadrática i = v^2
% Entrada: v(t) = cos(2*pi*50*t) + cos(2*pi*120*t)
% Se grafica la amplitud del espectro de la salida i(t) frente a la frecuencia.
%
% Resultado analítico (expandiendo v^2, identidad cos^2 a = (1 + cos 2a)/2
% y cos a cos b = [cos(a-b) + cos(a+b)]/2):
%   i(t) = 1 + cos(2*pi*70*t) + cos(2*pi*170*t)
%            + 0.5*cos(2*pi*100*t) + 0.5*cos(2*pi*240*t)
% Análogo óptico: término chi^(2) E^2 con dos frecuencias -> OR (DC), SHG
% (2f1, 2f2), SFG (f1+f2) y DFG (f2-f1). Hagan, Kik & Van Stryland,
% OSE5312 notas, ec. 15.31, p. 163.

clear; close all;

%% Parámetros de muestreo
f1 = 50;              % Hz
f2 = 120;             % Hz
fs = 10e3;            % frecuencia de muestreo (Hz), >> 2*240 Hz
T  = 1;               % duración (s): número entero de periodos de todas las componentes
N  = round(fs*T);
t  = (0:N-1)/fs;      % sin repetir el punto final -> ventana periódica exacta

%% Señales
v = cos(2*pi*f1*t) + cos(2*pi*f2*t);   % entrada (V)
i = v.^2;                               % salida (A), ley i = v^2 (coeficiente 1 A/V^2)

%% Espectro de amplitud unilateral
X = fft(i)/N;
f = (0:N/2)*fs/N;                 % resolución df = 1/T = 1 Hz
A = abs(X(1:N/2+1));
A(2:end-1) = 2*A(2:end-1);        % componentes f > 0 llevan factor 2 (DC no)

%% Valores analíticos
f_an = [0 70 100 170 240];
A_an = [1 1 0.5 1 0.5];

%% Tabla en consola
fprintf('\nPunto 2a: i = v^2\n');
fprintf('%10s %14s %14s\n', 'f (Hz)', '|I| FFT (A)', '|I| teórico (A)');
for k = 1:numel(f_an)
    [~, idx] = min(abs(f - f_an(k)));
    fprintf('%10.0f %14.6f %14.6f\n', f(idx), A(idx), A_an(k));
end

%% Figura
fig = figure('Units','centimeters','Position',[2 2 18 10],'Visible','off');
subplot(2,1,1);
plot(t*1e3, v, 'LineWidth', 1); hold on;
plot(t*1e3, i, 'LineWidth', 1);
xlim([0 100]); grid on;
xlabel('Tiempo t (ms)'); ylabel('Amplitud');
legend('v(t) (V)', 'i(t) (A)', 'Location', 'northeast');
title('Ley cuadrática: señal de entrada y salida');

subplot(2,1,2);
stem(f, A, 'filled', 'MarkerSize', 3); hold on;
plot(f_an, A_an, 'ro', 'MarkerSize', 8, 'LineWidth', 1.2);
xlim([-10 300]); ylim([0 1.2]); grid on;
xlabel('Frecuencia f (Hz)'); ylabel('|I(f)| (A)');
legend('FFT', 'Analítico', 'Location', 'northeast');
title('Espectro de amplitud de la salida i = v^2');
for k = 1:numel(f_an)
    text(f_an(k), A_an(k)+0.08, sprintf('%g Hz', f_an(k)), ...
        'HorizontalAlignment', 'center', 'FontSize', 8);
end

outdir = fullfile(fileparts(mfilename('fullpath')), 'figuras');
exportgraphics(fig, fullfile(outdir, 'punto2a_espectro.png'), 'Resolution', 200);
fprintf('Figura guardada en %s\n', fullfile(outdir, 'punto2a_espectro.png'));
