import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
data = pd.read_csv('titanic_data.csv', index_col='PassengerId')
basic_features = data.columns

y = pd.read_csv('titanic_surv.csv')
y.index = data.index
data = data.join(y)


def embarked(source_data):
    source_data['Embarked'].fillna('S', inplace=True)
    df_dummies = pd.get_dummies(source_data['Embarked'], prefix='Embarked')
    source_data = pd.concat([source_data, df_dummies], axis=1)
    source_data.drop('Embarked', axis=1, inplace=True)
    return source_data


def cabin(source_data):
    source_data['Cabin'].fillna('U', inplace=True)
    source_data['Cabin'] = source_data['Cabin'].map(lambda ca: ca[0])

    dummies = pd.get_dummies(data['Cabin'], prefix='Cabin')
    source_data = pd.concat([source_data, dummies], axis=1)
    source_data.drop('Cabin', inplace=True, axis=1)
    return source_data


def title(source_data):
    common_titles = ["Mr", "Mrs", "Miss", "Master"]
    titles = []
    for name in source_data['Name']:
        title = name.split(',')[1].split('.')[0].strip()
        if title in common_titles:
            titles.append(title)
        elif title == "Mlle":
            titles.append("Miss")
        elif title == "Mme":
            titles.append("Mrs")
        else:
            titles.append("Rare")
    df_titles = pd.DataFrame(titles, columns=['Titles'])
    title_dummies = pd.get_dummies(df_titles['Titles'], prefix='Title')
    title_dummies = title_dummies.reset_index(drop=True)
    source_data = source_data.reset_index(drop=True)
    source_data = pd.concat([source_data, title_dummies], axis=1)
    return source_data


data = embarked(data)
data = cabin(data)
data = title(data)
data['Age'].fillna(data['Age'].mean(), inplace=True)
data['Sex'] = data['Sex'].map(lambda sex: int(sex == 'male'))
data.drop(['Name', 'Ticket'], axis=1, inplace=True)


print(list(data.keys()))
for key in data.keys():
    print(data[key].value_counts())


data_y = data['Survived']
data_x = data.drop(['Survived'], axis=1)
print(data_y.head())
print(data_x.head())


X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.2, random_state=1)

clf = LogisticRegression(max_iter=1_000_000)
clf.fit(X_train, y_train)

print('Результат на обучающей: ', clf.score(X_train, y_train))
print('Результат на тестовой: ', clf.score(X_test, y_test))


clf = RandomForestClassifier(n_estimators=200, random_state=1, max_features=10, max_depth=4)
clf.fit(X_train, y_train)

print('Результат на обучающей: ', clf.score(X_train, y_train))
print('Результат на тестовой: ', clf.score(X_test, y_test))


clf = GradientBoostingClassifier(random_state=1, max_depth=2, learning_rate=0.09, n_estimators=95)
clf.fit(X_train, y_train)

print('Результат на обучающей: ', clf.score(X_train, y_train))
print('Результат на тестовой: ', clf.score(X_test, y_test))

print(clf.feature_importances_)