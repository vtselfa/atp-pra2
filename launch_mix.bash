#!/bin/bash

# Variables de entorno, ajustar si es necesario
PRA="."
M2S="$PRA/multi2sim/bin/m2s"

# Crear directorios de salida
rm -rf $PRA/reports
mkdir $PRA/reports

rm -rf $PRA/stdout
mkdir $PRA/stdout

rm -rf $PRA/stderr
mkdir $PRA/stderr

rm -rf $PRA/tmp
mkdir $PRA/tmp

I=0
for bench in "$@"; do
  sed "s/Context 0/Context $I/" <"$PRA/configs/ctxconfigs/ctxconfig.$bench" >>"$PRA/tmp/ctxconfig"
  I=$((I+1))
done
$M2S --x86-sim detailed --x86-config $PRA/configs/cpuconfig.4c1t.conf --mem-config $PRA/configs/memconfig.4c1t.L1idL2s.conf --x86-min-inst-per-ctx 1000000 --ctx-config "$PRA/tmp/ctxconfig" --x86-report $PRA/reports/x86_report.out --mem-report $PRA/reports/mem_report.out >$PRA/stdout/stdout 2>$PRA/stderr/stderr
