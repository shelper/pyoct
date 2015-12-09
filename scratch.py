# -*- coding: utf-8 -*-

"""
this file is a scratch file to test snippets, should not be included when release the package.

solely for development and quick test.

"""
import numpy as np
import time
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
fig.canvas.draw() # initialize the canvas for cached renderer for ax.draw_artist
img = ax.imshow(np.random.rand(100, 100))
plt.show(block=False)

tstart = time.time()
num_plots = 0
while time.time()-tstart < 1:
    img.set_data(np.random.rand(100, 100))
    ax.draw_artist(ax.patch)
    ax.draw_artist(img)
    fig.canvas.update()
    fig.canvas.flush_events()
    num_plots += 1
print(num_plots)
