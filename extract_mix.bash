#!/bin/bash
PRA="."

echo pid IPC
for bench in 100 101 102 103; do
  echo -n pid$bench" "
  echo -n $(t=( $(grep Commit.IPC reports/x86_report.out.pid$bench | head -2 | tail -1) ); echo ${t[2]})" "
  echo
done 2>/dev/null | tr . ,
