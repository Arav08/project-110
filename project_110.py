import plotly.figure_factory as ff
import pandas as pd
import random
import csv
import statistics
import plotly.graph_objects as go

df = pd.read_csv("project_110.csv")

data = df["claps"].tolist()

def randomSetOfMean(counter):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def showFig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["Number of claps"], show_hist = False)
    fig.show()

def setup():
    mean_list = []

    for i in range(0, 100):
        setOfMean = randomSetOfMean(30)
        mean_list.append(setOfMean)
    
    showFig(mean_list)

setup()