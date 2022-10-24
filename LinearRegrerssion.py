# California Housing Datasetを読み込む

from sklearn.datasets import fetch_california_housing

dataset = fetch_california_housing()

# データセットの説明
print(dataset.DESCR)
