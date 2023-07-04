import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pickle
import shutil

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.ensemble import VotingClassifier

# Defina o caminho do arquivo CSV
caminho_arquivo_csv = '/compartilhado/base_treinamento.csv'  # Substitua pelo caminho real do arquivo CSV

dataRefinadoNew = pd.read_csv(caminho_arquivo_csv, on_bad_lines='skip', sep=",")

dataRefinadoNewY = dataRefinadoNew['Aceita']
dataRefinadoNewX = dataRefinadoNew.drop([
 'Aceita',
], axis=1)

scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(pd.DataFrame(dataRefinadoNewX))

dataRefinadoNewXNormalizado = pd.DataFrame(scaler.transform(dataRefinadoNewX))

x_train, x_test, y_train, y_test = train_test_split(dataRefinadoNewXNormalizado, dataRefinadoNewY, test_size=0.20,stratify = dataRefinadoNewY)
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.20,stratify = y_train)


clf1 = KNeighborsClassifier(n_neighbors = 4)

scores = cross_val_score(clf1, x_train, y_train)
print('Cross validation KNN: ', np.mean(scores))

clf2 = DecisionTreeClassifier(criterion = 'gini', max_depth=6)

scores = cross_val_score(clf2, x_train, y_train)
print('Cross validation Decision Tree: ',np.mean(scores))

clf3 = RandomForestClassifier(n_estimators = 50,
                max_depth=6,
                criterion = 'gini',
                random_state=0)
scores = cross_val_score(clf3, x_train, y_train)
print('Cross validation Forest: ', np.mean(scores))

eclf1 = VotingClassifier(estimators=[('knn', clf1), ('dtc', clf2), ('rf', clf3)], voting='soft')
scores = cross_val_score(eclf1, x_train, y_train)
print()
print('Score final com ensemble:',np.mean(scores))

eclf1.fit(x_train, y_train)
predicaoNewY = eclf1.predict(x_test)
pd.crosstab(y_test, predicaoNewY, rownames=['Correto'], colnames=['Previsto'], margins=True)

with open('modelo.pkl', 'wb') as arquivo:
    pickle.dump(eclf1, arquivo)

