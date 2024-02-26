English version: [Text sentiment classification](README.en.md)
# 推特文本情感分析
推特文本情感分析，你需要预测推特推文的情绪。

data文件夹中包含提供的csv格式的推特推文数据集，其中train.csv为训练集，包含179995条推文，test.csv为测试集，包括44999条推文。sentiment列代表推文的情感，1为积极类别，0为消极类别。

## 设置
克隆仓库：
```
git clone https://github.com/GongXiangbo/Text-sentiment-classification.git
```
运行命令：
```
pip install accelerate -U
```
下载所需要的包：
```
pip install -r ./Text-sentiment-classification/requirements.txt
```
## 训练
要训练，请执行以下命令：
```
python ./Text-sentiment-classification/train.py 
```
你可以设置以下参数：

- epoch: 默认为3
- lr：默认为1.2e-5
- train_batch_size: 默认为16
- test_batch_size: 默认为4
- warm_up: 默认为500
- weight_decay: 默认为1e-2
- max_len: 默认为128
- model: 默认为"bert-large-uncased", 也建议使用“roberta-large”

例子:
```
python ./Text-sentiment-classification/train.py --epoch 5 --lr 3.2e-5 --model "bert-large-uncased"
```
## 实验结果
| Model | Accuracy | F1 (Macro) |
|----------|----------|----------|
| roberta-large | 88.68% | 88.42% |
| bert-large-uncased | 85.46% | 85.09% |

