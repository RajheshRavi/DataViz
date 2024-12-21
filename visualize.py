import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn

def preProcess(data):
    return data.iloc[:,0:-1], data.iloc[:,-1]

def scatterPlot(data):
    x, y = preProcess(data)
    #print(x)
    #print(y)
    for i in x:
        #print(x[i])
        #print(len(i),len(y))
        plt.scatter(x[i], y, label=i)
        plt.legend()
    return plt

def pieChart(data):
    #x, y = preProcess(data)
    for i in data:
        plt.pie(data[i])
    return plt

def linePlot(data):
    x, y = preProcess(data)
    for i in x:
        plt.plot(x[i],y)
    return plt

def boxPlot(data):
    x, y =preProcess(data)
    plt.boxplot(x, tick_labels=x.columns)
    return plt

def heatMap(data, colormap = "crest"):
    sn.heatmap(data, cmap = colormap)
    return plt

if __name__ == "__main__":
    data = pd.read_csv("P:\ML\data\Scripts\ML Prep\Salary_dataset.csv")
    #print(data.head())
    #print(data.iloc(:,0:-1))
    #bar = scatterChart(data["YearsExperience"], data["Salary"])
    #scatterChart(data)
    #linePlot(data)
    #boxPlot(data)
    heatMap(data.corr())
    plt.show()
    #pieChart(data)