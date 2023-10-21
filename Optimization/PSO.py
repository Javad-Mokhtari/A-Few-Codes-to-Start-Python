import numpy as np
import matplotlib.pyplot as plt


class PSO:
    "Implementation of Particle Swarm Optimization (PSO) algorithm"
    def __init__(self, obj_func, n_particles=20, seed=20):
        np.random.seed(seed)
        self.obj_func = obj_func
        # Initialize data
        self.X = (np.random.rand(2, n_particles) - 0.5) * 2
        self.V = np.random.randn(2, n_particles) * 0.1
        self.pbest = self.X
        self.pbest_obj = self.obj_func(self.X[0], self.X[1])
        self.gbest = self.pbest[:, self.pbest_obj.argmin()]
        self.gbest_obj = self.pbest_obj.min()

    def update(self, w=0.8, c1=0.1, c2=0.1):
        "Function to do one iteration of particle swarm optimization"
        r1, r2 = np.random.rand(2)

        # Update velocity and position vectors
        self.V = w * self.V + c1*r1*(self.pbest - self.X) + c2*r2*(self.gbest.reshape(-1, 1)-self.X)
        self.X = self.X + self.V

        # Update personal best and global best of particles
        obj = self.obj_func(self.X[0], self.X[1])
        self.pbest[:, (self.pbest_obj >= obj)] = self.X[:, (self.pbest_obj >= obj)]
        self.pbest_obj = np.array([self.pbest_obj, obj]).min(axis=0)
        self.gbest = self.pbest[:, self.pbest_obj.argmin()]
        self.gbest_obj = self.pbest_obj.min()

    def plot_contour(self, x, y, z, x_range=(-1, 1), y_range=(-1, 1), save=False, filename=""):
        # Find the global minimom
        x_min = x.ravel()[z.argmin()]
        y_min = y.ravel()[z.argmin()]

        # Set up contour map
        fig, ax = plt.subplots(figsize=(8, 6))
        fig.set_tight_layout(True)
        img = ax.imshow(z, extent=[x_range[0], x_range[1], y_range[0], y_range[1]],
                        origin='lower', cmap='viridis', alpha=0.5)
        fig.colorbar(img, ax=ax)
        ax.plot([x_min], [y_min], marker='x', markersize=5, color="white")
        contours = ax.contour(x, y, z, 10, colors='black', alpha=0.4)
        ax.clabel(contours, inline=True, fontsize=8, fmt="%.0f")
        ax.scatter(self.pbest[0], self.pbest[1],
                   marker='o', color='black', alpha=0.5)
        ax.scatter(self.X[0], self.X[1], marker='o', color='blue', alpha=0.5)
        ax.quiver(self.X[0], self.X[1], self.V[0], self.V[1], color='blue',
                  width=0.005, angles='xy', scale_units='xy', scale=1)
        plt.scatter([self.gbest[0]], [self.gbest[1]],
                    marker='*', s=100, color='black', alpha=0.4)
        ax.set_xlim(x_range)
        ax.set_ylim(y_range)
        if save == True:
            plt.savefig(filename)

# Define objective function
def f(x, y):
    return x**2 + 2 * y**2 - 0.3 * np.cos(3*np.pi*x) - 0.4 * np.cos(4*np.pi*y) + 1


if __name__ == "__main__":
    # Create search space
    x, y = np.array(np.meshgrid(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100)))
    z = f(x, y)

    # Run the PSO algorithm
    pso = PSO(f)
    iteration = 25
    pso.plot_contour(x, y, z, save=True, filename=f"PSO-iter1")
    for i in range(iteration):
        pso.update()
    pso.plot_contour(x, y, z, save=True, filename=f"PSO-iter{i+1}")

    print(f"PSO found best solution at f({pso.gbest.round(5)}) = {pso.gbest_obj:3f}")
