#!/bin/bash
#SBATCH --job-name=ode_solver_sweep
#SBATCH --output=logs/output_%j_dt_%x.out
#SBATCH --error=logs/error_%j_dt_%x.err
#SBATCH --time=00:10:00
#SBATCH --partition=m9
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=512M

mkdir -p data

for z in {0..6}; do
	dt=$(awk "BEGIN {print 10^(-$z)}")
    	param_file="data/params_${z}.dat"
    	output_file="data/output_${z}.dat"

    echo "$dt 1000" > $param_file
    
    ./bin/ode_solver $param_file $output_file
done

