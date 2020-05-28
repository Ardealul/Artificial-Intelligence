import matplotlib.pyplot as plt


def loadData():
    file = open("iris.data", "r")
    inputs = []
    outputs = []
    sepalLengths = []
    sepalWidths = []
    petalLenghts = []
    petalWidths = []
    labels = []
    line = file.readline()
    while line != "\n":
        line = line.split(",")
        sepalLengths.append(float(line[0]))
        sepalWidths.append(float(line[1]))
        petalLenghts.append(float(line[2]))
        petalWidths.append(float(line[3]))
        inputs.append([float(line[0]), float(line[1]), float(line[2]), float(line[3])])
        label = line[4].split("\n")[0]
        outputs.append(label)
        if label not in labels:
            labels.append(label)
        line = file.readline()
    file.close()

    return inputs, outputs, labels, sepalLengths, sepalWidths, petalLenghts, petalWidths


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


def plotData(x, y, z, c, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    img = ax.scatter(x, y, z, c=c, cmap=plt.hot())
    fig.colorbar(img)
    plt.title(title)
    plt.show()
