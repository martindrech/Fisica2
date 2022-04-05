# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:38:29 2022

@author: Martin
"""
import numpy as np
from matplotlib import pyplot as plt
import animatplot as amp


t = np.linspace(0, 50, 500)
x0 = [1, 0]
v0 = [0, 0]
g = 10
l = 1
k = 1
ma, mb = 1, 1

M = ma+mb
w1 = np.sqrt(g/l)
w2 = np.sqrt(g/l+k/ma+k/mb)

psi_a = mb/M * (np.cos(w1*t) - np.cos(w2*t))
psi_b = mb/M * (np.cos(w1*t) + ma/mb * np.cos(w2*t))

plt.figure(1)
plt.clf()
plt.plot(t, psi_a)
plt.plot(t, psi_b)


#%%
fps = 20

plt.figure(2)
plt.clf()
fig, ax = plt.subplots(1, 1, num = 2)
l = 10
def animate(i):
    
    ax.scatter(psi_a[i], -l, marker = 'o', c = 'r')
    ax.arrow(0, 0, psi_a[i], -l, zorder = -1)
   
    ax.scatter(1+psi_b[i], -l, marker = 'o', c = 'r')
    ax.arrow(1, 0, psi_b[i], -l, zorder = -1)
   
    ax.arrow(psi_a[i], -l, psi_b[i]-psi_a[i]+1, 0, zorder = -1)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-15, .2)
    ax.set_aspect('equal')
    
animate(0)
timeline = amp.Timeline(t, units='s', fps=fps)
block1 = amp.blocks.Nuke(animate, length=len(timeline), ax=ax)

anim = amp.Animation([block1], timeline)
anim.controls()
plt.show()   