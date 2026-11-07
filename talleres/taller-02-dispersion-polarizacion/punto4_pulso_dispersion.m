function punto4_pulso_dispersion()
% PUNTO4_PULSO_DISPERSION  Tarea 2, punto 4 (Óptica No Lineal, UNAL 2026-II).
%
% Resuelve la ecuación de la envolvente en un medio dispersivo
%
%       dA/dz = j (D_nu / 4 pi) d^2A/dt^2
%
% con el método de la función de transferencia
%
%       A(z,t) = F^{-1}[ H(nu,z) F[A(0,t)] ],   H(nu,z) = exp(-j pi D_nu nu^2 z),
%
% con la convención de Saleh y Teich (2.ª ed.): F[f](nu) = int f(t) exp(-j 2 pi nu t) dt,
% que coincide con la de fft/ifft de MATLAB. El coeficiente de dispersión D_nu se
% calcula con la ecuación de Sellmeier de la sílice fundida (tabla 5.5-1), que es
% la que genera la figura 5.6-5 del libro:  D_lambda = -(lambda/c0) d^2n/dlambda^2,
% D_nu = -D_lambda lambda^2 / c0  (D_nu = 2 pi beta'').
%
% Casos: (a) 10 ps, 0.8 um; (b) 10 ps, 1.55 um; (c) 1 ps, 0.8 um; (d) 1 ps, 1.55 um.
% El "ancho" tau0 es la semianchura a 1/e de la envolvente: A(0,t) = exp(-t^2/tau0^2).
% Distancias: z = 0, 0.2, 0.4, 0.6 y 1 km.
%
% Salidas (carpeta figuras/): punto4_caso_a..d.png/pdf, punto4_anchos.png/pdf,
% punto3_fig_5_6_5.png/pdf (reproducción de la Fig. 5.6-5) y una tabla en consola.
%
% Uso: punto4_pulso_dispersion, desde esta carpeta. Probado en MATLAB R2024b.
% Desde WSL, en modo batch, con la ruta Windows que da wslpath -w:
%   matlab.exe -batch "cd('<ruta de esta carpeta>'); punto4_pulso_dispersion"

c0 = 299792458;                                   % m/s
aqui   = fileparts(mfilename('fullpath'));
outdir = fullfile(aqui, 'figuras');
if ~exist(outdir, 'dir'), mkdir(outdir); end

% ------------------------------------------------------------------ Fig. 5.6-5
lam = linspace(0.6, 1.6, 601)*1e-6;
[n, N, Dlam] = dispersion_silice(lam, c0);
fig = figure('Visible', 'off', 'Position', [100 100 700 620]);
tiledlayout(2, 1, 'TileSpacing', 'compact');
nexttile; plot(lam*1e6, n, 'k', lam*1e6, N, 'b', 'LineWidth', 1.4); grid on
ylabel('Índice de refracción'); legend({'n = c_0/c', 'N = c_0/v (índice de grupo)'}, 'Location', 'northeast')
title('Sílice fundida: Sellmeier (tabla 5.5-1 de Saleh y Teich)')
nexttile; plot(lam*1e6, Dlam*1e6, 'r', 'LineWidth', 1.4); grid on; hold on
yline(0, 'k:');
for l = [0.8 1.312 1.55]
    [~, ~, D] = dispersion_silice(l*1e-6, c0);
    plot(l, D*1e6, 'ko', 'MarkerFaceColor', 'k');
    etq = sprintf('%.4g \\mum: %.1f', l, D*1e6);
    if l > 1.5
        text(l - 0.02, D*1e6, etq, 'FontSize', 9, 'HorizontalAlignment', 'right', 'VerticalAlignment', 'bottom');
    else
        text(l + 0.02, D*1e6, etq, 'FontSize', 9, 'VerticalAlignment', 'top');
    end
end
xlabel('Longitud de onda \lambda_0 (\mum)'); ylabel('D_\lambda (ps/(km\cdotnm))')
text(0.65, 15, 'dispersión anómala (D_\lambda > 0)', 'Color', [0.3 0.3 0.3]);
text(1.0, -100, 'dispersión normal (D_\lambda < 0)', 'Color', [0.3 0.3 0.3]);
guardar(fig, outdir, 'punto3_fig_5_6_5');

% ------------------------------------------------------- tabla para el punto 3
fprintf('\n%-8s %-9s %-9s %-16s %-14s\n', 'lam(um)', 'n', 'N', 'Dlam(ps/km/nm)', 'Dnu (s^2/m)');
for l = [0.8 1.312 1.55]
    [n1, N1, D1, Dnu1] = dispersion_silice(l*1e-6, c0);
    fprintf('%-8.3f %-9.5f %-9.5f %-16.2f %-14.3e\n', l, n1, N1, D1*1e6, Dnu1);
end

% --------------------------------------------------------------- punto 4
casos = struct('etq', {'a', 'b', 'c', 'd'}, ...
               'tau0', {10e-12, 10e-12, 1e-12, 1e-12}, ...
               'lam',  {0.8e-6, 1.55e-6, 0.8e-6, 1.55e-6});
zs = [0 0.2 0.4 0.6 1.0]*1e3;                     % m
col = [0 0 0; 0 0.45 0.74; 0.85 0.33 0.1; 0.47 0.67 0.19; 0.49 0.18 0.56];

fprintf('\n%-5s %-9s %-9s %-12s %-9s | %s\n', 'caso', 'tau0(ps)', 'lam(um)', 'Dnu(s^2/m)', 'z0(km)', ...
        'tau(z) numérico / analítico (ps) en z = 0, 0.2, 0.4, 0.6, 1 km');
