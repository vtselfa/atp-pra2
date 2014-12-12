#!/bin/bash
PRA="."

echo benchmark IPC
while read bench; do
  echo -n $bench" "
  echo -n $(t=( $(grep Commit.IPC reports/${bench}*.x86_report.out.pid100 | head -2 | tail -1) ); echo ${t[2]})" "
  echo
done < $PRA/benchmarks.lst 2>/dev/null | tr . ,
