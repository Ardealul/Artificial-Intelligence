def accuracy(real, computed):
    return sum([1 if real[i] == computed[i] else 0 for i in range(len(real))]) / len(real)


def truePositive(real, computed, label):
    return sum([1 if real[i] == label and computed[i] == label else 0 for i in range(len(real))])


def falsePositive(real, computed, label):
    return sum([1 if real[i] != label and computed[i] == label else 0 for i in range(len(real))])


def falseNegative(real, computed, label):
    return sum([1 if real[i] == label and computed[i] != label else 0 for i in range(len(real))])


if __name__ == '__main__':
    real = ['alpha', 'beta', 'gamma', 'alpha', 'alpha', 'alpha', 'gamma', 'beta', 'gamma', 'alpha',
            'beta', 'gamma', 'beta', 'alpha', 'alpha', 'gamma', 'beta', 'gamma', 'alpha', 'beta',
            'gamma', 'beta', 'alpha', 'alpha', 'alpha', 'gamma', 'gamma', 'beta', 'alpha', 'gamma']
    computed = ['beta', 'beta', 'alpha', 'alpha', 'alpha', 'alpha', 'gamma', 'beta', 'beta', 'alpha',
                'beta', 'gamma', 'alpha', 'alpha', 'alpha', 'beta', 'gamma', 'beta', 'alpha', 'alpha',
                'beta', 'gamma', 'alpha', 'alpha', 'beta', 'gamma', 'gamma', 'gamma', 'alpha', 'gamma']

    print("Accuracy: " + str(accuracy(real, computed) * 100) + "%")

    alphaTP = truePositive(real, computed, 'alpha')
    betaTP = truePositive(real, computed, 'beta')
    gammaTP = truePositive(real, computed, 'gamma')

    alphaFP = falsePositive(real, computed, 'alpha')
    betaFP = falsePositive(real, computed, 'beta')
    gammaFP = falsePositive(real, computed, 'gamma')

    alphaFN = falseNegative(real, computed, 'alpha')
    betaFN = falseNegative(real, computed, 'beta')
    gammaFN = falseNegative(real, computed, 'gamma')

    alphaPrecision = alphaTP / (alphaTP + alphaFP)
    betaPrecision = betaTP / (betaTP + betaFP)
    gammaPrecision = gammaTP / (gammaTP + gammaFP)

    alphaRecall = alphaTP / (alphaTP + alphaFN)
    betaRecall = betaTP / (betaTP + betaFN)
    gammaRecall = gammaTP / (gammaTP + gammaFN)

    print("-----True Positive-----")
    print("AlphaTP: " + str(alphaTP))
    print("BetaTP: " + str(betaTP))
    print("GammaTP: " + str(gammaTP))

    print("-----False Positive-----")
    print("AlphaFP: " + str(alphaFP))
    print("BetaFP: " + str(betaFP))
    print("GammaFP: " + str(gammaFP))

    print("-----False Negative-----")
    print("AlphaFN: " + str(alphaFN))
    print("BetaFN: " + str(betaFN))
    print("GammaFN: " + str(gammaFN))

    print("-----Precision-----")
    print("AlphaPrecision: " + str(alphaPrecision * 100) + "%")
    print("BetaPrecision: " + str(betaPrecision * 100) + "%")
    print("GammaPrecision: " + str(gammaPrecision * 100) + "%")

    print("-----Recall-----")
    print("AlphaRecall: " + str(alphaRecall * 100) + "%")
    print("BetaRecall: " + str(betaRecall * 100) + "%")
    print("GammaRecall: " + str(gammaRecall * 100) + "%")
