from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, Seq2SeqTrainingArguments, Seq2SeqTrainer, TranslationPipeline
import argparse
from pathlib import Path
 
parser = argparse.ArgumentParser(description="Toki Pona -> English translator.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#parser.add_argument("-f", "--file" , action="file_true", help="translate a file with sentences")

group = parser.add_mutually_exclusive_group()
group.add_argument("-s", "--sentence", type=str,required=False,default="", help="translate a sentence")
group.add_argument("-f", "--file" , type=str,required=False,default="", help="translate a file with sentences")

flags = parser.parse_args()

model_checkpoint = 'model'
model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, return_tensors="py")
pipeline = TranslationPipeline(model=model, tokenizer=tokenizer)
if flags.sentence!='':
    sentence = flags.sentence
    print(pipeline(sentence)[0]['translation_text'])

elif flags.file!='':
    file = flags.file
    path = Path(file)
    f = open(path,mode='r')
    lines = f.readlines()
    trans = pipeline(lines)
    for t in trans:
        print(t['translation_text'])

else: print('Please, use -s or -f options')




