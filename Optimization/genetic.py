# Travelling Salesperson Problem solved using Genetic algorithm
from typing import Callable

import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt


class GeneticOptimization:
    """
    The `GeneticOptimization` class is used for implementing a genetic optimization algorithm. It takes a fitness
    function, population size, and dimensionality as inputs and performs optimization by generating new populations
    through mating and mutation.

    Main functionalities:
    - Initializing the optimization algorithm with a fitness function, population size, and dimensionality.
    - Generating new populations through mating and mutation.
    - Keeping track of the optimal point found during the optimization process.
    """
    def __init__(self, func: Callable, n_population: int, n_dim: int, seed: int = 42) -> None:
        self.fitness = func
        self.n_population = n_population
        self.population = np.random.uniform(low=-5, high=5, size=(self.n_population, n_dim))
        self.__optimal_point = {"iteration": 0,
                                "fitness": self.population_fitness.min(),
                                "point": np.array([])}
        np.random.seed(seed)

    @property
    def optimal_point(self) -> dict:
        return self.__optimal_point

    @staticmethod
    def to_binary(point: tuple | list | np.ndarray, width: int = 17) -> str:
        binary = ""
        for num in point:
            if num >= 0:
                binary += f"{int(round(num, 4) * 1e4):0>{width}b}"
            else:
                binary += f"1{int(round(num, 4) * -1e4):0>{width - 1}b}"
        return binary

    @staticmethod
    def to_float(binary_point: str) -> np.ndarray:
        lng = len(binary_point) // 2
        point = []
        for binary_num in [binary_point[:lng], binary_point[lng: 2 * lng]]:
            if binary_num[0] == '0':
                point.append(int(binary_num, 2) * 1e-4)
            else:
                point.append(int(binary_num[1:], 2) * -1e04)
        return np.array(point)

    @staticmethod
    def mate(prog_a: str, prog_b: str):
        i, j = np.random.choice(len(prog_a), size=2, replace=False)
        if i <= j:
            offspring_1 = prog_b[:i] + prog_a[i: j] + prog_b[j:]
            offspring_2 = prog_a[:i] + prog_b[i: j] + prog_a[j:]
        else:
            offspring_1 = prog_b[:j] + prog_a[j: i] + prog_b[i:]
            offspring_2 = prog_a[:j] + prog_b[j: i] + prog_a[i:]
        return offspring_1, offspring_2

    @property
    def population_fitness(self):
        return np.array([self.fitness(x, y) for x, y in self.population])

    @staticmethod
    def mutate(offspring):
        i, j = np.random.choice(len(offspring), size=2, replace=False)
        chromosomes = list(offspring)
        chromosomes[i], chromosomes[j] = chromosomes[j], chromosomes[i]
        return "".join(chromosomes)

    def generate(self, mutation_rate: float = 0.25, scale: float = -1e-15):
        selection_prob = np.exp(scale * self.population_fitness)
        selection_prob /= selection_prob.sum()

        # Notice there is the chance that a progenitor. mates with oneself
        progenitor_a = self.population[np.random.choice(self.n_population, size=self.n_population, p=selection_prob)]
        progenitor_b = self.population[np.random.choice(self.n_population, size=self.n_population, p=selection_prob)]

        new_population = []
        for i in range(self.n_population):
            bin_prog_a = self.to_binary(progenitor_a[i])
            bin_prog_b = self.to_binary(progenitor_b[i])
            children = self.mate(bin_prog_a, bin_prog_b)
            if np.random.random() < mutation_rate:
                mutated = [self.mutate(child) for child in children]
                new_population.extend([self.to_float(offspring) for offspring in mutated])
            else:
                new_population.extend([self.to_float(child) for child in children])
        new_population = np.stack(new_population, axis=0)

        self.population = np.vstack((self.population, new_population))
        sorted_population = self.population[np.argsort(self.population_fitness)]
        self.population = np.delete(sorted_population, np.s_[self.n_population:], axis=0)

    def run(self, iteration, mutation_rate):
        last_fit_avg = pop_fit_avg = self.population_fitness.mean()
        stop_c = 0
        for i in range(iteration):
            if i % 20 == 0:
                print(f"After iteration {i}: min value = {self.optimal_point['fitness']:.4f}, average = {pop_fit_avg:.4f}")

            self.generate(mutation_rate=mutation_rate)

            # Saving the best solution
            min_output = self.population_fitness.min()
            if min_output < self.optimal_point["fitness"]:
                self.__optimal_point["iteration"] = i + 1
                self.__optimal_point["fitness"] = min_output
                self.__optimal_point["point"] = self.population[min_output == self.population_fitness][0]

            pop_fit_avg = self.population_fitness.mean()
            if pop_fit_avg == last_fit_avg:
                stop_c += 1
                if stop_c == 200:
                    break
            last_fit_avg = pop_fit_avg

        print(f"Optimal point found at {self.optimal_point['point']}")


