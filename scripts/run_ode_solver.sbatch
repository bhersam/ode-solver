#!/bin/bash
#SBATCH --job-name=ode_solver
#SBATCH --output=../logs/ode_solver_%j.out
#SBATCH --error=../logs/ode_solver_%j.err
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --mem=500M

# go to data directory where params.dat is
cd ~/training/data

# run the executable
~/training/bin/ode_solver

