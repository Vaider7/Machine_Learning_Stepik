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


ages = {
    '0-18': [],
    '19-30': [],
    '31-40': [],
    '41-50': [],
    '51-60': [],
    '61-70': [],
    '71-80': [],
}


for age in data.Age.to_numpy():
    if 0 <= age <= 18:
        ages['0-18'].append(age)
    if 19 <= age <= 30:
        ages['19-30'].append(age)
    if 31 <= age <= 40:
        ages['31-40'].append(age)
    if 41 <= age <= 50:
        ages['41-50'].append(age)
    if 51 <= age <= 60:
        ages['51-60'].append(age)
    if 61 <= age <= 70:
        ages['61-70'].append(age)
    if 71 <= age <= 80:
        ages['71-80'].append(age)


ages_check = {
    '18-30': [i for i in range(0, 19)],
    '19-30': [],
    '31-40': [],
    '41-50': [],
    '51-60': [],
    '61-70': [],
    '71-80': [],
}

id_member = []

for val in data.Age.to_numpy():
    if val == None:
        pass
    elif data[(data.Age == val) & (data.Survived == 1)]:
        data[(data.Age == val) & (data.Survived == 1)].PassengerId.count()

print(data[(data.Age == 18.0) & (data.Survived == 1)])

ages_numpy = []

ages_name = ['0-18', '19-30', '31-40', '41-50', '51-60', '61-70', '71-80']

for i in ages:
    ages_numpy.append(len(ages[i]))



plt.subplot(2, 1, 1)
plt.bar(ages_name, ages_numpy)
plt.show()
