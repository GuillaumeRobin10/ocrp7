import pandas as pd


def purge(data_frame, price, profit):
    for i, row in data_frame.iterrows():
        if row[price] <= 0:
            data_frame.drop(i, inplace=True)
        if row[profit] <= 0:
            data_frame.drop(i, inplace=True)
    return data_frame


def init(data_frame, max_budget):
    for initialisation in range(max_budget):
        data_frame[initialisation] = 0


def get_dimension_y(data_frame):
    dimension = data_frame.shape
    return dimension[0]


def maximum(valeur1, valeur2):
    if valeur1 > valeur2:
        return valeur1
    else:
        return valeur2


def matrice_bellman_fort(ant, dataframe, budget_max):
    y = 0
    for i in dataframe.iterrows():
        poids_item = i[1]["price"]
        valeur_item = i[1]["profit"]
        for c in range(0, budget_max + 1):
            realc = c + 3
            if poids_item <= c:
                dataframe.iloc[y, realc] = max(dataframe.iloc[y - 1, realc - poids_item] + valeur_item,
                                               dataframe.iloc[y - 1, realc])
                if dataframe.iloc[y - 1, realc - poids_item] + valeur_item >= dataframe.iloc[y, realc]:
                    ant.iloc[y, realc] = realc - poids_item
                else:
                    ant.iloc[y, realc] = realc
            else:
                ant.iloc[y, realc] = realc
                dataframe.iloc[y, realc] = dataframe.iloc[y - 1, realc]
        y += 1


def get_resultat(ant, max_budget):
    number_of_the_next_collum = max_budget + 3
    number_of_the_ant_collum = number_of_the_next_collum
    poids = 0
    valeur = 0
    souldbuy = ""
    for i in range(nb_item - 1, -1, -1):
        number_of_the_next_collum = ant.iloc[i, number_of_the_next_collum]
        if not (number_of_the_next_collum == number_of_the_ant_collum):
            souldbuy += f"{ant.iloc[i, 0]} / "
            poids += ant.iloc[i, 1]
            valeur += ant.iloc[i, 2]
        number_of_the_ant_collum = number_of_the_next_collum
    return souldbuy, poids, valeur,


budget = 500
dataset = purge(pd.read_csv('brut.csv'), "price", "profit")
dataset["profit"] = dataset["profit"]*dataset["price"]*0.01
nb_item = get_dimension_y(dataset)
init(dataset, budget+1)
predecesseur = dataset.copy()
matrice_bellman_fort(predecesseur, dataset, budget)
result = get_resultat(predecesseur, budget)
print(f"vous devez acheter les actions suivantes : {result[0]}")
print(f"budget dépensé {result[1]}€")
print(f"bénéfice {result[2]}€")

