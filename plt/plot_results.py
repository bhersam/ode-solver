import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Base folder where the dt_* folders are
base = Path.home() / "training/data"

# List of folders to loop over
folders = ["dt_1e-6","dt_1e-5","dt_1e-4","dt_1e-3","dt_1e-2","dt_1e-1","dt_1e0"]

plt.figure(figsize=(8,6))

# Loop over each folder and plot its output.dat
for f in folders:
    data = np.loadtxt(base/f/"output.dat")
    t = data[:,0]   # first column: time
    x = data[:,1]   # second column: solution
    plt.plot(t, x, label=f"Euler {f}")

# Plot the analytical solution
t_dense = np.linspace(0, 9, 1000)
plt.plot(t_dense, np.exp(-3*t_dense), 'k--', label="Analytical")

plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig(str(Path.home() / "training/plt/solutions.png"))

