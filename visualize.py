import os
import seaborn as sns
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

images = []
filenames = []
folder = "imgs"
for filename in os.listdir(folder):
    image = Image.open(folder + "/" + filename)
    ratio = 0.2
    w, h = image.size
    image = np.asarray(image.resize((int(w * ratio), int(h * ratio)))).flatten()
    images.append(image)
    filenames.append("imgs/" + filename)

images = np.array(images)
print(images.shape)

idx = np.random.randint(len(images), size=600)
images = images[idx]
filenames = [filenames[i] for i in idx]
print(images.shape, len(filenames))

pca = PCA(n_components=50)
pca_result = pca.fit_transform(images)
print(pca_result.shape)

tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=2000)
tsne_results = tsne.fit_transform(pca_result)
print(tsne_results.shape)

np.save("data/tsne.npy", tsne_results)
with open('data/filenames.txt', 'w') as f:
    for item in filenames:
        f.write("%s\n" % item)

plt.scatter(tsne_results[:, 0], tsne_results[:, 1])
plt.show()
