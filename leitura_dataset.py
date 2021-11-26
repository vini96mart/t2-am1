import pandas as pd
import sklearn.cluster as cluster
import seaborn as sns
iris = pd.read_csv('iris.data', header=None)

iris.rename(columns={0:'sepala_altura',
                     1:'sepala_largura',
                     2:'petala_altura',
                     3:'petala_largura',
                     4:'classe'}, inplace=True)

iris_data = iris[['sepala_altura', 'sepala_largura', 'petala_altura', 'petala_largura']]
iris_label = iris['classe']

#iris
iris.describe()
