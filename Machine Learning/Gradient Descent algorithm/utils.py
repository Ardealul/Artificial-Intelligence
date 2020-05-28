import csv
import matplotlib.pyplot as plt
import numpy as np


# load data from .csv file (for one attribute)
def loadDataOneInput(fileName, attributeName, outputName):
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
    attributeIndex = dataNames.index(attributeName)
    outputIndex = dataNames.index(outputName)
    inputs = [float(data[i][attributeIndex]) for i in range(len(data))]
    outputs = [float(data[i][outputIndex]) for i in range(len(data))]

    return inputs, outputs


# load data from .csv file (for two attributes)
def loadDataTwoInputs(fileName, firstAttributeName, secondAttributeName, outputName):
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


# plot data with model for two features
def plotDataForBi(dataSet1, dataSet2, dataSet3, beta, title):
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


# plot predicted test data and real test data for two features
def plotData2ForBi(feature1, feature2, realOutputs, computedOutputs, title):
    ax = plt.axes(projection='3d')
    ax.scatter3D(feature1, feature2, realOutputs, c='r', marker='o')
    ax.scatter3D(feature1, feature2, computedOutputs, c='g', marker='^')
    ax.set_xlabel('GDP')
    ax.set_ylabel('Freedom')
    ax.set_zlabel('Happiness')
    plt.title(title)
    plt.show()


# plot data with model for one feature
def plotDataForUni(dataSet1, dataSet2, beta, title):
    noOfPoints = 1000
    xref = []
    val = min(dataSet1)
    step = (max(dataSet1) - min(dataSet1)) / noOfPoints
    for i in range(1, noOfPoints):
        xref.append(val)
        val += step
    yref = [beta[0] + beta[1] * el for el in xref]

    if title != "Train & test data":
        plt.plot(dataSet1, dataSet2, 'ro', label='train data')
        plt.plot(xref, yref, 'b-', label='learnt model')
    else:
        plt.plot(dataSet1, dataSet2, 'ro', label='train and test data')
    plt.title(title)
    plt.xlabel('GDP')
    plt.ylabel('Happiness')
    plt.legend()
    plt.show()


# plot predicted test data and real test data for one feature
def plotData2ForUni(feature1, realOutputs, computedOutputs, title):
    plt.plot(feature1, computedOutputs, 'yo', label='computed data')
    plt.plot(feature1, realOutputs, 'g^', label='real data')
    plt.title(title)
    plt.xlabel('GDP')
    plt.ylabel('Happiness')
    plt.legend()
    plt.show()


def zScoreNormalization(trainInputs, testInputs, trainOutputs, testOutputs):
    trainGdp = [i[0] for i in trainInputs]
    trainFreedom = [i[1] for i in trainInputs]
    testGdp = [i[0] for i in testInputs]
    testFreedom = [i[1] for i in testInputs]

    meanGdp = sum(trainGdp) / len(trainGdp)
    stdevGdp = (1 / len(trainGdp) * sum([(gdp - meanGdp) ** 2 for gdp in trainGdp])) ** 0.5
    meanFreedom = sum(trainFreedom) / len(trainFreedom)
    stdevFreedom = (1 / len(trainFreedom) * sum([(freedom - meanFreedom) ** 2 for freedom in trainFreedom])) ** 0.5

    meanOutput = sum(trainOutputs) / len(trainOutputs)
    stdevOutput = (1 / len(trainOutputs) * sum([(output - meanOutput) ** 2 for output in trainOutputs])) ** 0.5

    # apply normalization
    trainGdp = [(gdp - meanGdp) / stdevGdp for gdp in trainGdp]
    trainFreedom = [(freedom - meanFreedom) / stdevFreedom for freedom in trainFreedom]
    testGdp = [(gdp - meanGdp) / stdevGdp for gdp in testGdp]
    testFreedom = [(freedom - meanFreedom) / stdevFreedom for freedom in testFreedom]
    trainOutputs = [(output - meanOutput) / stdevOutput for output in trainOutputs]
    testOutputs = [(output - meanOutput) / stdevOutput for output in testOutputs]

    trainInputs = [[gdp, freedom] for gdp, freedom in zip(trainGdp, trainFreedom)]
    testInputs = [[gdp, freedom] for gdp, freedom in zip(testGdp, testFreedom)]

    return trainInputs, testInputs, trainOutputs, testOutputs


# norm 1
def L1(real, computed):
    return sum([abs(real[i] - computed[i]) for i in range(len(real))]) / len(real)


# norm 2
def L2(real, computed):
    return (sum([(real[i] - computed[i]) ** 2 for i in range(len(real))]) / len(real)) ** 0.5


# MSE
def meanSquareError(real, computed):
    return sum([(real[i] - computed[i]) ** 2 for i in range(len(real))]) / len(real)
