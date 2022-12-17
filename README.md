# **Implementation of some classical algorithms in Python**

## 1. Random Walk Algorithm
<p align="justify">In mathematics, a random walk is a mathematical object, known as a stochastic or random process, that describes a path that consists of a succession of random steps on some mathematical space such as the integers. In the above code, we move randomly in one of the four directions up ٫ down ٫ left or right in a n×n network and it specifies the percentage of times the stimulus reaches a dead end.
</p>

## 2. Gray Code
<p align="justify">The reflected binary code (RBC), also known just as reflected binary (RB) or Gray code after Frank Gray, is an ordering of the binary numeral system such that two successive values differ in only one bit (binary digit). For example, the representation of the decimal value "1" in binary would normally be "001" and "2" would be "010". In Gray code, these values are represented as "001" and "011". That way, incrementing a value from 1 to 2 requires only one bit to change, instead of two. Gray codes are widely used to prevent spurious output from electromechanical switches and to facilitate error correction in digital communications such as digital terrestrial television and some cable TV systems.
</p>

## 3. Tower of Hanoi Problem
<p align="justify">The tower of Hanoi puzzle begins with the disks stacked on one rod in order of decreasing size, the smallest at the top, thus approximating a conical shape. The objective of the puzzle is to move the entire stack to the last rod, obeying the following rules:</p>
1. Only one disk may be moved at a time.</br>
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.</br>
3. No disk may be placed on top of a disk that is smaller than it.</br>
With 3 disks, the puzzle can be solved in 7 moves. The minimal number of moves required to solve a Tower of Hanoi puzzle is 2^n − 1, where n is the number of disks. In above code, we can see the order in which the disks are moved.

## 4. H-Tree Data Structure
<p align="justify">In fractal geometry, the H tree, or T-branching, is a fractal tree structure constructed from perpendicular line segments, each smaller by a factor of the square root of 2 from the next larger adjacent segment. It is so called because its repeating pattern resembles the letter "H". It has Hausdorff dimension 2, and comes arbitrarily close to every point in a rectangle. Its applications include VLSI design and microwave engineering.
</p>

## 5. Bouncing Ball
<p align="justify">In the bouncing ball code, a ball moves on a square plate with a specified velocity vector and whenever it strikes the walls, returns from the wall at the same angle of impact.
</p>

## 6. Chaos Game
The game on an equilateral triangle with three vertices R, G and B is defined as follows:
1. We start from one vertex and repeat the next steps n times.
2. We choose a vertex randomly.
3. From the beginning to the selected vertex, we walk halfway.
4. In this place we create a dot in the color of the selected vertex.
<p align="justify">The more times this algorithm is executed, the more complete the resulting image will be and finally the **Sierpinski triangle** will be seen.
Sierpinski triangle is a fractal attractive fixed set with the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles. Originally constructed as a curve, this is one of the basic examples of self-similar sets; That is, it is a mathematically generated pattern that is reproducible at any magnification or reduction. It is named after the Polish mathematician Wacław Sierpiński, but appeared as a decorative pattern many centuries before the work of Sierpinski.
</p>

## 7. Percolation-Problem
### Introduction
<p align="justify">
Now, we explain the percolation problem and try to implement it with Python step by step. In statistical physics and mathematics, percolation theory describes the behavior of a network when nodes or links are added. This is a geometric type of phase transition, since at a critical fraction of addition the network of small, disconnected clusters merge into significantly larger connected, so-called spanning cluster. The applications of percolation theory to materials science and in many other disciplines are discussed in the articles network theory and percolation.
</p>
<p align="justify">
  The Flory–Stockmayer theory was the first theory investigating percolation processes. A representative question (and the source of the name) is as follows. Assume that some liquid is poured on top of some porous material. Will the liquid be able to make its way from hole to hole and reach the bottom? This physical question is modelled mathematically as a three-dimensional network of n × n × n vertices, usually called "sites", in which the edge or "bonds" between each two neighbors may be open (allowing the liquid through) with probability p, or closed with probability 1 – p, and they are assumed to be independent. Therefore, for a given p, what is the probability that an open path (meaning a path, each of whose links is an "open" bond) exists from the top to the bottom? The behavior for large n is of primary interest. This problem, called now bond percolation, was introduced in the mathematics literature by Broadbent & Hammersley (1957), and has been studied intensively by mathematicians and physicists since then.
</p>

### Get started
<p align="justify">
To answer the percolation problem with coding, we consider an abstract model for porous material that could be an n×n table of cells. In this table, each house has two modes, open or closed. In writing this code, we use the Boolean matrix to showing the status of each cell. We also determine each house is full or empty. So we can finally tell from the connection of the houses with the surrounding houses whether the system is percolative or not. If in the table, every cell with probability p is open or closed, then the problem is random percolation. Theoretically, for large n, there is a threshold such as p*:<br/>
p* < p : Probably close to non-percolation certainty<br/>
p* > p : likely to percolation with certainty<br/>
Although there is no mathematical solution to obtain the value of p*, it can be obtained by Monte-Carlo simulation with a good approximation.
</p>

<p align="center">
  <img width="210" height="210" src="https://user-images.githubusercontent.com/73758193/135324080-16d71013-5d93-4286-aef9-1d0781b86b3a.png">
  <img width="210" height="210" src="https://user-images.githubusercontent.com/73758193/135327765-3591ca05-4b75-4466-bb5f-1375f71ca697.png">
  <img width="260" height="210" src="https://user-images.githubusercontent.com/73758193/135333505-a6a687d9-af77-4323-96cb-fd636878676a.png">
</p>

<p align="justify">
First, to simplify the problem, we consider the percolation problem only in the vertical position. That is, if the liquid percolate into any house if that house is open and the upper house is full. The probability of percolation in this case and drawing its diagram is placed in the files.
  </p>
  
 <p align="center">
  <img width="210" height="210" src="https://user-images.githubusercontent.com/73758193/135511320-01d97b8d-203e-4cfb-ae41-f88cd6163767.png">
  <img width="210" height="210" src="https://user-images.githubusercontent.com/73758193/135511359-c8e6dbe5-2764-40da-a4e0-b012b6c4c7b7.png">
</p>
<p align="justify">
The percolation problem code is almost identical to the vertical, and the main part of the code in writing is a function that represents the matrix of full cells. We use the recursive technique to write this function. Of course, this algorithm is not completely optimal and uses the <b>Depth First Search</b>, which increases the memory consumption and run time of the algorithm exponentially and is very bad for large values of n; But it will be useful for this experiment.
</p>
<p align="justify">
By visualiziation cells and showing full and empty cells, we can better understand the codes. Also, displaying data on a graph is very useful for obtaining the value of p*. Of course, the value of p* can also be obtained by testing different values, but it is a time-consuming and inaccurate way. I put a simple module to display the data and get P*, which results in a 5×5 and 10×10 matrix as follows:
  </p>

 <p align="center">
  <img width="350" height="280" src="https://user-images.githubusercontent.com/73758193/135774400-6c62c29d-2960-41aa-8af7-38f2398c4a8c.png">
  <img width="350" height="280" src="https://user-images.githubusercontent.com/73758193/135774402-400204ae-44ae-4ae1-a9e0-414750a87b12.png">
</p>
