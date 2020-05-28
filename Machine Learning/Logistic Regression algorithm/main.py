from LogRegression import MyLogisticRegression
from utils import loadData, zScoreNormalization, plotData
from sklearn import linear_model
import numpy as np


def accuracy(real, computed):
    return sum([1 if real[i] == computed[i] else 0 for i in range(len(real))]) / len(real)


if __name__ == '__main__':
    inputs, outputs, labels, feature1, feature2, feature3, feature4 = loadData()

    numericalLabels = [i for i in range(len(labels))]
    numericalOutputs = [0 for i in range(len(outputs))]
    for i in range(len(labels)):
        for j in range(len(outputs)):
            if outputs[j] == labels[i]:
                numericalOutputs[j] = i

    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)  # 80% train data
    testSample = [i for i in indexes if i not in trainSample]  # 20% test data

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [numericalOutputs[i] for i in trainSample]

    testInputs = [inputs[i] for i in testSample]
    testOutputs = [numericalOutputs[i] for i in testSample]

    # print(trainInputs)
    # print(testInputs)
    trainInputs, testInputs = \
        zScoreNormalization(trainInputs, testInputs)
    # print(trainInputs)
    # print(testInputs)

    trainFeature1 = [sample[0] for sample in trainInputs]
    trainFeature2 = [sample[1] for sample in trainInputs]
    trainFeature3 = [sample[2] for sample in trainInputs]
    trainFeature4 = [sample[3] for sample in trainInputs]

    plotData(trainFeature1, trainFeature2, trainFeature3, trainFeature4, "Train data")

    # tool
    classifier = linear_model.LogisticRegression(max_iter=1000)
    classifier.fit(trainInputs, trainOutputs)
    print("-----------tool-----------")
    print("Real: " + str(testOutputs))
    print("Comp: " + str(list(classifier.predict(testInputs))))
    print("Accuracy: " + str(accuracy(testOutputs, list(classifier.predict(testInputs)))))

    # manual

    classifierIrisSetosa = MyLogisticRegression()
    classifierIrisVersicolor = MyLogisticRegression()
    classifierIrisVirginica = MyLogisticRegression()

    trainOutputSetosa = [0 if sample != 0 else 1 for sample in trainOutputs]
    trainOutputVersicolor = [0 if sample != 1 else 1 for sample in trainOutputs]
    trainOutputVirginica = [0 if sample != 2 else 1 for sample in trainOutputs]

    classifierIrisSetosa.fit(trainInputs, trainOutputSetosa)
    classifierIrisVersicolor.fit(trainInputs, trainOutputVersicolor)
    classifierIrisVirginica.fit(trainInputs, trainOutputVirginica)

    probabilitiesSetosa = classifierIrisSetosa.predict(testInputs)
    probabilitiesVersicolor = classifierIrisVersicolor.predict(testInputs)
    probabilitiesVirginica = classifierIrisVirginica.predict(testInputs)

    # print(probabilitiesSetosa)
    # print(probabilitiesVersicolor)
    # print(probabilitiesVirginica)
    computedProbabilities = [[probabilitiesSetosa[i], probabilitiesVersicolor[i], probabilitiesVirginica[i]] for i in range(len(testOutputs))]

    # print(computedProbabilities)
    computedOutputs = [numericalLabels[np.argmax(sample)] for sample in computedProbabilities]

    print("----------manual----------")
    print("Real: " + str(testOutputs))
    print("Comp: " + str(computedOutputs))
    print("Accuracy: " + str(accuracy(testOutputs, computedOutputs)))





