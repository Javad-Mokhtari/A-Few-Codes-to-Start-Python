# Multi-Swarm Particle Swarm Optimization (MS-PSO)

import numpy as np
from matplotlib import pyplot as plt


class MSPSO:
    "Implementation of Multi-Swarm Particle Swarm Optimization (PSO) algorithm"
    def __init__(self, obj_func, n_swarms=4, n_particles=5, seed=24):
        np.random.seed(seed)
        self.obj_func = obj_func
        self.n_swarms = n_swarms
        # Initialize data
        self.X = (np.random.rand(2, n_swarms, n_particles) - 0.5) * 2
        self.V = np.random.randn(2, n_swarms, n_particles) * 0.1
        # Initialize best personal values of particles
        self.pbest = self.X
        self.pbest_obj = self.obj_func(self.X[0], self.X[1])
        # Initialize best swarm values of particles
        sbest_idx = np.unravel_index(np.argmin(self.pbest_obj, axis=1), self.pbest_obj.shape)
        self.sbest = self.pbest[:, sbest_idx[0], sbest_idx[1]]
        self.sbest_obj = self.obj_func(self.sbest[0], self.sbest[1])
        # Initialize best global value of particle
        self.gbest = self.sbest[:, self.sbest_obj.argmin()]
        self.gbest_obj = self.sbest_obj.min()

    def update(self, w=0.8, cp=0.1, cs=0.2, cg=0.3, limit_velocity=False, delta=0.02):
        "Function to do one iteration of particle swarm optimization"
        r1, r2, r3 = np.random.rand(3)

        # Update velocity and position vectors
        self.V = w * self.V + cp*r1*(self.pbest - self.X) + cs*r2*np.subtract(self.sbest.reshape(
            (2, -1, 1)), self.X) + cg*r3*(self.gbest.reshape(-1, 1, 1)-self.X)

        # Set limitation for velocity vector
        if limit_velocity:
            Vmax = delta * (self.X.max() - self.X.min())
            self.V[self.V > Vmax] = Vmax 

        # Move particles based on their velocity in t+1 moment
        self.X = self.X + self.V

        # Update personal, swarm and global best values of particles
        obj = self.obj_func(self.X[0], self.X[1])
        self.pbest[:, (self.pbest_obj >= obj)] = self.X[:, (self.pbest_obj >= obj)]
        self.pbest_obj = np.array([self.pbest_obj, obj]).min(axis=0)
        sbest_idx = np.unravel_index(np.argmin(self.pbest_obj, axis=1), self.pbest_obj.shape)
        self.sbest = self.pbest[:, sbest_idx[0], sbest_idx[1]]
        self.sbest_obj = self.obj_func(self.sbest[0], self.sbest[1])
        self.gbest = self.sbest[:, self.sbest_obj.argmin()]
        self.gbest_obj = self.sbest_obj.min()

    def plot_contour(self, x, y, z, x_range=(-1, 1), y_range=(-1, 1), save=False, filename="figure"):
        # Find the global minimom
        x_min = x.ravel()[z.argmin()]
        y_min = y.ravel()[z.argmin()]

        # Set up contour map
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.set_tight_layout(True)
        img = ax.imshow(z, extent=[x_range[0], x_range[1], y_range[0], y_range[1]],
                        origin='lower', cmap='viridis', alpha=0.5)
        fig.colorbar(img, ax=ax)
        ax.plot([x_min], [y_min], marker='X', markersize=5, color="white")
        contours = ax.contour(x, y, z, 10, colors='black', alpha=0.4)
        ax.clabel(contours, inline=True, fontsize=8, fmt="%.0f")

        # Consider some markers and colors for different swarms
        markers = ['o', '1', 's', '^', 'P', 'v']
        colors = ['red', 'blue', 'green', 'yellow', 'pink', 'brown']

        # Plot all swarms
        for i in range(self.n_swarms):
            ax.scatter(self.pbest[0, i], self.pbest[1, i], marker=markers[i], color='black', alpha=0.5)
            ax.scatter(self.X[0, i], self.X[1, i], marker=markers[i], color=colors[i], alpha=0.5)
            ax.quiver(self.X[0, i], self.X[1, i], self.V[0, i], self.V[1, i], color=colors[i],
                                                width=0.005, angles='xy', scale_units='xy', scale=1)
        plt.scatter([self.gbest[0]], [self.gbest[1]],
                    marker='*', s=100, color='white', alpha=0.7)
        ax.set_xlim(x_range)
        ax.set_ylim(y_range)

        # We can save or not plots
        if save == True:
            plt.savefig(filename)

# Objective function
def f(x, y):
    return x**2 + 2 * y**2 - 0.3 * np.cos(3*np.pi*x) - 0.4 * np.cos(4*np.pi*y) + 1


if __name__ == "__main__":
    x, y = np.array(np.meshgrid(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100)))
    z = f(x, y)
    # Run the PSO algorithm
    mspso = MSPSO(f)
    iteration = 25
    mspso.plot_contour(x, y, z, save=True, filename="MSPSO-iter0")
    for i in range(1, iteration):
        # Save and plot particles in each 5 iteration
        if i % 5 == 0:
            mspso.plot_contour(x, y, z, save=True, filename=f"MSPSO-iter{i}")
        mspso.update()
    print(f"MS-PSO found best solution at f({mspso.gbest.round(5)}) = {mspso.gbest_obj:3f}")


