# Particle Swarm Optimization (PSO)

from typing import Callable

from matplotlib import pyplot as plt
import numpy as np


class PSO:
    """
    Particle Swarm Optimization (PSO) is a popular optimization technique inspired by the social behavior 
    of birds and fish. In PSO, a group of particles, each representing a potential solution, navigates 
    through a solution space to find the optimal solution. Each particle adjusts its position based on 
    its own experience (local search) and the best-known solution in the group (global search). This 
    algorithm is particularly well-suited for solving optimization problems, including function 
    optimization and parameter tuning in various fields such as engineering, economics, and machine 
    learning. PSO's simplicity and effectiveness have made it a valuable tool in finding optimal 
    solutions for complex problems.
    """

    def __init__(self, obj_func: Callable, n_particles: int = 20, seed: int = 20) -> None:
        np.random.seed(seed)
        self.obj_func = obj_func
        # Initialization:
        self.X = (np.random.rand(2, n_particles) - 0.5) * 2
        self.V = np.random.randn(2, n_particles) * 0.1
        # Personal Best:
        self.pbest = self.X
        self.pbest_obj = self.obj_func(self.X[0], self.X[1])
        # Global Best:
        self.gbest = self.pbest[:, self.pbest_obj.argmin()]
        self.gbest_obj = self.pbest_obj.min()

    def update(self,
               w: float = 0.8,
               c1: float = 0.1,
               c2: float = 0.1,
               limit_velocity: bool = False,
               delta: float = 0.02) -> None:
        """Updates parameters of PSO in one iteration"""
        r1, r2 = np.random.rand(2)

        # Update velocity and position vectors
        self.V = w * self.V + c1 * r1 * (self.pbest - self.X) + c2 * r2 * (self.gbest.reshape(-1, 1) - self.X)

        if limit_velocity:
            v_max = delta * (self.X.max() - self.X.min())
            self.V[self.V > v_max] = v_max

        self.X = self.X + self.V

        # Update personal best and global best of particles
        obj = self.obj_func(self.X[0], self.X[1])
        self.pbest[:, (self.pbest_obj >= obj)] = self.X[:, (self.pbest_obj >= obj)]
        self.pbest_obj = np.array([self.pbest_obj, obj]).min(axis=0)
        self.gbest = self.pbest[:, self.pbest_obj.argmin()]
        self.gbest_obj = self.pbest_obj.min()

    def plot_contour(self, x, y, z, x_range=(-1, 1), y_range=(-1, 1), save_path: str | None = None):
        # Find the global minimom
        x_min = x.ravel()[z.argmin()]
        y_min = y.ravel()[z.argmin()]

        # Set up contour map
        fig, ax = plt.subplots(figsize=(5, 4))
        fig.set_tight_layout(True)
        img = ax.imshow(z, extent=[x_range[0], x_range[1], y_range[0], y_range[1]],
                        origin='lower', cmap='viridis', alpha=0.5)
        fig.colorbar(img, ax=ax)
        ax.plot([x_min], [y_min], marker='x', markersize=5, color="white")
        contours = ax.contour(x, y, z, 10, colors='black', alpha=0.4)
        ax.clabel(contours, inline=True, fontsize=8, fmt="%.0f")

        ax.scatter(self.pbest[0], self.pbest[1], marker='o', color='black', alpha=0.5)
        ax.scatter(self.X[0], self.X[1], marker='o', color='blue', alpha=0.5)
        ax.quiver(self.X[0], self.X[1], self.V[0], self.V[1], color='blue',
                  width=0.005, angles='xy', scale_units='xy', scale=1)
        plt.scatter([self.gbest[0]], [self.gbest[1]], marker='*', s=100, color='black', alpha=0.4)

        ax.set_xlim(x_range)
        ax.set_ylim(y_range)
        if save_path:
            plt.savefig(save_path)


# Objective function
def f(x, y):
    return x ** 2 + 2 * y ** 2 - 0.3 * np.cos(3 * np.pi * x) - 0.4 * np.cos(4 * np.pi * y) + 1


if __name__ == "__main__":
    # Global Best Method
    x_, y_ = np.array(np.meshgrid(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100)))
    z_ = f(x_, y_)
    # Run the PSO algorithm
    pso = PSO(f)
    iteration = 25
    pso.plot_contour(x_, y_, z_, save_path="PSO-iter0")
    for i in range(1, iteration):
        if i % 5 == 0:
            pso.plot_contour(x_, y_, z_, save_path=f"PSO-iter{i}")
        pso.update()
    print(f"PSO found best solution at f({pso.gbest.round(5)}) = {pso.gbest_obj:3f}")

    # Global Best with Vmax Method
    pso_vmax = PSO(f)
    iteration = 25
    pso_vmax.plot_contour(x_, y_, z_, save_path=f"PSO-Vmax-iter0")
    for i in range(1, iteration):
        if i % 5 == 0:
            pso_vmax.plot_contour(x_, y_, z_, save_path=f"PSO-Vmax-iter{i}")
        pso_vmax.update(limit_velocity=True, delta=0.01)
    print(f"PSO with Vmax limitation found best solution at f({pso_vmax.gbest.round(5)}) = {pso_vmax.gbest_obj:3f}")
