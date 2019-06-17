# Link: https://github.com/mheriyanto/Data-Science
# Ref: Python Data Science Handbook (J. Vanderplas. 2018. O'Reilly Media. ISBN-13: 978-1491912058)
# Selecting Point from Random Points

import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set()
mean = [0, 0]
cov = [[1, 2], [2, 5]]
x = np.random.multivariate_normal(mean, cov, 100)
# memilih 20 random point yang tidak berulang
indices = np.random.choice(x.shape[0], 20, replace=False)
selection = x[indices]
plt.scatter(x[:, 0], x[:, 1], alpha=0.1)
plt.scatter(selection[:, 0], selection[:, 1], facecolor='none', color='blue', s=200)
plt.show()
