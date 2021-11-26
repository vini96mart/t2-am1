#considerar o leitura_dataset.py
#fazendo para sépalas
kmeans = cluster.KMeans(n_clusters=3 ,init="k-means++")
kmeans = kmeans.fit(iris[['sepala_altura','sepala_largura']])
kmeans.cluster_centers_

iris['Clusters'] = kmeans.labels_
#iris 
#para ver como tá os Clusters depois de dividir

iris['Clusters'].value_counts()

iris.to_csv('irisClusters.csv', index = False)
sns.scatterplot(x="sepala_altura", y="sepala_largura",hue = 'Clusters',  data=iris)


#fazendo para pétalas
kmeans = cluster.KMeans(n_clusters=3 ,init="k-means++")
kmeans = kmeans.fit(iris[['petala_altura','petala_largura']])
kmeans.cluster_centers_

iris['Clusters'] = kmeans.labels_
#iris 
#para ver como tá os Clusters depois de dividir

iris['Clusters'].value_counts()

iris.to_csv('irisClusters.csv', index = False)
sns.scatterplot(x="petala_altura", y="petala_largura",hue = 'Clusters',  data=iris)
