Title: Projects
Date: 13-08-2021
Modified: 24-02-2025
Slug: projects
Author: Kareem Skinner
Summary: Projects page for Karsteski.com

### [**Solaran: An Intense 5v5 MOBA Game [WIP]**](https://github.com/Karsteski/karsteski.github.io)
This is my current project, a game using the Godot Engine. It's in the early stages right now :)

***Images coming soon!***

-----------------------------------------------------------------------------

### [**Cutercon: Minecraft Remote Console**](https://github.com/Karsteski/Cutercon)

[RCON](https://wiki.vg/RCON) is a TCP/IP-based protocol that allows server administrators to remotely execute Minecraft commands.

I wrote this program to help with my Minecraft server administration. It's very convenient to be able to send commands remotely to my Ubuntu server, and I added a simple GUI using PyQt6!

![Cutercon]({projects.md}/../../images/projects/cutercon/cutercon-gui.png)

-----------------------------------------------------------------------------

### [**Glautomata - Conway's Game of Life**](https://github.com/Karsteski/Glautomata)

John Conway's Game of Life displayed using batch rendering in OpenGL.

- The Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead.
- Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.
- At each step in time, the following transitions occur:
  1. Any live cell with fewer than two live neighbours dies, as if by underpopulation
  2. Any live cell with two or three live neighbours lives on to the next generation
  3. Any live cell with more than three live neighbours dies, as if by overpopulation
  4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
- This creates complex patterns from very simple rules.

I decided on a whim one day to apply my OpenGL learning to one of my favourite things to code, the game of life! It runs a lot better than my first implementation of it, which just used the [Dear ImGUI library](https://github.com/ocornut/imgui) to leverage a rendering API *(OpenGL in this case as well)* to draw to the screen. However, batch rendering, i.e. sending all the vertex data simultaneously per draw call proved to be a far more efficient method.

I'm quite proud of the code, despite it being a small project, as its pretty clean in my opinion.

**Demonstration GIF:**

![Cutercon]({projects.md}/../../images/projects/glautomata/glautomata-video.gif)

-----------------------------------------------------------------------------

### [**Cellular Automata Generator**](https://github.com/Karsteski/The_Cellular_Automata)

This is a generator for Elementary Cellular Automata and John Conway's Game of Life. Inspired by Stephen Wolfram's 2002 book: A New Kind of Science.

The cellular automata generator took me quite a while to get right. It was my first time trying to do something a bit complicated in C++, but I learnt quite a lot, and my second time around (*See Glautomata above*) had the code be much cleaner and maintainable.

- Elementary Cellular Automata are the simplest class of one-dimensional cellular atomata.
- Each cell in a grid has two possible values (0 or 1) and rules that depend on their previous three nearest neighbours.
- In this program, different automata can be generated simply by changing an 8-bit binary number that represents the rules for what each cell's state should be given it's neighbours.
- More details at [Wolfram Mathworld](https://mathworld.wolfram.com/ElementaryCellularAutomaton.html).

![**Elementary Cellular Automata: Rule 90**]({projects.md}/../../images/projects/the-cellular-automata/elementary-automata.png)
