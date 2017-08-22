#!/bin/bash
#PBS -N testarray
#PBS -l walltime=00:01:00,mppwidth=24
#PBS -S /bin/bash
#PBS -t 1-5
#PBS -q development
#PBS -j oe
#PBS -V
#PBS -v VAR1=value1,VAR2=value2

echo "Job array: ${PBS_ARRAYID}, ${PBS_JOBNAME}"
echo "${VAR1}, ${VAR2}"
