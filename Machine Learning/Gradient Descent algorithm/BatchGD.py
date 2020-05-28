import random


# shuffle data from x and y in parallel
def shuffle(x, y):
    index = [i for i in range(len(x))]
    random.shuffle(index)
    xnew = [x[i] for i in index]
    ynew = [y[i] for i in index]

    return xnew, ynew


class MyBGDRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    # mini-batch algorithm
    def fit(self, x, y, noBatches=1, learningRate=0.005, noEpochs=1000):
        self.coef_ = [0.0 for _ in range(len(x[0]) + 1)]
        # self.coef_ = [random.random() for _ in range(len(x[0]) + 1)]
        batchSize = len(x) // noBatches
        listOfBatches = []
        for i in range(0, len(x), batchSize):
            mini_batch_x = x[i:i + batchSize]
            mini_batch_y = y[i:i + batchSize]
            listOfBatches.append([mini_batch_x, mini_batch_y])
            if i + batchSize > len(x):
                mini_batch_x = x[i: len(x) + 1]
                mini_batch_y = y[i: len(x) + 1]
                listOfBatches.append([mini_batch_x, mini_batch_y])
        for epoch in range(noEpochs):
            for batch in listOfBatches:
                w = [0.0 for _ in range(len(x[0]) + 1)]
                mini_batch_x = batch[0]
                mini_batch_y = batch[1]
                for i in range(len(mini_batch_x)):
                    ycomputed = self.eval(mini_batch_x[i])
                    crtError = ycomputed - mini_batch_y[i]
                    for j in range(0, len(mini_batch_x[0])):
                        w[j] += crtError * mini_batch_x[i][j]
                    w[len(mini_batch_x[0])] += crtError * 1

                for i in range(len(mini_batch_x[0]) + 1):
                    self.coef_[i] = self.coef_[i] - learningRate * (w[i] / len(mini_batch_x))

        self.intercept_ = self.coef_[-1]
        self.coef_ = self.coef_[:-1]

    # batch algorithm
    def fit2(self, x, y, learningRate=0.01, noEpochs=1000):
        self.coef_ = [0.0 for _ in range(len(x[0]) + 1)]
        # self.coef_ = [random.random() for _ in range(len(x[0]) + 1)]
        for epoch in range(noEpochs):
            w = [0.0 for _ in range(len(x[0]) + 1)]
            # x, y = shuffle(x, y)
            for i in range(len(x)):
                ycomputed = self.eval(x[i])
                crtError = ycomputed - y[i]
                for j in range(0, len(x[0])):
                    w[j] += crtError * x[i][j]
                w[len(x[0])] += crtError * 1

            for i in range(len(x[0]) + 1):
                self.coef_[i] = self.coef_[i] - learningRate * (w[i] / len(x))

        self.intercept_ = self.coef_[-1]
        self.coef_ = self.coef_[:-1]

    def eval(self, xi):
        yi = self.coef_[-1]  # w0
        for j in range(len(xi)):
            yi += self.coef_[j] * xi[j]  # w0 + w1*x1 + ...
        return yi

    def predict(self, x):
        yComputed = [self.eval(xi) for xi in x]
        return yComputed
