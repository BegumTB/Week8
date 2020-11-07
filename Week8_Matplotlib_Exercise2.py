import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

N_points = 100000
n_bins = 5

x = np.random.randn(N_points)
y = .4 * x + np.random.randn(100000) + 5

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(x, bins=n_bins)
axs[1].hist(y, bins=n_bins)


plt.show()

fig, axs = plt.subplots(1, 2, tight_layout=True)

N, bins, patches = axs[0].hist(x, bins=n_bins)

fracs = N / N.max()

norm = colors.Normalize(fracs.min(), fracs.max())

for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)

axs[1].hist(x, bins=n_bins, density=True)


axs[1].yaxis.set_major_formatter(PercentFormatter(xmax=1))

plt.show()


