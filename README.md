# Biased News Data Influence on Classifying Social Media Posts

**Abstract**: A common task among social scientists is to mine and interpret public opinion using social media data. Scientists tend to employ off-theshelf state-of-the-art short-text classification models. Those algorithms, however, require a large amount of labeled data. Recent efforts aim to decrease the compulsory number of labeled data via self-supervised learning and fine-tuning. In this work, we explore the use of news data on a specific topic in fine-tuning opinion mining models learned from social media data, such as Twitter. Particularly, we investigate the influence of biased news data on models trained on Twitter data by considering both the balanced and unbalanced cases. Results demonstrate that tuning with biased news data of different properties changes the classification accuracy up to 9.5%. The experimental studies reveal that the characteristics of the text of the tuning dataset, such as bias, vocabulary diversity and writing style, are essential for the final classification results, while the size of the data is less consequential. Moreover, a state-of-the-art algorithm is not robust on unbalanced twitter dataset, and it exaggerates when predicting the most frequent label.

```
@inproceedings{stanojevic2019biased,
  title={Biased News Data Influence on Classifying Social Media Posts.},
  author={Stanojevic, Marija and Alshehri, Jumanah and Dragut, Eduard C and Obradovic, Zoran},
  year={2019}
}
```

# Datasets:
**News**: Unfortunately, those data are not ours to share, but we are sharing here dataset which contains links of the news articles that we used. You can download those articles and replace URL with the article text to repeat the experiments.

**Twitter**: Unfortunately, those data are not ours to share, but we are sharing here https://drive.google.com/file/d/13UVJK0ejtcA78bHbz7zV6oE1zJlAKQAU/view?usp=sharing dataset which contains IDs of the tweets that we used (second column). You can use Twitter API to download those tweets. Data were extracted using timeframe and hashtags described in a paper.

# Code notes:
This is the main part of the code. Code used to download and transform twitter datasets, we can't share due to Twitter policy.
