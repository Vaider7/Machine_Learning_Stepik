import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('titanic_data.csv', index_col='PassengerId')
basic_features = data.columns

y = pd.read_csv('titanic_surv.csv')
y.index = data.index

print('На корабле было', data.Sex.value_counts().male,'мужчин и', data.Sex.value_counts().female,'женщин\n')
print('Класс ', data.Pclass.value_counts(), ':', '\n')

print(data.Sex.unique())
result_sex = []

for sex in data.Sex.unique():
    result_sex.extend([data[(data.Sex == sex)].Sex.count(), data[(data.Sex == sex)&(data.Survived == 1)].Sex.count()])#/data.Sex.value_counts().male
result_sex = np.array(result_sex)

names = ['Total_male', 'Survived_male', 'Total_female', 'Survived_female']
print(result_sex)

plt.figure(figsize=(6, 6))

plt.bar(names, result_sex)
plt.show()

print('Долявыживших мужчин равна:',data[(data.Sex == 'male')&(data.Survived == 1)].Sex.count()/data.Sex.value_counts().male)
print('Долявыживших женщин равна:',data[(data.Sex == 'female')&(data.Survived == 1)].Sex.count()/data.Sex.value_counts().female)
