# Text-sentiment-classification
This is a deep learning practice project. In this project, you need to predict the sentiment of given content on Twitter. In short, the emotions provided in this task are either positive or negative.

The folder "data" contains the provided tweet data set in csv format, where train.csv is the training set, which contains 179995 tweets, and test.csv is the test set, which includes 44999 tweets. The sentiment of the tweet is reported on the feature named sentiment and is equal to 1 for the Positive class and 0 for the Negative one.

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
To train, execute the following command: 
```
python ./Text-sentiment-classification/train.py 
```
You can set the following parameters:

- epoch: default=3
- lr：default=2e-5
- train_batch_size: default=15
- test_batch_size: default=1
- warm_up: default=500
- weight_decay: default=1e-2
- max_len: default=64
- model: default="bert-large-uncased", it is also recommended to use "roberta-large"

Example:
```
python ./Text-sentiment-classification/train.py --epoch 5 --lr 3.2e-5 --model "bert-large-uncased"
```
## Results

| Model | Accuracy | F1 (Macro) |
|----------|----------|----------|
| roberta-large | 88.68% | 88.42% |
| bert-large-uncased | 85.46% | 85.09% |
