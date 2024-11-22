#!/usr/bin/env python3
import os, sys
import numpy as np
import matplotlib.pyplot as plt

# define a function
def plot_AT_content(input_file,window,fragment_to_evaluate):
    # 1. Import sequence and define variable
    # fragment_to_evaluate=100000
    # window = 1000
    ecoli = open(input_file).read().replace("\n", "").upper()
    ecoli_size = ecoli[0:fragment_to_evaluate]

    # 2. Make chart shows AT content in sliding 1000 base window
    ##2.1 Create empty list to hold the number of each nucleotide
    a = []
    t = []
    g = []
    c = []
    ##2.2 Count each nucleotide in every window
    for start in range(len(ecoli_size) - window):  # start in range 0:49000
        win = ecoli_size[start:start + window]  # iteracy-1  0:1000,  1:1001  100:1100   49000:50000
        a.append(win.count("A") / window)
        t.append(win.count('T') / window)
        g.append(win.count('G') / window)
        c.append(win.count('C') / window)

    # Plot the lists with appropriate labels
    plt.figure(figsize=(20, 10))
    plt.plot(a, label="A", color="red", linewidth=1)
    plt.plot(t, label="T", color="green", linewidth=1)
    # plt.plot(g, label="G",color="blue",linewidth=1)
    # plt.plot(c, label="C",color="orange",linewidth=1)
    plt.ylabel('Fraction of bases')
    plt.xlabel('Position on genome')
    plt.suptitle(f'AT contents in the E coli seq: the first {fragment_to_evaluate} bases.', fontsize=14)
    plt.title("Window size of " + str(window), fontsize=14)
    plt.legend()
    plt.savefig(f'Chart_Exercise_{fragment_to_evaluate}.png', transparent=True)
    plt.show()


# Run the function for specific arguments
input_file = "ecoli.txt"
window = 1000
fragment_to_evaluate = [50000,100000,5498450]

# Call the function with the provided input
plot_AT_content(input_file, window, fragment_to_evaluate[0])
plot_AT_content(input_file, window, fragment_to_evaluate[1])
plot_AT_content(input_file, window, fragment_to_evaluate[2])
