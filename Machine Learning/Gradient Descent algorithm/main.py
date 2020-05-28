import os
import numpy as np

from sklearn import linear_model
from sklearn.metrics import mean_squared_error

from utils import loadDataTwoInputs, L1, L2, meanSquareError, plotData2ForBi, plotDataForBi, plotDataForUni, \
    plotData2ForUni
from StochasticGD import MySGDRegression
from BatchGD import MyBGDRegression
from utils import zScoreNormalization


# for univariate regression
def UnivariateStochasticTool():
    regressor = linear_model.SGDRegressor(alpha=0.01, max_iter=1000)

    xx = [[el] for el in trainGdp]
    regressor.partial_fit(xx, trainOutputs)
    w0, w1 = regressor.intercept_[0], regressor.coef_[0]
    w = [w0, w1]
    print("-----with tool-----")
    print("Regression for attribute: GDP")
    print("\tThe learnt model: f(X,w) = " + str(w0) + " + " + str(w1) + " * X")

    computedOutputs = regressor.predict([[x] for x in testGdp])
    print("\tPrediction error (tool): ", str(mean_squared_error(testOutputs, computedOutputs)))
    print("\tPrediction error (manual): ", str(meanSquareError(testOutputs, computedOutputs)))

    plotDataForUni(gdpData, outputs, w, "Train & test data")
    plotDataForUni(trainGdp, trainOutputs, w, "Train data and the learnt model")
    plotData2ForUni(testGdp, testOutputs, computedOutputs, "Computed vs real test data")


# for bivariate regression
def BivariateStochasticTool():
    regressor = linear_model.SGDRegressor(alpha=0.01, max_iter=1000)

    regressor.fit(trainInputs, trainOutputs)
    w0, w1, w2 = regressor.intercept_[0], regressor.coef_[0], regressor.coef_[1]
    w = [w0, w1, w2]
    print("-----with tool-----")
    print("Regression for attributes: GDP & Freedom")
    print("\tThe learnt model: f(X,w) = " + str(w0) + " + " + str(w1) + " * X1 + " + str(w2) + " * X2")

    computedTestOutputs = regressor.predict(testInputs)
    print("\tPrediction error (tool): ", str(mean_squared_error(testOutputs, computedTestOutputs)))
    print("\tPrediction error (manual): ", str(meanSquareError(testOutputs, computedTestOutputs)))

    plotDataForBi(gdpData, freedomData, outputs, w, "Train & test data")
    plotDataForBi(trainGdp, trainFreedom, trainOutputs, w, "Train data and the learnt model")
    plotData2ForBi(testGdp, testFreedom, testOutputs, computedTestOutputs, "Computed(green) vs real(red) test data")


# for univariate regression
def UnivariateStochastic():
    regressor = MySGDRegression()

    xx = [[el] for el in trainGdp]
    regressor.fit(xx, trainOutputs)
    w0, w1 = regressor.intercept_, regressor.coef_[0]
    w = [w0, w1]
    print("-----manual stochastic-----")
    print("Regression for attribute: GDP")
    print("\tThe learnt model: f(X,w) = " + str(w0) + " + " + str(w1) + " * X")

    computedOutputs = regressor.predict([[x] for x in testGdp])
    print("\tPrediction error (tool): ", str(mean_squared_error(testOutputs, computedOutputs)))
    print("\tPrediction error (manual): ", str(meanSquareError(testOutputs, computedOutputs)))

    plotDataForUni(gdpData, outputs, w, "Train & test data")
    plotDataForUni(trainGdp, trainOutputs, w, "Train data and the learnt model")
    plotData2ForUni(testGdp, testOutputs, computedOutputs, "Computed vs real test data")


# for bivariate regression
def BivariateStochastic():
    regressor = MySGDRegression()

    regressor.fit(trainInputs, trainOutputs)
    w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
    w = [w0, w1, w2]
    print("-----manual stochastic-----")
    print("Regression for attributes: GDP & Freedom")
    print("\tThe learnt model: f(X,w) = " + str(w0) + " + " + str(w1) + " * X1 + " + str(w2) + " * X2")

    computedTestOutputs = regressor.predict(testInputs)
    print("\tPrediction error (tool): ", str(mean_squared_error(testOutputs, computedTestOutputs)))
    print("\tPrediction error (manual): ", str(meanSquareError(testOutputs, computedTestOutputs)))

    plotDataForBi(gdpData, freedomData, outputs, w, "Train & test data")
    plotDataForBi(trainGdp, trainFreedom, trainOutputs, w, "Train data and the learnt model")
    plotData2ForBi(testGdp, testFreedom, testOutputs, computedTestOutputs, "Computed(green) vs real(red) test data")


# mini-batch gd for univariate regression with tool
def UnivariateMiniBatchTool(noBatches):
    batchSize = len(trainGdp) // noBatches
    regressor = linear_model.SGDRegressor(alpha=0.01, max_iter=1000, average=batchSize, shuffle=False)

    xx = [[el] for el in trainGdp]
    regressor.fit(xx, trainOutputs)
    w0, w1 = regressor.intercept_[0], regressor.coef_[0]
    w = [w0, w1]
    print("-----with tool-----")
    print("Regression for attribute: GDP")
    print("\tThe learnt model: f(X,w) = " + str(w0) + " + " + str(w1) + " * X")

    computedOutputs = regressor.predict([[x] for x in testGdp])
    print("\tPrediction error (tool): ", str(mean_squared_error(testOutputs, computedOutputs)))
    print("\tPrediction error (manual): ", str(meanSquareError(testOutputs, computedOutputs)))

    plotDataForUni(gdpData, outputs, w, "Train & test data")
    plotDataForUni(trainGdp, trainOutputs, w, "Train data and the learnt model")
    plotData2ForUni(testGdp, testOutputs, computedOutputs, "Computed vs real test data")


