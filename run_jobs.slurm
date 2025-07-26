#!/bin/bash
#SBATCH --job-name=ode_solver_batch
#SBATCH --output=logs/output_%j.txt
#SBATCH --error=logs/error_%j.txt
#SBATCH --time=00:10:00
#SBATCH --partition=m9
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=512M

mkdir -p data

for z in {0..6}; do
    dt=$(echo "10^(-$z)" | bc -l)
    steps=$(echo "9 / $dt" | bc)  # crude step calculation
    param_file="data/params_$z.dat"
    output_file="data/output_$z.dat"

    echo "$dt $steps" > "$param_file"
    
    ./bin/ode_solver "$param_file" "$output_file"
done

