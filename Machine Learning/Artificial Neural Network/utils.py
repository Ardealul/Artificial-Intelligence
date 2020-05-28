import os
import matplotlib.pyplot as plt
import numpy as np
import itertools
from sklearn.metrics import confusion_matrix
from PIL import Image


# load data from images
def loadData(director):
    inputs = []
    outputs = []
    outputLabels = [0, 1]  # 0 means Non-Sepia, 1 means Sepia
    images = os.listdir(director)
    for i in range(len(images)):
        image = Image.open(director + "/" + images[i])
        # WIDTH, HEIGHT = image.size
        # print(WIDTH, HEIGHT)
        data = list(image.getdata())
        inputs.append(data)
        # print(data)
        # print(len(data))
        category = images[i].split(".")[0].split("-")[1]
        if category == "True":
            outputs.append(0)
        elif category == "False":
            outputs.append(1)

    return inputs, outputs, outputLabels


# plot confusion matrix
def plotConfusionMatrix(cm, classNames, title):
    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap='Greens')
    plt.title('Confusion Matrix: ' + title)
    plt.colorbar()
    tick_marks = np.arange(len(classNames))
    plt.xticks(tick_marks, classNames, rotation=45)
    plt.yticks(tick_marks, classNames)

    text_format = 'd'
    thresh = cm.max() / 2.
    for row, column in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(column, row, format(cm[row, column], text_format),
                 horizontalalignment='center',
                 color='white' if cm[row, column] > thresh else 'black')

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

    plt.show()


# compute accuracy, precision, recall and confusion matrix
def evalMultiClass(realLabels, computedLabels, labelNames):
    confMatrix = confusion_matrix(realLabels, computedLabels)
    acc = sum([confMatrix[i][i] for i in range(len(labelNames))]) / len(realLabels)
    precision = {}
    recall = {}
    for i in range(len(labelNames)):
        precision[labelNames[i]] = confMatrix[i][i] / sum([confMatrix[j][i] for j in range(len(labelNames))])
        recall[labelNames[i]] = confMatrix[i][i] / sum([confMatrix[i][j] for j in range(len(labelNames))])
    return acc, precision, recall, confMatrix


# standardisation
def zScoreNormalization(trainInputs, testInputs):
    for i in range(len(trainInputs[0])):
        feature = [sample[i] for sample in trainInputs]
        mean = sum(feature) / len(feature)
        stDev = (1 / len(feature) * sum([(sample - mean) ** 2 for sample in feature])) ** 0.5
        for j in range(len(trainInputs)):
            trainInputs[j][i] = (trainInputs[j][i] - mean) / stDev
        for j in range(len(testInputs)):
            testInputs[j][i] = (testInputs[j][i] - mean) / stDev

    return trainInputs, testInputs


# convert an image to grayscale
def transformToGray(fromFile, toFile):
    images = os.listdir(fromFile)
    for i in range(len(images)):
        sepia_image = Image.open(fromFile + '/' + images[i]).convert('L')
        sepia_image.save(toFile + '/' + images[i])

# transformToGray(Images, GrayImages)
