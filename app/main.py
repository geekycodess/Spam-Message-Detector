import pickle
import tensorflow
from keras.utils import pad_sequences
from fastapi import FastAPI 
import numpy as np

App = FastAPI()
maxlen=189

model=tensorflow.keras.models.load_model('model.h5')
tokenizer = pickle.load(open('Tokenizer.pkl', 'rb'))

@App.post('/')
def spamDetector(msg: str):
    inp = np.array([msg])
    tokenized=tokenizer.texts_to_sequences(inp)
    padded = pad_sequences(tokenized, maxlen)

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
