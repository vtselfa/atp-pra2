#!/bin/bash

# Variables de entorno, ajustar si es necesario
PRA="."
M2S="$PRA/multi2sim/bin/m2s"
NUMCPU=6

# Crear directorios de salida
rm -rf $PRA/reports
mkdir $PRA/reports

rm -rf $PRA/stdout
mkdir $PRA/stdout

rm -rf $PRA/stderr
mkdir $PRA/stderr

rm -rf $PRA/tmp
mkdir $PRA/tmp

CORES=$1 # I = 2 o 4
CORUNNER=$2

while read bench; do
  cp "$PRA/configs/ctxconfigs/ctxconfig.$bench" "$PRA/tmp/"
  if [ $CORUNNER ]; then
    I=1
    while [ $I -lt $CORES ]; do
      sed "s/Context 0/Context $I/" <"$PRA/configs/ctxconfigs/ctxconfig.$CORUNNER" >>"$PRA/tmp/ctxconfig.$bench"
      I=$((I+1))
    done
  fi
  $M2S --x86-sim detailed --x86-config $PRA/configs/cpuconfig."$CORES"c1t.conf --mem-config $PRA/configs/memconfig."$CORES"c1t.L1idL2s.conf --x86-min-inst-per-ctx 1000000 --ctx-config "$PRA/tmp/ctxconfig.$bench" --x86-report $PRA/reports/"$bench".x86_report.out --mem-report $PRA/reports/"$bench".mem_report.out >$PRA/stdout/"$bench".stdout 2>$PRA/stderr/"$bench".stderr &
  J=$(jobs -r | wc -l)
  while [ $J -eq $NUMCPU ]; do
    sleep 1s;
    J=$(jobs -r | wc -l)
  done
done < $PRA/benchmarks.lst
wait
