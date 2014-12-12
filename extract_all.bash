#!/bin/bash
PRA="."

echo benchmark Misses_L1D Misses_L1I Misses_L2 IPC
while read bench; do
  echo -n $bench" "
  echo -n $(t=( $(grep dl1-0.RealMisses+Evictions reports/${bench}*.mem_report.out.pid100 | head -1) ); echo ${t[2]})" "
  echo -n $(t=( $(grep il1-0.RealMisses+Evictions reports/${bench}*.mem_report.out.pid100 | head -1) ); echo ${t[2]})" "
  echo -n $(t=( $(grep l2-0.RealMisses+Evictions reports/${bench}*.mem_report.out.pid100 | head -1) ); echo ${t[2]})" "
  echo -n $(t=( $(grep Commit.IPC reports/${bench}*.x86_report.out.pid100 | head -2 | tail -1) ); echo ${t[2]})" "
  echo
done < $PRA/benchmarks.lst 2>/dev/null | tr . ,
