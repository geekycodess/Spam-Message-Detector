# Spam-Message-Detector
An End-to-End project to detect spam Text messages. It is complete end-to-end project which contains [Dockerfile](DockerFile) as well as the [FastAPI app](./app/main.py) .

<img src=spam.png width="500rem">

## Requirements:
1. __[Kaggle](https://www.kaggle.com/)__
2. __[Docker](https://www.docker.com/)__
3. __[GitHub](https://www.github.com/)__

## DataSet 
_The DataSet is taken from the kaggle, you can check it here : [Spam Text Message Classification](https://www.kaggle.com/datasets/team-ai/spam-text-message-classification), the DataSet is also available in the repository at_ [DataSet](./model/DataSet.csv) .

## Model 
### Discription
The model is made by using Sequential model, with the layers like `LSTM`, `Bidirectional` and `Embedding`. The model look like this:

<img src='./Model/model.png' width="450rem">

You can check the model devlopment file at the `./Model/LSTM Model.ipynb`

### Model Performance :
#### Accuracy -
* Train set accuracy : _99.89%_
* Validation set accuracy : _99.89%_
#### Loss -
* Train set Loss : _0.0047_
* Validation set Loss : _0.0571_

### Use model :
If you want to use the model just download `./app/model.h5` and `./app/Tokenizer.pkl`, and import them in your system and use accordingly, use tokenizer for data preprocessing and model for the prediction.

## App
### Discription
The app folder have `./app/main.py` file with the App [FastAPI]() application or object and it uses post method to take the input ``msg : str`` and do the preprocessing for you and return a json object with 
```json
{
    msg: weather the given message is spam or not.
    value: 0 - not spam, 1 - spam
}
``` 



 It also have the `requirements.txt` with the nessasary libraries to run the app.

 ### Use app
 You can use the app by the following command:
 ```bash
 cd app
 pip install -r requirements.txt
 uvicorn main:App
 ```

Then the server will start runing go toh the provided link, which you will get in terminal. and go to the `/docs` and try the app.

## DockerFile
It contains the required script to build the `docker image` and it can be done using the following command:
```bash
docker build -t <file name> .
```
once the image is build you can run it using:

```bash
docker run <file name>
```

## License
This project is licensed under the MIT License See the [LICENSE](LICENSE) file for details.