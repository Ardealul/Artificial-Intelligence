import numpy as np
from PIL import Image

from utils import loadData, zScoreNormalization, evalMultiClass, plotConfusionMatrix
from sklearn.neural_network import MLPClassifier


if __name__ == '__main__':
    inputs, outputs, numericalLabels = loadData("GrayImages")
    outputLabels = ["Original", "Sepia"]  # [0, 1]
    # print(inputs)

    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)  # 80% train data
    testSample = [i for i in indexes if i not in trainSample]  # 20% test data

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    # print(trainInputs[:5])
    # print(testInputs[:5])
    trainInputs, testInputs = \
        zScoreNormalization(trainInputs, testInputs)
    # print(trainInputs[:5])
    # print(testInputs[:5])

    classifier = MLPClassifier(hidden_layer_sizes=(5, 5, ), activation='relu', max_iter=1000, solver='sgd',
                               verbose=10, random_state=10, learning_rate_init=.1)

    classifier.fit(trainInputs, trainOutputs)

    computedOutputs = classifier.predict(testInputs)

    print("Computed: " + str(list(computedOutputs)))
    print("Real:     " + str(testOutputs))

    accuracy, precision, recall, confusionMatrix = evalMultiClass(testOutputs, list(computedOutputs), outputLabels)
    print('accuracy: ', accuracy)
    print('precision: ', precision)
    print('recall: ', recall)

    plotConfusionMatrix(confusionMatrix, outputLabels, "Sepia vs Non-Sepia classification")
