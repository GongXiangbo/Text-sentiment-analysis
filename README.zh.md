Read in English: [Text sentiment classification](README.md)
# 文本情感分析
这是一个机器学习和深度学习实践项目。 在此项目中，你需要预测推特上给定内容的情绪。 简而言之，此任务中提供的情绪要么是积极的，要么是消极的。

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
- lr：默认为2.4e-5
- train_batch_size: 默认为15
- test_batch_size: 默认为1
- warm_up: 默认为1000
- weight_decay: 默认为1e-2
- max_len: 默认为128
- model: 默认为"bert-large-uncased", 也建议使用“roberta-large”或“xlnet-large-cased”

例子:
```
python ./Text-sentiment-classification/train.py --epoch 3 --lr 2.4e-5 --model "roberta-large"
```
