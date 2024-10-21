import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def kubik1(n: int):
    """

    :param n: Количество подбрасываний
    :return:  Список слкучайных подюрасываний кубика
    """
    data = []
    while len(data) < n:
        data.append(random.randint(1, 6))
    return data

def kubik2(n):
    return random.sample(range(1, 7), n, counts=None)

def kubik3(n):
    return [random.randrange(1, 6, 1) for _ in range(n)]

def kubik4(n):
    return list(np.random.randint(low = 1,high=6,size=n))

def kubik5(n):
    return list(np.random.random_sample(size = n))

def count_rate(kub_data: list):
    """
    Возвращает частоту выпадания значений кубика,
    согласно полученным данным
    :param kub_data: данные эксперимента
    :return:
    """
    kub_rate = {}
    for i in kub_data:
        if i in kub_rate:
            continue
        else:
            kub_rate[i] = kub_data.count(i)
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0
    return kub_rate

def sort_rate(counted_rate: dict):
    """
    Возвращает отсортированную частоту по ключу
    :param counted_rate: Наша неотсортированная частота
    :return:
    """
    sorted_rate = {}
    for key in sorted(counted_rate.keys()):
        sorted_rate[key] = counted_rate[key]
    return sorted_rate

def crate_dataframe(sorted_date: dict):
    """
    Создание и преобразование данных в Pandas dataframe
    :param sorted_date: dict
    :return: pd.Dataframe
    """
    df = pd.DataFrame(sorted_date, index=[0])
    df = df.T
    df = df.rename(columns={0: 'Частота'})
    df.insert(0, 'Количество выпаданий', range(1, 1 + len(df)))
    return df


def format_data(dataframe: pd.DataFrame):
    """
    Вычисление вероятности полученных результатов
    :param dataframe:
    :return:
    """
    sum_rate = dataframe['Частота'].sum()
    probability = []
    for i in dataframe['Частота']:
        probability.append(i / sum_rate)
    dataframe['Вероятность'] = probability
    return dataframe

def probability_solving(dataframe: pd.DataFrame):
    """
    Вычисление вероятности полученных результатов
    :param dataframe:
    :return:
    """
    sum_rate = dataframe['Частота'].sum()
    probability = []
    for i in dataframe['Частота']:
        probability.append(i / sum_rate)
    dataframe['Вероятность'] = probability
    return dataframe

def creat_global_data_frame(dfs):
    pass

def creat_hists(df):
    pass

k = [kubik1, kubik3, kubik4]
proba = pd.DataFrame()


for i in range(3):
    kubik = k[i]
    proba1 = probability_solving(crate_dataframe(sort_rate(count_rate(kubik(100)))))
    proba2 = probability_solving(crate_dataframe(sort_rate(count_rate(kubik(1000)))))
    proba3 = probability_solving(crate_dataframe(sort_rate(count_rate(kubik(10000)))))
    proba4 = probability_solving(crate_dataframe(sort_rate(count_rate(kubik(1000000)))))

    # a = proba['Вероятность'].plot(kind='bar', legend=True)
    # a = proba['Вероятность'].plot(kind='bar', legend=True, color='red')
    # a.figure.savefig('Вероятность.png')


    proba[f'100_{i}'] = proba1['Вероятность']
    proba[f'1000_{i}'] = proba2['Вероятность']
    proba[f'10000_{i}'] = proba3['Вероятность']
    proba[f'1000000_{i}'] = proba4['Вероятность']

proba['Количество выпаданий'] = proba1['Количество выпаданий']
proba.plot(x='Количество выпаданий', y=[f'{i}_{j}' for i in ['100', '1000', '10000', '1000000'] for j in range(3)], kind='bar')

plt.show()
