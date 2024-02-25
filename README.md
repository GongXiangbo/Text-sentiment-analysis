English version: [Text sentiment classification](README.en.md)
# 文本情感分析
这是一个深度学习的实战项目。 在此项目中，你需要预测推特上给定内容的情绪。 简而言之，此任务中提供的情绪要么是积极的，要么是消极的。

data文件夹中包含提供的csv格式的推特推文数据集，其中development.csv为训练集，其中包含150000条推文，test.csv为测试集，其中包括50000条推文。sentiment列代表推文的情感，1为积极类别，0为消极类别。

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
- lr：默认为2e-5
- train_batch_size: 默认为15
- test_batch_size: 默认为1
- warm_up: 默认为500
- weight_decay: 默认为1e-2
- max_len: 默认为64
- model: 默认为"bert-large-uncased", 也建议使用“roberta-large”

例子:
```
python ./Text-sentiment-classification/train.py --epoch 5 --lr 3.2e-5 --model "bert-large-uncased"
```
## 实验结果
| Model | Accuracy | F1 (Macro) |
|----------|----------|----------|
| RoBERTa-large | 88.28% | 88.01% |

