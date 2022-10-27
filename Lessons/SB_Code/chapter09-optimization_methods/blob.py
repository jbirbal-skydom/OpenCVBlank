from sklearn.datasets import make_blobs
import numpy as np

(X, y) = make_blobs(n_samples=20, n_features=2, centers=2,
	cluster_std=1.5, random_state=1)
y = y.reshape((y.shape[0], 1))

def next_batch(X, y, batchSize):
	for i in np.arange(0, X.shape[0], batchSize):
		yield (X[i:i + batchSize], y[i:i + batchSize])

print(X)
i=0
for (batchX, batchY) in next_batch(X,y,2):
	print (i)
	print(batchX, batchY)
	i+=1

