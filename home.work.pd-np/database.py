import pandas as pd
import numpy as np

file_path = "tested.csv"

#pandas
data = pd.read_csv(file_path)

print(f"Размер датасета: {data.shape}\n")
print("Пропуски по столбцам:\n", data.isna().sum(), "\n")
print("Типы данных:\n", data.dtypes, "\n")

n = 10
print(data.head(n), "\n")

if "Age" in data.columns:
    print("Статистика по Age:\n", data["Age"].describe(), "\n")

print(f"Число строк: {len(data)}")
print(f"Число столбцов: {len(data.columns)}")

total_na = data.isna().sum().sum()
print(f"Всего пропусков: {total_na}\n")

if "Age" in data.columns:
    median_age = data["Age"].median()
    data["Age"] = data["Age"].fillna(median_age)

rows_with_na = data[data.isna().any(axis=1)]
drop_index = rows_with_na.index[:20]
data = data.drop(index=drop_index).reset_index(drop=True)

print(f"После удаления 20 строк: {data.shape}\n")


# numpy

if {"Sex", "Survived"}.issubset(data.columns):
    male = data["Sex"] == "male"
    female = data["Sex"] == "female"

    surv_male = data.loc[male, "Survived"].mean() * 100
    surv_female = data.loc[female, "Survived"].mean() * 100

    print(f"Процент выживших мужчин:  {surv_male:.2f}%")
    print(f"Процент выживших женщин: {surv_female:.2f}%\n")

if "Age" in data.columns:
    male = data["Sex"] == "male"
    female = data["Sex"] == "female"

    print(f"Средний возраст мужчин: {np.mean(data.loc[male,'Age'])}")
    print(f"Средний возраст женщин: {np.mean(data.loc[female,'Age'])}\n")

if {"Age", "Sex", "Survived"}.issubset(data.columns):
    surv = data["Survived"] == 1
    dead = data["Survived"] == 0
    male = data["Sex"] == "male"
    female = data["Sex"] == "female"

    print("Возраст выживших мужчин:", np.mean(data.loc[surv & male,"Age"]))
    print("Возраст погибших мужчин:", np.mean(data.loc[dead & male,"Age"]))
    print("Возраст выживших женщин:", np.mean(data.loc[surv & female,"Age"]))
    print("Возраст погибших женщин:", np.mean(data.loc[dead & female,"Age"]))


# фильтрации
if {"Age", "Sex", "Pclass"}.issubset(data.columns):
    f1 = (data["Age"] > 30) & (data["Sex"] == "male") & (data["Pclass"] == 1)
    print("Мужчины >30 лет, 1-й класс:\n", data[f1], "\n")

if {"Age", "Sex", "Survived"}.issubset(data.columns):
    f2 = ((data["Age"] < 18) | (data["Sex"] == "female")) & (data["Survived"] == 1)
    print("Моложе 18 или женщины, и выжили:\n", data[f2], "\n")


# группировки
if {"Pclass", "Sex", "Age", "Survived", "Fare"}.issubset(data.columns):
    grp = data.groupby(["Pclass", "Sex"])

    print("Средний возраст:\n", grp["Age"].mean(), "\n")
    print("Доля выживших:\n", grp["Survived"].mean(), "\n")
    print("Средняя стоимость билета:\n", grp["Fare"].mean(), "\n")
