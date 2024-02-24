import argparse
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score, accuracy_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer, EvalPrediction
from utils import process_text
from dataset import TextDataset

# Set Argument Parser
parser = argparse.ArgumentParser()
# Training hyperparameters
parser.add_argument('--epoch', type=int, default=3)
parser.add_argument('--lr', type=float, default=2.4e-5)
parser.add_argument('--train_batch_size',type=int, default=30)
parser.add_argument('--test_batch_size',type=int, default=5)
parser.add_argument('--warm_up',type=int, default=1500)
parser.add_argument('--weight_decay',type=float, default=1e-2)
# Tokenizer hyperparameters
parser.add_argument('--max_len', type=int, default=128)
# Model hyperparameters
parser.add_argument('--model',type=str, default='bert-large-uncased')
args = parser.parse_args()


#load training set and preprocessing
df_train = pd.read_csv("data/development.csv")
df_train['text'] = df_train['text'].apply(lambda text: process_text(text))
#load test set and preprocessing
df_test = pd.read_csv("data/test.csv")
df_test['text'] = df_test['text'].apply(lambda text: process_text(text))


# Load Tokenizer associated to the model
tokenizer = AutoTokenizer.from_pretrained(args.model)
model = AutoModelForSequenceClassification.from_pretrained(args.model)
#encode the text
train_encodings = tokenizer(df_train['text'].tolist(), truncation=True, padding=True, max_length=args.max_len)
test_encodings = tokenizer(df_test['text'].tolist(), truncation=True, padding=True, max_length=args.max_len)


train_dataset = TextDataset(train_encodings, df_train['sentiment'].tolist())
test_dataset = TextDataset(test_encodings, df_test['sentiment'].tolist())


# Set metric
def compute_metrics(p: EvalPrediction):
    preds = np.argmax(p.predictions, axis=1)
    return {
      'accuracy': accuracy_score(p.label_ids, preds),
      'f1_macro': f1_score(p.label_ids, preds, average='macro'),
    }


# Set Training Arguments
training_args = TrainingArguments(
    output_dir='./results',             
    num_train_epochs=args.epoch,                 
    learning_rate=args.lr,
    per_device_train_batch_size=args.train_batch_size,     
    per_device_eval_batch_size=args.test_batch_size,      
    warmup_steps=args.warm_up,                   
    weight_decay=args.weight_decay,                        
    logging_steps=1000,                     
    save_steps=1000      
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics
)
# Run Training (Finetuning)
trainer.train()
# Run Evaluating
trainer.evaluate()