figA = figure('Visible', 'off', 'Position', [100 100 760 520]); hold on; grid on
for k = 1:numel(casos)
    tau0 = casos(k).tau0; lam0 = casos(k).lam;
    [~, ~, ~, Dnu] = dispersion_silice(lam0, c0);
    z0 = pi*tau0^2/abs(Dnu);                      % longitud de dispersión (Saleh 22.3)
    tau_an = tau0*sqrt(1 + (zs/z0).^2);           % solución analítica gaussiana

    % malla temporal: ventana amplia para el pulso final, paso fino para el inicial
    T  = 24*tau_an(end);
    Nt = 2^16;
    dt = T/Nt;
    t  = (-Nt/2:Nt/2-1)*dt;
    nu = (-Nt/2:Nt/2-1)/(Nt*dt);                  % eje de frecuencia centrado (Hz)

    A0  = exp(-t.^2/tau0^2);                      % pulso gaussiano inicial
    A0f = fftshift(fft(ifftshift(A0)));           % F[A(0,t)]

    fig = figure('Visible', 'off', 'Position', [100 100 760 480]); hold on; grid on
    tau_num = zeros(size(zs));
    for m = 1:numel(zs)
        H  = exp(-1j*pi*Dnu*nu.^2*zs(m));         % función de transferencia
        A  = fftshift(ifft(ifftshift(H.*A0f)));   % A(z,t) = F^{-1}[H F[A0]]
        s = 1:4:Nt;                               % submuestreo solo para dibujar
        plot(t(s)*1e12, abs(A(s)), 'Color', col(m, :), 'LineWidth', 1.4, ...
             'DisplayName', sprintf('z = %.1f km', zs(m)/1e3));
        tau_num(m) = semianchura_1e(t, abs(A));
    end
    xlim([-1 1]*3.2*tau_an(end)*1e12)
    xlabel('t (ps)'); ylabel('|A(z,t)| (u.a.)')
    title(sprintf('(%s)  \\tau_0 = %g ps,  \\lambda_0 = %.2f \\mum,  D_\\lambda = %.1f ps/(km\\cdotnm),  z_0 = %.3g km', ...
          casos(k).etq, tau0*1e12, lam0*1e6, -Dnu*c0/lam0^2*1e6, z0/1e3));
    legend('Location', 'northeast')
    guardar(fig, outdir, ['punto4_caso_' casos(k).etq]);

    fprintf('%-5s %-9g %-9.2f %-12.3e %-9.3f | ', casos(k).etq, tau0*1e12, lam0*1e6, Dnu, z0/1e3);
    fprintf('%.2f/%.2f  ', [tau_num; tau_an]*1e12); fprintf('\n');

    % resumen: ancho numérico vs analítico
    figure(figA);
    zz = linspace(0, 1e3, 200);
    plot(zz/1e3, tau0*sqrt(1 + (zz/z0).^2)*1e12, '-', 'Color', col(k, :), 'LineWidth', 1.3, ...
         'DisplayName', sprintf('(%s) analítico: \\tau_0[1+(z/z_0)^2]^{1/2}', casos(k).etq));
    plot(zs/1e3, tau_num*1e12, 'o', 'Color', col(k, :), 'MarkerFaceColor', col(k, :), ...
         'DisplayName', sprintf('(%s) numérico (FFT)', casos(k).etq));
end
figure(figA);
set(gca, 'YScale', 'log'); xlabel('z (km)'); ylabel('\tau(z): semianchura a 1/e de |A| (ps)')
title('Ensanchamiento del pulso gaussiano: método FFT frente a la solución analítica')
legend('Location', 'eastoutside', 'FontSize', 8)
guardar(figA, outdir, 'punto4_anchos');
end

% =========================================================================
function [n, N, Dlam, Dnu] = dispersion_silice(lam, c0)
% Índice, índice de grupo y coeficientes de dispersión de la sílice fundida.
% Sellmeier (Saleh y Teich, 5.5-28 y tabla 5.5-1), lambda en metros.
% N = n - lam dn/dlam (5.6-2); Dlam = -(lam/c0) d2n/dlam2 (5.6-7); Dnu = -Dlam lam^2/c0.
B = [0.6962 0.4079 0.8975]; L = [0.06840 0.1162 9.8962]*1e-6;
nf = @(l) sqrt(1 + B(1)*l.^2./(l.^2 - L(1)^2) + B(2)*l.^2./(l.^2 - L(2)^2) + B(3)*l.^2./(l.^2 - L(3)^2));
h  = 1e-10;                                        % paso de derivación (m)
n  = nf(lam);
dn = (nf(lam + h) - nf(lam - h))/(2*h);
d2 = (nf(lam + h) - 2*n + nf(lam - h))/h^2;
N    = n - lam.*dn;
Dlam = -(lam/c0).*d2;                              % s/m^2  (1e6 -> ps/(km nm))
Dnu  = -Dlam.*lam.^2/c0;                           % s^2/m
end

function tau = semianchura_1e(t, a)
% Semianchura a 1/e de |A| (interpolación lineal alrededor del cruce).
a = a/max(a); i0 = find(a >= exp(-1), 1, 'last');
tau = interp1(a([i0 i0+1]), t([i0 i0+1]), exp(-1)) - t(a == 1);
tau = tau(1);
end

function guardar(fig, outdir, nombre)
exportgraphics(fig, fullfile(outdir, [nombre '.png']), 'Resolution', 170);
exportgraphics(fig, fullfile(outdir, [nombre '.pdf']), 'ContentType', 'vector');
close(fig);
end