# mini-batch gd for bivariate regression with tool
def BivariateMiniBatchTool(noBatches):
    batchSize = len(trainInputs) // noBatches
    regressor = linear_model.SGDRegressor(alpha=0.01, max_iter=1000, average=batchSize, shuffle=False)

    regressor.fit(trainInputs, trainOutputs)
    w0, w1, w2 = regressor.intercept_[0], regressor.coef_[0], regressor.coef_[1]
    w = [w0, w1, w2]
    print("-----with tool-----")
    print("Regression for attributes: GDP & Freedom")
    print("\tThe learnt model: f(X,w) = " + str(w0) + " + " + str(w1) + " * X1 + " + str(w2) + " * X2")

    computedTestOutputs = regressor.predict(testInputs)
    print("\tPrediction error (tool): ", str(mean_squared_error(testOutputs, computedTestOutputs)))
    print("\tPrediction error (manual): ", str(meanSquareError(testOutputs, computedTestOutputs)))

    plotDataForBi(gdpData, freedomData, outputs, w, "Train & test data")
    plotDataForBi(trainGdp, trainFreedom, trainOutputs, w, "Train data and the learnt model")
    plotData2ForBi(testGdp, testFreedom, testOutputs, computedTestOutputs, "Computed(green) vs real(red) test data")


# for univariate regression
def UnivariateMiniBatch(nrBatches):
    regressor = MyBGDRegression()
    print("-----manual batch-----")

    xx = [[el] for el in trainGdp]
    regressor.fit(xx, trainOutputs, nrBatches)
    w0, w1 = regressor.intercept_, regressor.coef_[0]
    w = [w0, w1]
    print("Regression for attribute: GDP")
    print("\tThe learnt model: f(X,w) = " + str(w0) + " + " + str(w1) + " * X")

    computedOutputs = regressor.predict([[x] for x in testGdp])
    print("\tPrediction error (tool): ", str(mean_squared_error(testOutputs, computedOutputs)))
    print("\tPrediction error (manual): ", str(meanSquareError(testOutputs, computedOutputs)))

    plotDataForUni(gdpData, outputs, w, "Train & test data")
    plotDataForUni(trainGdp, trainOutputs, w, "Train data and the learnt model")
    plotData2ForUni(testGdp, testOutputs, computedOutputs, "Computed vs real test data")


# for bivariate regression
def BivariateMiniBatch(nrBatches):
    regressor = MyBGDRegression()
    print("-----manual batch-----")

    regressor.fit(trainInputs, trainOutputs, nrBatches)
    w0, w1, w2 = regressor.intercept_, regressor.coef_[0], regressor.coef_[1]
    w = [w0, w1, w2]
    print("Regression for attributes: GDP & Freedom")
    print("\tThe learnt model: f(X,w) = " + str(w0) + " + " + str(w1) + " * X1 + " + str(w2) + " * X2")

    computedTestOutputs = regressor.predict(testInputs)
    print("\tPrediction error (tool): ", str(mean_squared_error(testOutputs, computedTestOutputs)))
    print("\tPrediction error (manual): ", str(meanSquareError(testOutputs, computedTestOutputs)))

    plotDataForBi(gdpData, freedomData, outputs, w, "Train & test data")
    plotDataForBi(trainGdp, trainFreedom, trainOutputs, w, "Train data and the learnt model")
    plotData2ForBi(testGdp, testFreedom, testOutputs, computedTestOutputs, "Computed(green) vs real(red) test data")


if __name__ == '__main__':
    crtDir = os.getcwd()
    filePath = os.path.join(crtDir, 'data.csv')
    inputs, outputs = loadDataTwoInputs(filePath, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score')
    gdpData = [i[0] for i in inputs]
    freedomData = [i[1] for i in inputs]

    # print('GDP: ', list(gdpData[i] for i in range(5)))
    # print('Freedom: ', list(freedomData[i] for i in range(5)))
    # print('Happiness: ', outputs[:5])

    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)  # 80% train data
    testSample = [i for i in indexes if i not in trainSample]  # 20% test data

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    trainInputs, testInputs, trainOutputs, testOutputs = \
        zScoreNormalization(trainInputs, testInputs, trainOutputs, testOutputs)

    trainGdp = [i[0] for i in trainInputs]
    trainFreedom = [i[1] for i in trainInputs]
    testGdp = [i[0] for i in testInputs]
    testFreedom = [i[1] for i in testInputs]

    # UnivariateStochasticTool()
    # BivariateStochasticTool()

    # UnivariateStochastic()
    # BivariateStochastic()

    # UnivariateMiniBatchTool(1)
    # BivariateMiniBatchTool(1)

    # UnivariateMiniBatch(1)
    BivariateMiniBatch(1)
