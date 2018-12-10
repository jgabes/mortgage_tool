import budget
from matplotlib import pyplot as plt


def plot_budget(my_budget: budget.Budget):
    plt.figure(1)
    my_dates = list(my_budget.history().keys())
    values = list(my_budget.history().values())
    labels = make_labels(my_dates)
    y = list(range(my_dates))

    plt.plot(values, y, 'ro')
    plt.xticks(values, labels, rotation='vertical')
    plt.margins(0.2)
    plt.subplots_adjust(bottom=0.15)
    plt.show()


def make_labels(my_dates):
    first_day = my_dates[0]
    labels = ["{} {}, {}".format(first_day.day, first_day.month, first_day.year)]
    for date in my_dates[1:]:
        if date.day == 1:
            if date.month == "January":
                labels.append("{}".format(date.year))
            else:
                labels.append("{}".format(date.month))
        else:
            labels.append("{}".format(date.day))
    return labels
