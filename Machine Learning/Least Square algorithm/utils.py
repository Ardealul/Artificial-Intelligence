import csv
import matplotlib.pyplot as plt
import numpy as np


# load data from .csv file
def loadData(fileName, firstAttributeName, secondAttributeName, outputName):
    data = []
    dataNames = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1
    firstAttributeIndex = dataNames.index(firstAttributeName)
    secondAttributeIndex = dataNames.index(secondAttributeName)
    outputIndex = dataNames.index(outputName)
    inputs = [[float(data[i][firstAttributeIndex]), float(data[i][secondAttributeIndex])] for i in range(len(data))]
    outputs = [float(data[i][outputIndex]) for i in range(len(data))]

    return inputs, outputs


# plot data histogram
def plotDataHistogram(x, variableName):
    plt.hist(x, 10)
    plt.title('Histogram of ' + variableName)
    plt.show()


# plot data with model
def plotData(dataSet1, dataSet2, dataSet3, beta, title):
    noOfPoints = 1000
    xref1 = []
    xval1 = min(dataSet1)
    xstep1 = (max(dataSet1) - min(dataSet1)) / noOfPoints
    xref2 = []
    xval2 = min(dataSet2)
    xstep2 = (max(dataSet2) - min(dataSet2)) / noOfPoints
    for _ in range(1, noOfPoints):
        xref1.append(xval1)
        xref2.append(xval2)
        xval1 += xstep1
        xval2 += xstep2
    yref = [[beta[0] + beta[1] * x1 + beta[2] * x2] for x1, x2 in zip(xref1, xref2)]

    ax = plt.axes(projection='3d')
    ax.scatter3D(dataSet1, dataSet2, dataSet3, c='r', marker='o')
    if title != "Train & test data":
        ax.plot_surface(np.array(xref1), np.array(xref2), np.array(yref), color='green')
    ax.set_xlabel('GDP')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness')
    plt.title(title)
    plt.show()


# plot predicted test data and real test data
def plotData2(feature1, feature2, realOutputs, computedOutputs, title):
    ax = plt.axes(projection='3d')
    ax.scatter3D(feature1, feature2, realOutputs, c='r', marker='o')
    ax.scatter3D(feature1, feature2, computedOutputs, c='g', marker='^')
    ax.set_xlabel('GDP')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness')
    plt.title(title)
    plt.show()


# norm 1
def L1(real, computed):
    return sum([abs(real[i] - computed[i]) for i in range(len(real))]) / len(real)


# norm 2
def L2(real, computed):
    return (sum([(real[i] - computed[i]) ** 2 for i in range(len(real))]) / len(real)) ** 0.5


# MSE
def meanSquareError(real, computed):
    return sum([(real[i] - computed[i]) ** 2 for i in range(len(real))]) / len(real)
