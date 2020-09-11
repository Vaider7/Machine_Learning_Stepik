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
for p_class in data.Pclass.unique():
    print('На корабле было', data[(data.Pclass == p_class)].Pclass.count(), 'пассажиров класса', p_class)

names = []
values = []
for val in data.Sex.unique():
    names.append(val)
    values.append(data[(data.Sex == val) & (data.Survived == 1)].Sex.count()/data[(data.Sex == val)].Sex.count())
values = np.array(values)

plt.figure(figsize=(10, 6))
plt.subplot(1, 3, 1)
plt.ylabel('survive ratio')
plt.ylim(0, 1)
plt.bar(names, values)

names = []
values = []
for val in data.Pclass.unique():
    names.append(str(val)+' class')
    values.append(data[(data.Pclass == val) & (data.Survived == 1)].Pclass.count()/data[(data.Pclass == val)].Pclass.count())
values = np.array(values)

plt.subplot(1, 3, 2)
plt.ylabel('survive ratio')
plt.ylim(0, 1)
plt.bar(names, values)


names = []
values = []
for val in data.Age.unique():
    names.append(val)
    values.append(data[(data.Age == val) & (data.Survived == 1)].Age.count()/data[(data.Age == val)].Age.count())
values = np.array(values)

plt.subplot(1, 3, 3)
plt.ylabel('survive ratio')
plt.ylim(0, 1)
plt.hist((names, values), 90)
plt.show()

mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)
print('Доля выживших мужчин равна:', data[(data.Sex == 'male')&(data.Survived == 1)].Sex.count()/data.Sex.value_counts().male)
print('Доля выживших женщин равна:', data[(data.Sex == 'female')&(data.Survived == 1)].Sex.count()/data.Sex.value_counts().female)
