import glob
import pandas as pd
import csv
import json


# SCRIPT used to download news from dataset:
# mysql -u dragroot -p -e 'SELECT na.articleid, na.title, na.newsoutletid, at.extracttext FROM newsarticle as na JOIN articletext as at WHERE na.articleid = at.articleid AND (na.newsoutletid = 3 OR na.newsoutletid = 20669);' newsdb > wsj_dataset.csv

# Dictionary of outlets names and their ids
# manually remove issues and merge if multiple sources are available.
# Outlet ids = {'wsj': [3, 20669], 'foxnews': [18], 'marketwatch': [135], 'washingtonpost': [9, 80], 'cnn': [11], 'bbc': [30, 923]}
# Outlet sizes = {'wsj': 3307, 'foxnews': 5204, 'marketwatch': 3418, 'washingtonpost': 11371, 'cnn': 528, 'bbc': 2490}
# Outlet bias = {'wsj': 'right_center', 'foxnews': 'right', 'marketwatch': 'neutral_right', 'washingtonpost': 'left_center', 'cnn': 'left', 'bbc': 'neutral_left'}
# # Politics texts = {'wsj': 575, 'foxnews': 2275, 'marketwatch': 984, 'washingtonpost': 4875, 'cnn': 271, 'bbc': 609}
# articles between: 2015-10-28 and 2016-12-01

# # News dataset
# for file in glob.glob('*.csv'):
#     texts = []
#     df = pd.read_csv(file, header=None, quoting=csv.QUOTE_ALL)
#     for index, row in df.iterrows():
#         if 'election' in row[3] or 'ballot' in row[3] or 'republican' in row[3] or 'GOP' in row[3] or 'democrat' in row[3]:
#             texts.append(row[3])
#     texts = pd.DataFrame(texts).sample(frac=1)
#     texts.to_csv('texts/' + file, header=False, index=False)
#
# # Alternative possibility: take data just for 2015-10-28 and 2016-12-01 period
# # split row[3] into list by " " and do intersection of the two lists @list(set(lst1) & set(lst2))@
# # if len of intersection is > 3 (including words Clinton, Trump, Sanders) add text into dataset
# #
# for file in glob.glob('texts/*.csv'):
#     df = pd.read_csv(file, header=None)[:50].sample(frac=1).reset_index(drop=True)
#     train = []
#     test = []
#     validation = []
#     for index, row in df.iterrows():
#         text = row[0].replace('\\n', ' ').split('. ')
#         if index < 5:
#             for i in range(len(text) - 3):
#                 test.append([int(row[1]), text[i] + '. ' + text[i + 1] + '. ' + text[i + 2] + '. ' + text[i + 3]])
#         elif index < 10:
#             for i in range(len(text) - 3):
#                 validation.append([int(row[1]), text[i] + '. ' + text[i + 1] + '. ' + text[i + 2] + '. ' + text[i + 3]])
#         else:
#             for i in range(len(text) - 3):
#                 train.append([int(row[1]), text[i] + '. ' + text[i + 1] + '. ' + text[i + 2] + '. ' + text[i + 3]])
#     pd.DataFrame(test).sample(frac=1).to_csv(file.replace('.', '_test.').replace('text', 'dataset'), header=False, index=False)
#     pd.DataFrame(validation).sample(frac=1).to_csv(file.replace('.', '_validation.').replace('text', 'dataset'), header=False, index=False)
#     pd.DataFrame(train).sample(frac=1).to_csv(file.replace('.', '_train.').replace('text', 'dataset'), header=False, index=False)


# Twitter dataset
with open('election.json', 'r') as json_file:
    all_data = []
    i = 0
    while True:
        data = json_file.readline()
        if data != '':
            data = json.loads(data)
            if 'text' in data.keys() and data['text'][0:4] != 'RT @':
                print(i)
                i += 1
                data['text'] = data['text'].encode('UTF-8', 'strict')
                all_data.append([data['created_at'], data['id'], data['text'], data['user']['screen_name'],
                                 data['user']['description']])
        else:
            break
    with open('election.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(all_data)

# df = pd.read_csv('election.csv', header=None).sample(frac=1)
# df[:1000].to_csv('election_test.csv', header=False, index=False)
# df[1000:].to_csv('election_unlabeled.csv', header=False, index=False)
