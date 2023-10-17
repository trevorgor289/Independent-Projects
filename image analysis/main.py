import numpy as np
from sklearn.clusters import KMeans

img = cv.imread("konabeach.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

