#!/usr/bin/env bash
# esperar_lumerical_libre.sh — espera (sin tocar nada) a que el Lumerical local quede
# LIBRE de la tesis y la RAM alcance, y entonces sale con código 0.
#
# Regla de ONL (CLAUDE.md, skill recursos-simulaciones): ONL solo simula si el
# Lumerical local está libre. Este script solo MIRA: no lanza ni mata procesos.
#
# Uso:  scripts/esperar_lumerical_libre.sh [argumentos de ram_lumerical.py] 
#       p. ej.  scripts/esperar_lumerical_libre.sh --fde
# Variables: INTERVALO_S (300 por defecto), MAX_HORAS (48 por defecto).
set -u
cd "$(dirname "$0")/.."
INTERVALO_S="${INTERVALO_S:-300}"
MAX_HORAS="${MAX_HORAS:-48}"
fin=$(( $(date +%s) + MAX_HORAS * 3600 ))
while :; do
  salida=$(python3 scripts/ram_lumerical.py "$@" 2>&1); rc=$?
  veredicto=$(printf '%s\n' "$salida" | grep -m1 'VEREDICTO' || echo "VEREDICTO: ?")
  disp=$(printf '%s\n' "$salida" | grep -m1 -o 'disponible [0-9.]* GB' || true)
  echo "$(date '+%F %T')  rc=$rc  $veredicto  ($disp)"
  if [ "$rc" -eq 0 ]; then
    echo "LUMERICAL LIBRE Y CABE: se puede lanzar ONL."; exit 0
  fi
  if [ "$(date +%s)" -ge "$fin" ]; then
    echo "Tiempo maximo de espera agotado (${MAX_HORAS} h)."; exit 2
  fi
  sleep "$INTERVALO_S"
done
