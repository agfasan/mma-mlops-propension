import pickle
import numpy as np
from sklearn.naive_bayes import GaussianNB
import os
# from config import *
# import aws_utils as au

""" Fetch trained models, encoders and tokenizers. Make predictions. """
def fetch_pickle(folder: str, filename: str):
    
    with open(os.path.join(folder, filename), 'rb') as f:
        fetched_object = pickle.load(f)
    
    return fetched_object    

def get_model(folder, filename):
    model = fetch_pickle(folder, filename)

    return model

def predict(sample: dict, folder:str, filename:str) -> dict:
    """
        'sample': List of four floats
    """


    sample_list = np.array(list(sample.values())).reshape(1,-1)
    print("SAMPLE LIST: ",sample_list)
    print("SAMPLE LENGHT: ",len(sample_list))

    model = get_model(folder, filename)

    probability = model.predict(sample_list)

    prediction = {
        'sample': sample,
        'score': int(probability[0])
    }

    return prediction

