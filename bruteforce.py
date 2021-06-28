import csv


class Action:
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit

    @property
    def benefice(self):
        benefice = self.price*self.profit*0.01
        return benefice


def get_actions(files):
    """
    :param files: cvs files you want to process
    :return: array of actions object
    """
    actions = []
    with open(files) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                profit = row[2].split("%")
                if not (float(profit[0]) <= 0 or float(row[1]) <= 0):
                    actions.append(Action(name=row[0], price=float(row[1]), profit=float(profit[0])))
                line_count += 1
    return actions


def exploration(dataset, max_depense):
    """
    explore all possibilities for this dataset and return the best possibilities matched with contrainte
    :param dataset: the dataset, csv format
    :param max_depense: the budget you have
    :return: the best solution ( list of actions)
    """
    max_benef = 0
    bestsolution = []
    max_possibilite = pow(2, len(dataset))
    for j in range(max_possibilite):
        benef = 0
        total_depense = 0
        i = 1
        solution = []
        a_possibilities = format(j, 'b')
        for number in reversed(a_possibilities):
            if number == "1":
                solution.append(dataset[-i])
            i += 1
        for actionn in solution:
            benef += actionn.benefice
            total_depense += actionn.price
        if benef > max_benef and total_depense <= max_depense:
            bestsolution = solution
            max_benef = benef
    return bestsolution


def display(resultat):
    """

    :param resultat: the best solution you have
    :return: display the solution
    """
    resultat_string = ""
    resultat_euro = 0
    depense = 0
    for action in resultat:
        resultat_string += f"{action.name} - "
        resultat_euro += action.benefice
        depense += action.price
    print(f"vous devez acheter :\n "
          f"{resultat_string}\n"
          f" vous aurez un profit de :"
          f"{resultat_euro} \n"
          f" pour un dépense de: {depense}")


BUDGET = 500
display(exploration(get_actions("Données.csv"), BUDGET))
