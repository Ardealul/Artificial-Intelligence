from utils import loadData, featureComputation
import numpy as np


if __name__ == '__main__':
    # inputs, outputs, labelNames = loadData("spam.csv")
    inputs, outputs, labelNames = loadData("reviews_mixed.csv")
    # print(inputs[:5])
    # print(outputs[:5])
    # print(labelNames)

    np.random.seed(5)
    indexes = [i for i in range(len(inputs))]
    trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)  # 80% train data
    testSample = [i for i in indexes if i not in trainSample]  # 20% test data

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]

    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                 "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                 "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
                 "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
                 "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because",
                 "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into",
                 "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out",
                 "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where",
                 "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
                 "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just",
                 "don", "should", "now"]

    # representation 1: Bag of Words
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(stop_words=stopwords)

    trainFeatures = vectorizer.fit_transform(trainInputs)
    testFeatures = vectorizer.transform(testInputs)

    print("vocab: " + str(vectorizer.vocabulary_))

    # representation 2: TF-IDF- word granularity
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(stop_words=stopwords)

    trainFeatures = vectorizer.fit_transform(trainInputs)
    testFeatures = vectorizer.transform(testInputs)

    print("vocab: " + str(vectorizer.vocabulary_))

    # representation 3: embedded features extracted by a pre-train model (in fact, word2vec pretrained model)
    import gensim
    word2vecModel300 = gensim.models.KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True, limit=100000)
    print(word2vecModel300.most_similar("support")[:3])
    # print(word2vecModel300["house"])

    trainFeatures = featureComputation(word2vecModel300, trainInputs)
    testFeatures = featureComputation(word2vecModel300, testInputs)

    # unsupervised classification (= clustering) of data
    from sklearn.cluster import KMeans

    unsupervisedClassifier = KMeans(n_clusters=2, random_state=0)
    unsupervisedClassifier.fit(trainFeatures)
    computedTestIndexes = unsupervisedClassifier.predict(testFeatures)
    computedTestOutputs = [labelNames[index] for index in computedTestIndexes]

    # measure performance
    from sklearn.metrics import accuracy_score
    print("accuracy: ", accuracy_score(testOutputs, computedTestOutputs))


