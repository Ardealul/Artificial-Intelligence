import csv
import numpy as np

def loadData(fileName):
    data = []
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                dataNames = row
            else:
                data.append(row)
            line_count += 1

    inputs = [data[i][0] for i in range(len(data))]
    outputs = [data[i][1] for i in range(len(data))]
    labelNames = list(set(outputs))

    return inputs, outputs, labelNames


def featureComputation(model, data):
    features = []
    phrases = [phrase.split() for phrase in data]
    for phrase in phrases:
        # compute the embeddings of all the words from a phrase (words of more than 2 characters) known by the model
        vectors = [model[word] for word in phrase if (len(word) > 2) and (word in model.vocab.keys())]
        if len(vectors) == 0:
            result = [0.0] * model.vector_size
        else:
            result = np.sum(vectors, axis=0) / len(vectors)
        features.append(result)
    return features
