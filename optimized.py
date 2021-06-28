import csv

# CONSTANTE
BUDGET_INITIAL = 500
COMA = pow(10, 2)
BENEFICE_REEL = 1000000
FILES = "Données.csv"

def get_dataset(fichier):
    """
    :return:liste de liste contenant le nom de l'action, le prix et le bénéfice
    """
    dataset = []
    with open(fichier, newline='') as data:
        for row in csv.reader(data, delimiter=' '):
            dataset.append(row[0].split(','))
    return dataset


def purgedataset(dataset):
    """
    :param dataset: a list of list
    :return: a dataset without incorrect value
    """
    del dataset[0]
    i = 0
    for row in range(len(dataset)):
        try:
            if float(dataset[i][1]) <= 0 or float(dataset[i][2]) <= 0:
                del dataset[i]
                i -= 1
        except ValueError:
            del dataset[i]
        i += 1
    return dataset


def endofcoma(dataset):
    """
    :param dataset:  a list of list
    :return: a dataset without coma and with rawbenefit
    """
    for row in dataset:
        row[1] = int(float(row[1]) * COMA)
        row[2] = int(float(row[2]) * COMA) * row[1]
    return dataset


def bellmanford(budget, dataset):
    """
    :param budget: budget maximal du client
    :param dataset: liste de liste contenant le nom de l'action, le prix et le bénéfice
    :return: la liste des actions à acheté
    """
    matricebellmanford = [[0 for _ in range(budget + 1)] for _ in range(len(dataset) + 1)]
    for i in range(1, len(dataset) + 1):
        for prix in range(1, budget + 1):
            if dataset[i - 1][1] <= prix:
                matricebellmanford[i][prix] =\
                    max(dataset[i - 1][2] + matricebellmanford[i - 1][prix - dataset[i - 1][1]],
                        matricebellmanford[i - 1][prix])
            else:
                matricebellmanford[i][prix] = matricebellmanford[i - 1][prix]
    prix = budget
    nbelement = len(dataset)
    elements_selectionne = []
    while prix >= 0 and nbelement >= 0:
        action = dataset[nbelement - 1]
        if matricebellmanford[nbelement][prix] == matricebellmanford[nbelement - 1][prix - action[1]] + action[2]:
            elements_selectionne.append(action)
            prix -= action[1]
        nbelement -= 1
    return matricebellmanford[-1][-1], elements_selectionne


def showresulats(solution):
    prix = 0
    rawbenefit = solution[0]/BENEFICE_REEL
    print("Vous devez acheter les actions suivantes")
    for action in solution[1]:
        print(action[0])
        prix += action[1]
    print(f"Prix Total : {round(prix/100, 2)} \n"
          f"Bénéfice sur 2 ans :{round(rawbenefit, 2)}")


def main():
    dataset = get_dataset(FILES)
    dataset = purgedataset(dataset)
    dataset = endofcoma(dataset)
    resultat = bellmanford(BUDGET_INITIAL * COMA, dataset)
    showresulats(resultat)


main()
