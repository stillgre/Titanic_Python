import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path1 = r"C:\Users\USER\Desktop\titanic\titanic1.csv"  # загрузка данных из 1 файла
df1 = pd.read_csv(file_path1)

file_path2 = r"C:\Users\USER\Desktop\titanic\titanic2.csv"  # загрузка данных из 2 файла
df2 = pd.read_csv(file_path2)

df_comb = pd.concat([df1, df2], ignore_index=True)  # объединение в один датафрейм

titanic_cleaned = df_comb.dropna(
    subset=["Pclass", "Survived"]
)  # удаляем строки с пустыми значениями в ключевых полях

titanic_cleaned = titanic_cleaned.drop_duplicates()  # удаляем дубликаты

# для удобства переименуем переменную
titanic = titanic_cleaned

# теперь создадим новую таблицу для наглядности

total_pass = (
    titanic.groupby(["Pclass"])
    .size()
    .reset_index(name="count")
    .sort_values(["count"], ascending=[False])
)  # все пассажиры в каждом классе

surv_pass = (
    titanic[titanic["Survived"] == 1]
    .groupby("Pclass")
    .size()
    .reset_index(name="count_surv")
)  # только выжившие пассажиры по каждому классу

result = pd.merge(total_pass, surv_pass, on="Pclass")

result["ratio"] = (result["count_surv"] / result["count"]) * 100
result = result.sort_values(["ratio"], ascending=False)

df = pd.DataFrame(result)
df.to_excel("Result.xlsx", index=False)

print(result)

# график, отражающий доли выживших по каждому классу
plt.figure(figsize=(12, 6))
sns.barplot(data=titanic, x="Pclass", y="Survived", ci=None)
plt.title = "Выживаемость по классам"
plt.xlabel = "Класс"
plt.ylabel = "Доля выживших"
plt.ylim(0, 1)
plt.show()

# график, показывающий выживаемость и некую зависимость от возраста и класса
plt.figure(figsize=(10, 6))
sns.boxplot(data=titanic, x="Pclass", y="Age", hue="Survived")
plt.title = "Распределение возраста по классам и выживаемости"
plt.xlabel = "Класс"
plt.ylabel = "Возраст"
plt.legend(title="Выжил")
plt.show()
