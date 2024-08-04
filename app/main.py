import pickle
import keras
import tensorflow as tf
from fastapi import FastAPI 

path = 'model.keras'
model=tf.keras.models.load_model(path)


App = FastAPI()
maxlen=189


tokenizer = pickle.load(open('Tokenizer.pkl', 'rb'))

@App.get('/')
def default():
    return {
        'msg' : 'The App started'
    }

@App.post('/')
def spamDetector(msg: str):
    inp = [msg]
    tokenized=tokenizer.texts_to_sequences(inp)
    padded = keras.utils.pad_sequences(tokenized, maxlen)

    pred = model.predict(padded, verbose=0)

    if pred>=0.35: ## For safety concerns i droped the thrushold
        return {
            "Msg" : "This message is spam!!",
            "code": 1
        }
    else :
        return {
            "Msg" : "This message is not spam. :)",
            "code": 0
        }