class GeneticTSP:
    def __init__(self, cities: np.ndarray, n_population: int = 100, seed: int = 42) -> None:
        self.n_cities = cities.shape[0]
        self.n_population = n_population
        self.cities = cities

        rng = np.random.default_rng()
        self.population = np.array([rng.permutation(x=cities, axis=0) for _ in range(self.n_population)])
        self.__best_solution = {"iteration": 0,
                                "fitness": self.population_fitness.min(),
                                "route": np.array([])}
        np.random.seed(seed)

    @property
    def best_solution(self):
        return self.__best_solution

    @staticmethod
    def fitness(route: np.ndarray):
        total_dist = la.norm(route[-1] - route[0])
        for i in range(route.shape[0] - 1):
            total_dist += la.norm(route[i] - route[i + 1])
        return total_dist

    @property
    def population_fitness(self) -> np.ndarray:
        return np.array([self.fitness(route) for route in self.population])

    @staticmethod
    def mate(prog_a: np.ndarray, prog_b: np.ndarray) -> np.ndarray:
        i, j = np.random.choice(prog_a.shape[0], size=2, replace=False)
        gen_a = prog_a[i: j] if i < j else prog_a[j: i]
        mask = np.ones(prog_a.shape[0], dtype=bool)

        for i, city_b in enumerate(prog_b):
            for city_a in gen_a:
                if (city_b == city_a).all():
                    mask[i] = False

        gen_b = prog_b[mask]
        offspring = np.vstack((gen_a, gen_b))
        return offspring

    def mutate(self, offspring):
        points_dist = np.array([self.fitness(offspring[[i - 2, i - 1, i]]) for i in range(self.n_cities)])
        nodes_prob = np.roll(points_dist, -1) / sum(points_dist)

        points = np.random.choice(self.n_cities, size=3, p=nodes_prob)
        for p in points:
            d = np.random.randint(self.n_cities)
            offspring[[p - d, p]] = offspring[[p, p - d]]
        return offspring

    def generate(self, mutation_rate: float = 0.25):
        selection_prob = np.exp(-1e-6 * self.population_fitness)
        selection_prob /= selection_prob.sum()

        # Notice there is the chance that a progenitor. mates with oneself
        progenitor_a = self.population[np.random.choice(self.n_population, size=self.n_population, p=selection_prob)]
        progenitor_b = self.population[np.random.choice(self.n_population, size=self.n_population, p=selection_prob)]

        children = []
        for i in range(self.n_population):
            child = self.mate(progenitor_a[i], progenitor_b[i])
            if np.random.random() < mutation_rate:
                children.append(self.mutate(child))
            else:
                children.append(child)
        children = np.stack(children, axis=0)

        self.population = np.vstack((self.population, children))
        sorted_population = self.population[np.argsort(self.population_fitness)]
        self.population = np.delete(sorted_population, np.s_[self.n_population:], axis=0)

    def run(self, iteration, mutation_rate):
        last_fit_avg = pop_fit_avg = self.population_fitness.mean()
        stop_c = 0
        for i in range(iteration):
            if i % 50 == 0:
                print(
                    f"After iteration {i}: min distance = {self.best_solution['fitness']:.4f}, average = {pop_fit_avg:.4f}")

            self.generate(mutation_rate=mutation_rate)

            # Saving the best solution
            min_distance = self.population_fitness.min()
            if min_distance < self.best_solution["fitness"]:
                self.__best_solution["iteration"] = i + 1
                self.__best_solution["fitness"] = min_distance
                self.__best_solution["route"] = self.population[min_distance == self.population_fitness][0]

            pop_fit_avg = self.population_fitness.mean()
            if pop_fit_avg == last_fit_avg:
                stop_c += 1
                if stop_c == 100:
                    break
            last_fit_avg = pop_fit_avg

    def plot_map(self):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot()
        # Plot cities
        ax.scatter(self.cities[:, 0], self.cities[:, 1], c='darkgreen', marker='o')

        # Plot best path
        best_route = self.best_solution["route"]
        for i in range(self.n_cities - 1):
            ax.plot([best_route[i, 0], best_route[i + 1, 0]], [best_route[i, 1], best_route[i + 1, 1]],
                    c='purple', linestyle='-', linewidth=1)

        # Plot last connection to complete loop
        ax.plot([best_route[0, 0], best_route[-1, 0]], [best_route[0, 1], best_route[-1, 1]],
                c='purple', linestyle='-', linewidth=1)

        plt.title("Solved TSP Problem using Genetic Algorithm")
        plt.text(x=1300, y=2300, s=f"Route length = {self.best_solution['fitness']:.4f}", color="purple")

        plt.savefig("Solved_TSP.svg")
        plt.show(block=True)
