import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

'''
fig, ax = plt.subplots(10,10)  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
plt.show()
'''

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.triplot(data1, data2, **param_dict)

    return out


data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {'marker': 'x'})
plt.show()
my_plotter(ax2, data3, data4, {'marker': 'o'})


