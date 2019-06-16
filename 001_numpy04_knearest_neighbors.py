import numpy as np
import matplotlib.pyplot as plt
import seaborn
from itertools import cycle
seaborn.set()

x = np.random.rand(10, 2)
# menghitung jarak setiap point
dist_sq = np.sum((x[:,np.newaxis,:] - x[np.newaxis,:,:]) ** 2, axis = -1)
# menghitung perbedaan koordinat setiap poin
differences = x[:,np.newaxis,:] - x[np.newaxis,:,:]
sq_differences = differences ** 2
# jumlah perbedaan koordinat untu dapat squared distance
dist_sq = sq_differences.sum(-1)
dist_sq.diagonal()
# mencari indeks nearest neighbors
nearest = np.argsort(dist_sq, axis = 1)
k = 2
nearest_partition = np.argpartition(dist_sq, k + 1, axis = 1)
plt.scatter(x[:, 0], x[:, 1], s = 100)
# gambar line untuk setiap titik terdekat
k = 2
cycol = cycle('bgrcmky')
for i in range(x.shape[0]):
    for j in nearest_partition[i, :k+1]:
        # plot line dari x[i] to x[j] menggujnakan zip magic
        plt.plot(*zip(x[j], x[i]), c=next(cycol))

plt.show()
