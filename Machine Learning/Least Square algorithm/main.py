import os

import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from utils import loadData, meanSquareError, L1, L2, plotData, plotData2, plotDataHistogram
from regression import MyLinearBivariateRegression

if __name__ == '__main__':
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data.csv')
    inputs, outputs = loadData(filePath, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score')
    gdpData = [i[0] for i in inputs]
    freedomData = [i[1] for i in inputs]

    # print('GDP:  ', list(gdpData[i] for i in range(5)))
    # print('Freedom:  ', list(freedom[i] for i in range(5)))
    # print('Happiness: ', outputs[:5])

    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)  # 80% train data
    testSample = [i for i in indexes if i not in trainSample]  # 20% test data

    trainInputs = [inputs[i] for i in trainSample]
    trainGdp = [gdpData[i] for i in trainSample]
    trainFreedom = [freedomData[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    testInputs = [inputs[i] for i in testSample]
    testGdp = [gdpData[i] for i in testSample]
    testFreedom = [freedomData[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    # tool
    regressor = linear_model.LinearRegression()
    w = regressor.fit(trainInputs, trainOutputs)
    w0 = w.intercept_
    w1, w2 = w.coef_
    w = [w0, w1, w2]
    print("-----with tool-----")
    print("The learnt model: f(X,w) = " + str(w0) + " + " + str(w1) + " * X1 + " + str(w2) + " * X2")

    # print("Real: " + str(testOutputs))
    # print("Computed: " + str(list(regressor.predict(testInputs))))

    # print("Prediction error (tool): ", str(mean_squared_error(testOutputs, regressor.predict(testInputs))))
    # print("Prediction error (manual): ", str(meanSquareError(testOutputs, regressor.predict(testInputs))))

    # manual
    regressor2 = MyLinearBivariateRegression()
    regressor2.fit(trainInputs, trainOutputs)
    wPrim = [regressor2.intercept_, regressor2.coef_[0], regressor2.coef_[1]]
    print("-----manual-----")
    print("The learnt model: f(X,w) = " + str(wPrim[0]) + " + " + str(wPrim[1]) + " * X1 + " + str(wPrim[2]) + " * X2")

    # print("Real: " + str(testOutputs))
    # print("Computed: " + str(list(regressor2.predict(testInputs))))

    print("-----performance-----")
    print("Prediction error (tool): ", str(mean_squared_error(testOutputs, regressor2.predict(testInputs))))
    print("Prediction error (manual): ", str(meanSquareError(testOutputs, regressor2.predict(testInputs))))

    plotDataHistogram(gdpData, 'GDP')
    plotDataHistogram(freedomData, 'Freedom')
    plotDataHistogram(outputs, 'Happiness score')

    # for train and test data
    plotData(gdpData, freedomData, outputs, w, "Train & test data")

    # for train data
    plotData(trainGdp, trainFreedom, trainOutputs, w, "Train data and the learnt model")

    # for test data
    computedTestOutputs = regressor2.predict(testInputs)
    plotData2(testGdp, testFreedom, testOutputs, computedTestOutputs, "Computed(green) vs real(red) test data")
