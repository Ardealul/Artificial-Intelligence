import random


# shuffle data from x and y in parallel
def shuffle(x, y):
    index = [i for i in range(len(x))]
    random.shuffle(index)
    xnew = [x[i] for i in index]
    ynew = [y[i] for i in index]

    return xnew, ynew


class MySGDRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = []

    def fit(self, x, y, learningRate=0.01, noEpochs=1000):
        self.coef_ = [0.0 for _ in range(len(x[0]) + 1)]
        # self.coef_ = [random.random() for _ in range(len(x[0]) + 1)]
        for epoch in range(noEpochs):
            # x, y = shuffle(x, y)  # TBA: shuffle the training examples in order to prevent cycles
            for i in range(len(x)):  # for each sample from the training data
                ycomputed = self.eval(x[i])  # estimate the output
                crtError = ycomputed - y[i]  # compute the error for the current sample
                for j in range(0, len(x[0])):  # update the coefficients
                    self.coef_[j] = self.coef_[j] - learningRate * crtError * x[i][j]
                self.coef_[len(x[0])] = self.coef_[len(x[0])] - learningRate * crtError * 1
            # print("epoch " + str(epoch) + ": " + str(self.coef_))

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
