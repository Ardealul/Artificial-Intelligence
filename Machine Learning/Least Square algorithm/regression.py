from matrixOperations import multiply, transposed, inverse


# build and return matrix X
def buildX(x):
    noCols = len(x[0])
    noRows = len(x)
    result = []
    for i in range(noRows):
        row = [1.0]
        for j in range(noCols):
            row.append(x[i][j])
        result.append(row)
    return result


# build and return matrix Y
def buildY(y):
    noRows = len(y)
    result = []
    for i in range(noRows):
        row = [y[i]]
        result.append(row)
    return result


class MyLinearBivariateRegression:
    def __init__(self):
        self.intercept_ = 0.0
        self.coef_ = [0.0, 0.0]

    # learn a linear bivariate regression model by using training inputs (x) and outputs (y)
    def fit(self, x, y):
        x = buildX(x)
        y = buildY(y)

        # xT * x
        result = multiply(transposed(x), x)
        # inverse(xT * x)
        result = inverse(result)
        # inverse(xT * x) * xT
        result = multiply(result, transposed(x))
        # inverse(xT * x) * xT * y
        result = multiply(result, y)

        self.intercept_ = result[0][0]  # w0
        self.coef_[0] = result[1][0]  # w1
        self.coef_[1] = result[2][0]  # w2

    # predict the outputs for some new inputs (by using the learnt model)
    def predict(self, x):
        if isinstance(x[0], list):  # a list of inputs
            return [self.intercept_ + self.coef_[0] * el[0] + self.coef_[1] * el[1] for el in x]
        else:  # one input
            return self.intercept_ + self.coef_[0] * x[0] + self.coef_[1] * x[1]
