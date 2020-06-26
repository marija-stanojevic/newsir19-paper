import fasttext
import os
import pandas as pd
import string
import re


def reform_train(data):
    train = []
    for index, row in data.iterrows():
        train.append('__label__' + str(row.iloc[1] + 1) + ' ' + str(row.iloc[0]))
    return pd.DataFrame(train)


def train_fast_text(news, pretrained, dim):
    train_data = pd.DataFrame()
    for outlet in news:
        data = pd.read_csv(f'datasets/{outlet}_train.csv', header=None)
        train_data = pd.concat([train_data, data])
    reform_train(train_data).to_csv('hidden_train.csv', index=False, header=False)
    classifier = fasttext.supervised('hidden_train.csv', 'model', pretrained_vectors=pretrained, dim=dim)
    os.remove('hidden_train.csv')
    os.remove('model.bin')
    return classifier


def predict_label_fast_text(news, classifier):
    unlabeled_data = pd.read_csv('election_test.csv').iloc[:205, 2].values.astype('U').tolist()
    for i in range(len(unlabeled_data)):
        unlabeled_data[i] = re.sub(r'https?://\S+', '', unlabeled_data[i], flags=re.MULTILINE)
        unlabeled_data[i] = unlabeled_data[i].translate(str.maketrans('', '', string.punctuation))
    labels = classifier.predict_proba(unlabeled_data)
    for i in range(len(labels)):
        labels[i] = [int(labels[i][0][0]), labels[i][0][1]]
    labels = pd.DataFrame(labels)
    labels[0] -= 1
    name = ''
    for outlet in news:
        name += outlet + '_'
    labels.to_csv(f'{name}predicted_labels.csv', index=False, header=False)


def main():
    for news in [['wsj'], ['foxnews'], ['cnn'], ['washingtonpost'], ['bbc'], ['marketwatch'],
                 ['wsj', 'foxnews', 'marketwatch'], ['washingtonpost', 'bbc', 'cnn'],
                 ['wsj', 'foxnews', 'marketwatch', 'washingtonpost', 'bbc', 'cnn']]:
        classifier = train_fast_text(news, 'wiki-news-300d-1M.vec', 300)
        predict_label_fast_text(news, classifier)


if __name__ == '__main__':
    main()


# general data => news data => classification score;
# general data => twitter data => classification score;
# general data => news data => twitter data => classification score;
# general data => news data => users => classification score;
# how much those scores differ; what examples are mislabeled in each case; what are low confidence examples
# what effect news bias has on twitter classification
