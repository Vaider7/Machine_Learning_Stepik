import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('titanic_data.csv', index_col='PassengerId')
basic_features = data.columns

y = pd.read_csv('titanic_surv.csv')
y.index = data.index
data = data.join(y)

print('На корабле было', data.Sex.value_counts().male,'мужчин и', data.Sex.value_counts().female,'женщин\n')
print('Класс ', data.Pclass.value_counts(), ':', '\n')

print(data.Sex.unique())
result_sex = []

for sex in data.Sex.unique():
    result_sex.extend([data[(data.Sex == sex)].Sex.count(), data[(data.Sex == sex)&(data.Survived == 1)].Sex.count()])#/data.Sex.value_counts().male
result_sex = np.array(result_sex)

names = ['Total_male', 'Survived_male', 'Total_female', 'Survived_female']
print(result_sex)

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.bar(names, result_sex)

# change total-survived system, to ratio system

names = []
result_sex = []
for sex in data.Sex.unique():
    names.append(sex+' survive ratio')
    result_sex.append(data[(data.Sex == sex)&(data.Survived == 1)].Sex.count()/data[(data.Sex == sex)].Sex.count())#/data.Sex.value_counts().male
result_sex = np.array(result_sex)
print(result_sex)

plt.subplot(1, 2, 2)
plt.bar(names, result_sex)
plt.show()

print('Доля выживших мужчин равна:', data[(data.Sex == 'male')&(data.Survived == 1)].Sex.count()/data.Sex.value_counts().male)
print('Доля выживших женщин равна:', data[(data.Sex == 'female')&(data.Survived == 1)].Sex.count()/data.Sex.value_counts().female)
