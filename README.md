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
You can set the following parameters:

- epoch: default=3
- lr：default=2.4e-5
- train_batch_size: default=15
- test_batch_size: default=1
- warm_up: default=1000
- weight_decay: default=1e-2
- max_len: default=128
- model: default="bert-large-uncased", it is also recommended to use "roberta-large" or "xlnet-large-cased"
Example:
```
python ./Text-sentiment-classification/train.py --epoch 3 --lr 2.4e-5 --model "roberta-large"
```

