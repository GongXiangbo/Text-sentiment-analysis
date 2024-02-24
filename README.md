阅读中文版本: [文本情感分类](README.zh.md)
# Text-sentiment-classification
This is a machine learning and deep learning practice project. In this project, you need to predict the sentiment of given content on Twitter. In short, the emotions provided in this task are either positive or negative.

## Setting
Clone the repository:
```
git clone https://github.com/GongXiangbo/Text-sentiment-classification.git
```
Run the command:
```
pip install accelerate -U
```
Download the required packages
```
pip install -r ./Text-sentiment-classification/requirements.txt
```

## Train
To train the original SICK model execute the following command: 
```
python ./Text-sentiment-classification/train.py 
```
During training, when it outputs ```wandb: Enter your choice:```, you can just enter 3.

You can set the following parameters:

- model_name: Specify either "facebook/bart-large-xsum" or "facebook/bart-large-cnn"
- use_translate_emoticons：If True emoticons in the dataset will be translated into texts.
- use_remove_emoticons: If True emoticons in the dataset will be removed.
- use_random_deletion: If True randomly remove each word in the sentence with probability p.
- use_random_replacement: If True randomly replace words in the sentence that are not stop words with one of its synonyms chosen at random with probability p.
- p: The probability of random deletion or random replacement.


