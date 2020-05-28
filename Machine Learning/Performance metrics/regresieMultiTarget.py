def L1(real, computed):
    errors = []
    for i in range(len(real[0])):
        error = sum(abs(r[i] - c[i]) for r, c in zip(real, computed)) / len(real)
        errors.append(error)
    return errors


def L2(real, computed):
    errors = []
    for i in range(len(real[0])):
        error = (sum((r[i] - c[i]) ** 2 for r, c in zip(real, computed)) / len(real)) ** 0.5
        errors.append(error)
    return errors


if __name__ == '__main__':
    real = [[1.75, 3.25, 4.05], [4.75, 9.15, 7.15], [2.75, 3.25, 4.95], [4.25, 6.5, 1.25], [4.25, 5.6, 7.45],
            [10.0, 7.5, 6.25], [8.05, 9.25, 1.45], [5.0, 6.25, 7.1], [6.2, 8.5, 4.5], [3.5, 6.3, 6.25]]
    computed = [[1.75, 3.25, 5.1], [2.3, 9.5, 4.8], [5.2, 3.15, 5.0], [4.3, 7.0, 2.1], [4.25, 4.5, 8.75],
                [9.3, 6.55, 5.95], [8.2, 9.15, 2.5], [6.5, 5.25, 7.55], [6.4, 8.75, 5.65], [4.75, 7.0, 5.25]]

    print("ErrorL1: " + str(L1(real, computed)))
    print("ErrorL2: " + str(L2(real, computed)))
