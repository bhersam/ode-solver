import numpy as np
import matplotlib.pyplot as plt
import os
import glob

x0= 1.0
lmbda= 1.0

data_dir='../data'
plot_dir= '.'

plt.figure(figsize=(10,6))

errors = []

for filepath in sorted(glob.glob(os.path.join(data_dir, 'output_dt*dat'))):
    dt_str = filepath.split('_dt')[1].split('dat')[0]
    label = f'dt=1e-{dt_str[-1]}' if 'e' in dt_str else f'dt={dt_str}'

    t, x_num = np.loadtxt(filepath, unpack=True)

    x_analytical= x0*np.exp(-lmbda*t)

    #error
    error = np.sqrt(np.mean((x_num-x_analytical)**2))
    errors.append((dt_str, error))

    plt.plot(t, x_num, label=label)

t_exact= np.linspace(0,9,1000)
x_exact= x0*np.exp(-lmbda*t_exact)
plt.plot(t_exact, x_exact, 'k--', label= 'analytical')
plt.plot(t_exact, x_num, '-o', label= 'numerical')

plt.xlabel('time t')
plt.ylabel('x(t)')
plt.title('numerical vs analytical solution')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(os.path.join(plot_dir, 'soln_plot.png'))


