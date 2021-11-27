#considerar o leitura_dataset.py

###### SÉPALAS ######

kmeans = cluster.KMeans(n_clusters=3 ,init="k-means++")
kmeans = kmeans.fit(iris[['sepala_altura','sepala_largura']])
kmeans.cluster_centers_

iris['Clusters'] = kmeans.labels_

#iris   #Para ver como tá os Clusters depois de dividir

iris['Clusters'].value_counts()

#Um modo de medir a "acurácia" do k-médias e ver se é válido usar
Resultados_corretos = iris.query('(classe == "Iris-setosa" and Clusters == "2") or (classe == "Iris-virginica" and Clusters == "1") or (classe == "Iris-versicolor" and Clusters == "0")')
Quantidade_RC = Resultados_corretos.classe.count()
print('A quantidade de resultados corretos é : ',Quantidade_RC)
Quantidade_amostras = iris.classe.count()
print('Considerando que temos um total de ', Quantidade_amostras, 'temos que a taxa de acerto na classificação foi de:')
Acerto =  Quantidade_RC/Quantidade_amostras
Acerto = Acerto * 100
print(Acerto,'%')

iris.to_csv('irisClusters.csv', index = False)
sns.scatterplot(x="sepala_altura", y="sepala_largura",hue = 'Clusters',  data=iris)




###### PÉTALAS ######

kmeans = cluster.KMeans(n_clusters=3 ,init="k-means++")
kmeans = kmeans.fit(iris[['petala_altura','petala_largura']])
kmeans.cluster_centers_

iris['Clusters'] = kmeans.labels_

#iris   #Para ver como tá os Clusters depois de dividir

iris['Clusters'].value_counts()

#O mesmo que foi feito para a análise de sépalas
Resultados_corretos = iris.query('(classe == "Iris-setosa" and Clusters == "1") or (classe == "Iris-virginica" and Clusters == "0") or (classe == "Iris-versicolor" and Clusters == "2")')
Quantidade_RC = Resultados_corretos.classe.count()
print('A quantidade de resultados corretos é : ',Quantidade_RC)
Quantidade_amostras = iris.classe.count()
print('Considerando que temos um total de ', Quantidade_amostras, 'temos que a taxa de acerto na classificação foi de:')
Acerto =  Quantidade_RC/Quantidade_amostras
Acerto = Acerto * 100
print(Acerto,'%')

iris.to_csv('irisClusters.csv', index = False)
sns.scatterplot(x="petala_altura", y="petala_largura",hue = 'Clusters',  data=iris)
